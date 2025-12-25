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
    date_str = date_str.replace('dated ', '').replace('the ', '').replace(',', '').strip()
    try:
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
df_filtered_by_grant = df[(df['parsed_grant_date'] >= start_date) & (df['parsed_grant_date'] <= end_date)].copy()

# Filter for Germany (country code DE)
def extract_country_code(patents_info):
    if not isinstance(patents_info, str):
        return None
    # Search for "DE" or "Germany" in a case-insensitive manner
    if re.search(r'\bDE\b|\bGERMANY\b', patents_info, re.IGNORECASE):
        return 'DE'
    return None

df_filtered_by_grant['country_code'] = df_filtered_by_grant['Patents_info'].apply(extract_country_code)
df_filtered_germany = df_filtered_by_grant[df_filtered_by_grant['country_code'] == 'DE'].copy()

# Extract filing year and CPC codes
if not df_filtered_germany.empty:
    df_filtered_germany['filing_year'] = df_filtered_germany['parsed_filing_date'].dt.year
else:
    # If no German patents, set filing_year to None or handle appropriately
    df_filtered_germany['filing_year'] = None


def extract_cpc_level4(cpc_json_str):
    if not isinstance(cpc_json_str, str):
        return []
    try:
        cpc_list = json.loads(cpc_json_str)
        level4_codes = [cpc_item['code'][:4] for cpc_item in cpc_list if 'code' in cpc_item and len(cpc_item['code']) >= 4]
        return list(set(level4_codes))
    except json.JSONDecodeError:
        return []

df_filtered_germany['cpc_level4_codes'] = df_filtered_germany['cpc'].apply(extract_cpc_level4)

# Explode the DataFrame to have one row per CPC code
df_exploded = df_filtered_germany.explode('cpc_level4_codes').dropna(subset=['cpc_level4_codes'])

# Count filings per CPC level 4 group per year
if not df_exploded.empty:
    cpc_filings_per_year = df_exploded.groupby(['cpc_level4_codes', 'filing_year']).size().reset_index(name='filings_count')
else:
    cpc_filings_per_year = pd.DataFrame(columns=['cpc_level4_codes', 'filing_year', 'filings_count'])

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []

if not cpc_filings_per_year.empty:
    for cpc_group, group_df in cpc_filings_per_year.groupby('cpc_level4_codes'):
        group_df = group_df.sort_values(by='filing_year')
        current_ema = 0
        if not group_df.empty:
            current_ema = group_df['filings_count'].iloc[0]
            ema_results.append({'cpc_group_code': cpc_group, 'filing_year': group_df['filing_year'].iloc[0], 'ema': current_ema})

            for i in range(1, len(group_df)):
                current_ema = alpha * group_df['filings_count'].iloc[i] + (1 - alpha) * current_ema
                ema_results.append({'cpc_group_code': cpc_group, 'filing_year': group_df['filing_year'].iloc[i], 'ema': current_ema})

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC group at level 4 (highest EMA)
if not ema_df.empty:
    best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_group_code')['ema'].idxmax()].copy()
    # Ensure filing_year is int type for consistency if all are years
    best_year_per_cpc['filing_year'] = best_year_per_cpc['filing_year'].astype(int)
else:
    best_year_per_cpc = pd.DataFrame(columns=['cpc_group_code', 'filing_year', 'ema'])

best_year_per_cpc = best_year_per_cpc.rename(columns={'filing_year': 'best_year'})

print('__RESULT__:')
print(best_year_per_cpc.to_json(orient='records'))"""

env_args = {'var_function-call-11734270909720189975': 'file_storage/function-call-11734270909720189975.json'}

exec(code, env_args)
