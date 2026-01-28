code = """import json
import pandas as pd
import re

# Load the publication data from the stored variable
result_key = 'var_functions.query_db:6'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        publications = json.load(f)
else:
    publications = result_file

# Parse CPC codes and extract years
cpc_year_data = []

for pub in publications:
    cpc_str = pub.get('cpc', '')
    pub_date_str = pub.get('publication_date', '')
    
    if not cpc_str or not pub_date_str:
        continue
    
    # Extract year from publication date (format: "Aug 3rd, 2021")
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON string
    try:
        cpc_list = json.loads(cpc_str)
    except:
        # Try to evaluate as Python literal if JSON fails
        try:
            cpc_list = eval(cpc_str)
        except:
            continue
    
    if not isinstance(cpc_list, list):
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            code = cpc_item['code']
            # Store the full code and also extract group (first part before /)
            if '/' in code:
                group = code.split('/')[0]
            else:
                group = code
            
            cpc_year_data.append({
                'full_code': code,
                'group_code': group,
                'year': year,
                'inventive': cpc_item.get('inventive', False),
                'first': cpc_item.get('first', False)
            })

# Convert to DataFrame for easier processing
df = pd.DataFrame(cpc_year_data)

# Get CPC level 5 codes from CPCDefinition_database
cpc_level5_key = 'var_functions.query_db:5'
cpc_level5_data = locals()[cpc_level5_key]
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

# Filter our data to only include CPC groups that are at level 5
df_level5 = df[df['group_code'].isin(cpc_level5_symbols)].copy()

# Count filings per group per year
yearly_counts = df_level5.groupby(['group_code', 'year']).size().reset_index(name='count')

# Get all years and groups
all_years = sorted(yearly_counts['year'].unique())
all_groups = yearly_counts['group_code'].unique()

# Create complete matrix with all combinations
complete_matrix = []
for group in all_groups:
    for year in all_years:
        complete_matrix.append({'group_code': group, 'year': year, 'count': 0})

complete_df = pd.DataFrame(complete_matrix)

# Merge with actual counts
merged_counts = pd.merge(complete_df, yearly_counts, on=['group_code', 'year'], how='left', suffixes=('_default', '_actual'))
merged_counts['final_count'] = merged_counts['count_actual'].fillna(0)

# Calculate exponential moving average for each group
smoothing_factor = 0.2

def calculate_ema(group_data):
    group_data = group_data.sort_values('year')
    ema_values = []
    ema_prev = None
    
    for _, row in group_data.iterrows():
        count = row['final_count']
        if ema_prev is None:
            # First value - use actual count
            ema = count
        else:
            # EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
            ema = smoothing_factor * count + (1 - smoothing_factor) * ema_prev
        
        ema_values.append(ema)
        ema_prev = ema
    
    group_data = group_data.copy()
    group_data['ema'] = ema_values
    return group_data

# Apply EMA calculation to each group
ema_results = []
for group in all_groups:
    group_data = merged_counts[merged_counts['group_code'] == group]
    group_ema = calculate_ema(group_data)
    ema_results.append(group_ema)

ema_df = pd.concat(ema_results, ignore_index=True)

# Find best year for each group (year with highest EMA)
best_years = ema_df.loc[ema_df.groupby('group_code')['ema'].idxmax()][['group_code', 'year', 'ema']]

# Filter groups whose best year is 2022
groups_best_2022 = best_years[best_years['year'] == 2022]['group_code'].tolist()

# Format the result
result = {
    'total_publications': len(publications),
    'total_cpc_entries': len(cpc_year_data),
    'level5_groups_analyzed': len(all_groups),
    'years_analyzed': len(all_years),
    'year_range': f"{min(all_years)} to {max(all_years)}" if all_years else "No data",
    'groups_with_best_year_2022': groups_best_2022,
    'count_best_2022': len(groups_best_2022)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
