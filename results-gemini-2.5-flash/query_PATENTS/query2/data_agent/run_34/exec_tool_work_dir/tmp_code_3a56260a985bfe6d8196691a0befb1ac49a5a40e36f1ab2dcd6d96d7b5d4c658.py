code = """import pandas as pd
import json
import re

# Load the full result from the file
with open(locals()['var_function-call-11734270909720189975'], 'r') as f:
    publication_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(publication_data)

# Function to parse natural language dates
def parse_date(date_str):
    if not isinstance(date_str, str):
        return None
    # Handle common date formats
    date_str = date_str.replace('dated ', '').replace('the ', '').replace(',', '').strip()
    try:
        # Try parsing with month name first
        return pd.to_datetime(date_str, format='%d %B %Y', errors='coerce')
    except:
        try:
            return pd.to_datetime(date_str, format='%B %d %Y', errors='coerce')
        except:
            return pd.to_datetime(date_str, errors='coerce')

df['parsed_grant_date'] = df['grant_date'].apply(parse_date)
df['parsed_filing_date'] = df['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019
start_date = pd.to_datetime('2019-07-01')
end_date = pd.to_datetime('2019-12-31')
df_filtered_by_grant = df[(df['parsed_grant_date'] >= start_date) & (df['parsed_grant_date'] <= end_date)]

# Filter for Germany (country code DE)
def extract_country_code(patents_info):
    if not isinstance(patents_info, str):
        return None
    match = re.search(r'country_code\":\"(.*?)\"', patents_info)
    if match:
        return match.group(1)
    return None

df_filtered_by_grant['country_code'] = df_filtered_by_grant['Patents_info'].apply(extract_country_code)
df_filtered_germany = df_filtered_by_grant[df_filtered_by_grant['country_code'] == 'DE']

# Extract filing year and CPC codes
df_filtered_germany['filing_year'] = df_filtered_germany['parsed_filing_date'].dt.year

def extract_cpc_level4(cpc_json_str):
    if not isinstance(cpc_json_str, str):
        return []
    try:
        cpc_list = json.loads(cpc_json_str)
        level4_codes = [cpc_item['code'][:4] for cpc_item in cpc_list if 'code' in cpc_item and len(cpc_item['code']) >= 4]
        return list(set(level4_codes)) # Get unique level 4 CPC codes
    except json.JSONDecodeError:
        return []

df_filtered_germany['cpc_level4_codes'] = df_filtered_germany['cpc'].apply(extract_cpc_level4)

# Explode the DataFrame to have one row per CPC code
df_exploded = df_filtered_germany.explode('cpc_level4_codes')

# Count filings per CPC level 4 group per year
cpc_filings_per_year = df_exploded.groupby(['cpc_level4_codes', 'filing_year']).size().reset_index(name='filings_count')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []

for cpc_group, group_df in cpc_filings_per_year.groupby('cpc_level4_codes'):
    group_df = group_df.sort_values(by='filing_year')
    ema = []
    if not group_df.empty:
        # Initialize EMA with the first filing count if available
        current_ema = group_df['filings_count'].iloc[0] if not group_df['filings_count'].empty else 0
        ema.append({'cpc_level4_codes': cpc_group, 'filing_year': group_df['filing_year'].iloc[0], 'ema': current_ema})

        for i in range(1, len(group_df)):
            current_ema = alpha * group_df['filings_count'].iloc[i] + (1 - alpha) * current_ema
            ema.append({'cpc_level4_codes': cpc_group, 'filing_year': group_df['filing_year'].iloc[i], 'ema': current_ema})
    ema_results.extend(ema)

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC group at level 4 (highest EMA)
best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_level4_codes')['ema'].idxmax()]

# Rename columns for clarity
best_year_per_cpc = best_year_per_cpc.rename(columns={'cpc_level4_codes': 'cpc_group_code', 'filing_year': 'best_year'})

print('__RESULT__:')
print(best_year_per_cpc.to_json(orient='records'))"""

env_args = {'var_function-call-11734270909720189975': 'file_storage/function-call-11734270909720189975.json'}

exec(code, env_args)
