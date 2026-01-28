code = """import json
import pandas as pd
import re

# Load the data from the file
file_path = var_functions.query_db:7
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse CPC codes and extract years
records = []
for row in data:
    cpc_json = row['cpc']
    pub_date = row['publication_date']
    
    # Extract year from publication date
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
            
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            records.append({
                'cpc_code': code,
                'year': year
            })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(records)

# Extract CPC group at level 5 (format: XNNN/NN)
# We need to extract just the group part before the slash
df['cpc_group'] = df['cpc_code'].str.extract(r'^([A-Z]\d{2}[A-Z]\d{2}/\d{2})')

# Filter for level 5 CPC codes (should have exactly 5 parts when split by / or spaces)
# Actually, level 5 in CPC is typically like G06F16/00, where:
# - Section: 1 char (G)
# - Class: 2 digits (06)
# - Subclass: 1 char (F)
# - Main group: 3+ digits (16)
# - Subgroup: 2+ digits (/00)
# So we want codes that match pattern: [A-Z]\d{2}[A-Z]\d{2,}/\d{2,}
valid_level5 = df['cpc_code'].str.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$')
df_level5 = df[valid_level5].copy()

# Count filings per CPC group per year
cpc_year_counts = df_level5.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Get all years and all CPC codes
years = sorted(cpc_year_counts['year'].unique())
cpc_codes = cpc_year_counts['cpc_code'].unique()

# Create a complete dataframe with all combinations
all_combinations = []
for cpc in cpc_codes:
    for year in years:
        all_combinations.append({'cpc_code': cpc, 'year': year, 'count': 0})

df_complete = pd.DataFrame(all_combinations)

# Update with actual counts
df_counts = df_complete.set_index(['cpc_code', 'year'])
df_actual = cpc_year_counts.set_index(['cpc_code', 'year'])
df_counts.update(df_actual)
df_counts = df_counts.reset_index()

# Calculate exponential moving average for each CPC code (smoothing factor 0.2)
def calculate_ema(group):
    # Sort by year
    group = group.sort_values('year')
    # Calculate EMA
    alpha = 0.2
    ema_values = []
    ema = group['count'].iloc[0]  # Start with first value
    ema_values.append(ema)
    
    for i in range(1, len(group)):
        ema = alpha * group['count'].iloc[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    group['ema'] = ema_values
    return group

df_ema = df_counts.groupby('cpc_code').apply(calculate_ema).reset_index(drop=True)

# Find the year with highest EMA for each CPC code
df_max_ema = df_ema.loc[df_ema.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes where best year is 2022
df_best_2022 = df_max_ema[df_max_ema['year'] == 2022]

print(f"Number of CPC codes with best year 2022: {len(df_best_2022)}")
if len(df_best_2022) > 0:
    print("Top 10 CPC codes with best year 2022:")
    print(df_best_2022.head(10))

# Get CPC group codes at level 5
cpc_groups_2022 = df_best_2022['cpc_code'].tolist()

print(f"\nCPC group codes at level 5 with best year 2022: {cpc_groups_2022[:10]}...")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
