code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-5336319047275791554']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Robust year extraction
def extract_year(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NA
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if year_match:
        return int(year_match.group(0))
    return pd.NA

df['filing_year'] = df['filing_date'].apply(extract_year)
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Filter out years not within a reasonable range
df = df[(df['filing_year'] >= 1950) & (df['filing_year'] <= 2023)] 

# Efficiently parse CPC codes and flatten
def parse_cpc_codes(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        return [item.get('code') for item in cpc_list if item.get('code')]
    except (json.JSONDecodeError, TypeError):
        return []

df['parsed_cpc_codes'] = df['cpc'].apply(parse_cpc_codes)
df_exploded = df.explode('parsed_cpc_codes')
df_exploded = df_exploded.rename(columns={'parsed_cpc_codes': 'cpc_code'})
df_exploded = df_exploded.dropna(subset=['cpc_code'])

# Extract level 5 CPC group codes (first 5 characters)
df_exploded['cpc_group_level_5'] = df_exploded['cpc_code'].apply(lambda x: x[:5] if isinstance(x, str) and len(x) >= 5 else pd.NA)
df_exploded = df_exploded.dropna(subset=['cpc_group_level_5'])

# Group by cpc_group_level_5 and filing_year to count filings
yearly_filings = df_exploded.groupby(['cpc_group_level_5', 'filing_year']).size().reset_index(name='filings')

if yearly_filings.empty:
    result = []
else:
    # Calculate Exponential Moving Average
    smoothing_factor = 0.2

    min_year = yearly_filings['filing_year'].min()
    max_year = yearly_filings['filing_year'].max()
    all_years = pd.Series(range(min_year, max_year + 1))

    ema_results = {}
    best_year_for_cpc = {}

    for cpc_group_code in yearly_filings['cpc_group_level_5'].unique():
        # Create a series for the current CPC group code, reindex to fill missing years with 0
        series_data = yearly_filings[yearly_filings['cpc_group_level_5'] == cpc_group_code].set_index('filing_year')['filings']
        full_series = series_data.reindex(all_years, fill_value=0)

        if not full_series.empty:
            ema = full_series.ewm(alpha=smoothing_factor, adjust=False).mean()
            ema_results[cpc_group_code] = ema
            best_year = ema.idxmax()
            best_year_for_cpc[cpc_group_code] = best_year

    # Filter for CPC codes whose best year is 2022
    result = [cpc for cpc, year in best_year_for_cpc.items() if year == 2022]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5336319047275791554': 'file_storage/function-call-5336319047275791554.json'}

exec(code, env_args)
