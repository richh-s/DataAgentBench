code = """import json
import pandas as pd

def parse_date(date_str):
    if not isinstance(date_str, str): # Handle non-string types gracefully
        return None
    try:
        # Attempt to parse common date formats
        return pd.to_datetime(date_str, errors='coerce', format='%Y, %B %dth') \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%Y, %B %d')) \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%dth %b %Y')) \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%b %dth, %Y')) \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%Y-%m-%d')) \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%B %d, %Y')) \
               .fillna(pd.to_datetime(date_str, errors='coerce', format='%d %b %Y')) \
               .fillna(pd.to_datetime(date_str, errors='coerce')) # Generic parsing
    except:
        return None

all_patents = pd.read_json(locals()['var_function-call-159961854333049397'])

# Filter for German patents and second half of 2019
german_patents = all_patents[all_patents['Patents_info'].str.contains('country_code: DE', na=False)].copy()
german_patents['grant_date_parsed'] = german_patents['grant_date'].apply(parse_date)
german_patents = german_patents[german_patents['grant_date_parsed'].dt.month >= 7]

# Extract CPC codes and filing year
cpc_data = []
for _, row in german_patents.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            if 'code' in cpc_item:
                cpc_data.append({
                    'cpc_group': cpc_item['code'][:4],
                    'filing_year': parse_date(row['filing_date']).year if parse_date(row['filing_date']) else None
                })
    except (json.JSONDecodeError, TypeError):
        continue
cpc_df = pd.DataFrame(cpc_data).dropna()
cpc_df['filing_year'] = cpc_df['filing_year'].astype(int)

# Calculate yearly filings for each CPC group
yearly_filings = cpc_df.groupby(['cpc_group', 'filing_year']).size().unstack(fill_value=0)

# Calculate EMA
smoothing_factor = 0.1
ema_result = {}
for cpc_group in yearly_filings.index:
    ema_values = []
    current_ema = 0
    for year in sorted(yearly_filings.columns):
        current_filings = yearly_filings.loc[cpc_group, year]
        current_ema = (current_filings * smoothing_factor) + (current_ema * (1 - smoothing_factor))
        ema_values.append({'year': year, 'ema': current_ema})
    ema_result[cpc_group] = ema_values

# Find the best year for each CPC group
best_ema_per_cpc = {}
for cpc_group, ema_values in ema_result.items():
    if ema_values:
        best_year_entry = max(ema_values, key=lambda x: x['ema'])
        best_ema_per_cpc[cpc_group] = {
            'best_year': best_year_entry['year'],
            'max_ema': best_year_entry['ema']
        }

# Sort by max_ema and get the top CPC groups
sorted_cpc_groups = sorted(best_ema_per_cpc.items(), key=lambda item: item[1]['max_ema'], reverse=True)

# Extract the CPC group codes at level 4 for querying definition database
top_cpc_codes_level4 = [cpc_group for cpc_group, _ in sorted_cpc_groups]

# Prepare output as JSON string
output = []
for cpc_group, details in best_ema_per_cpc.items():
    output.append({
        'cpc_group': cpc_group,
        'best_year': details['best_year'],
        'max_ema': details['max_ema']
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-13781591671737650296': [], 'var_function-call-159961854333049397': 'file_storage/function-call-159961854333049397.json'}

exec(code, env_args)
