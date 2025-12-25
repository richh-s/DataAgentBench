code = """import pandas as pd
import json
import re

# Read the full result from the file
with open(locals()['var_function-call-8060160587968561136'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to extract year from filing_date
def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

# Function to extract CPC codes
def extract_cpc_codes(cpc_str):
    if isinstance(cpc_str, str):
        try:
            cpc_list = json.loads(cpc_str)
            return [cpc['code'] for cpc in cpc_list if 'code' in cpc]
        except json.JSONDecodeError:
            return []
    return []

df['filing_year'] = df['filing_date'].apply(extract_year)
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

df['cpc_codes'] = df['cpc'].apply(extract_cpc_codes)
df_exploded = df.explode('cpc_codes')

# Keep only valid CPC codes
df_exploded = df_exploded[df_exploded['cpc_codes'].apply(lambda x: isinstance(x, str) and len(x) > 0)]

# Group by year and CPC code to count filings
filings_by_year_cpc = df_exploded.groupby(['filing_year', 'cpc_codes']).size().reset_index(name='filings')

# Prepare data for EMA calculation (fill missing years with 0 filings)
all_years = range(filings_by_year_cpc['filing_year'].min(), filings_by_year_cpc['filing_year'].max() + 1)
all_cpc_codes = filings_by_year_cpc['cpc_codes'].unique()

ema_results = []
smoothing_factor = 0.2

for cpc_code in all_cpc_codes:
    cpc_data = filings_by_year_cpc[filings_by_year_cpc['cpc_codes'] == cpc_code]
    cpc_data = cpc_data.set_index('filing_year').reindex(all_years, fill_value=0).reset_index()
    cpc_data = cpc_data.rename(columns={'index': 'filing_year'})

    # Calculate EMA
    cpc_data['ema'] = cpc_data['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results.append(cpc_data)

ema_df = pd.concat(ema_results)

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-8060160587968561136': 'file_storage/function-call-8060160587968561136.json'}

exec(code, env_args)
