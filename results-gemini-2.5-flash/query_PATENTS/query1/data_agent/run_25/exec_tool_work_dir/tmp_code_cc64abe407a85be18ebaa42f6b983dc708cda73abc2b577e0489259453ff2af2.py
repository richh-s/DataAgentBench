code = """import pandas as pd
import json
import re

# Load the data from the stored file
with open(locals()['var_function-call-13225136143239241627'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to extract year from filing_date
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

# Function to extract all CPC codes (without filtering by level yet)
def extract_all_cpc_codes(cpc_json_string):
    cpc_codes = []
    if isinstance(cpc_json_string, str):
        try:
            cpc_entries = json.loads(cpc_json_string)
            for entry in cpc_entries:
                code = entry.get('code')
                if code:
                    cpc_codes.append(code)
        except json.JSONDecodeError:
            pass
    return list(set(cpc_codes))

df['filing_year'] = df['filing_date'].apply(extract_year)
df['all_cpc_codes'] = df['cpc'].apply(extract_all_cpc_codes)

# Explode the DataFrame to have one CPC code per row
df_exploded = df.explode('all_cpc_codes')

# Filter out rows with no valid year or CPC code
df_filtered = df_exploded.dropna(subset=['filing_year', 'all_cpc_codes'])

# Count patent filings per CPC code per year
filings_per_year_cpc = df_filtered.groupby(['all_cpc_codes', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_results = {}

for cpc_code in filings_per_year_cpc['all_cpc_codes'].unique():
    cpc_data = filings_per_year_cpc[filings_per_year_cpc['all_cpc_codes'] == cpc_code].sort_values(by='filing_year')
    ema = []
    if not cpc_data.empty:
        ema_current = cpc_data.iloc[0]['filings']
        ema.append(ema_current)
        for i in range(1, len(cpc_data)):
            ema_current = (cpc_data.iloc[i]['filings'] * smoothing_factor) + (ema_current * (1 - smoothing_factor))
            ema.append(ema_current)
    cpc_data['ema'] = ema
    ema_results[cpc_code] = cpc_data

# Find the best year (highest EMA) for each CPC code
best_year_cpc = {}
for cpc_code, cpc_df in ema_results.items():
    if not cpc_df.empty:
        best_year = cpc_df.loc[cpc_df['ema'].idxmax()]
        best_year_cpc[cpc_code] = best_year['filing_year']

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = [cpc for cpc, year in best_year_cpc.items() if year == 2022]

print('__RESULT__:')
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13225136143239241627': 'file_storage/function-call-13225136143239241627.json', 'var_function-call-11412886215749648234': []}

exec(code, env_args)
