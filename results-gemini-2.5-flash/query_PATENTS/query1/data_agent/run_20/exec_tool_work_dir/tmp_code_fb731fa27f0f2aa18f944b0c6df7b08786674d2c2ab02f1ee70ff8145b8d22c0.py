code = """import pandas as pd
import json
import re

# Access the full result from the publication_database
with open(locals()['var_function-call-17598841612245828655']['query_db_response']['results']) as f:
    publication_data = json.load(f)

# Create a DataFrame for publication data
df = pd.DataFrame(publication_data)

# Extract year from 'filing_date' more robustly
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'(\d{4})', date_string)
        if match:
            return int(match.group(1))
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)
df.dropna(subset=['filing_year'], inplace=True)
df['filing_year'] = df['filing_year'].astype(int)

all_cpc_codes = []
for index, row in df.iterrows():
    cpc_raw = row['cpc']
    if isinstance(cpc_raw, str) and cpc_raw.strip(): # Check if it's a non-empty string
        try:
            cpc_data = json.loads(cpc_raw)
            if isinstance(cpc_data, list):
                for item in cpc_data:
                    # Ensure item is a dictionary before trying to access 'code'
                    if isinstance(item, dict) and 'code' in item and isinstance(item['code'], str):
                        all_cpc_codes.append({'cpc_code': item['code'], 'filing_year': row['filing_year']})
        except json.JSONDecodeError:
            continue # Skip rows with malformed JSON

cpc_df = pd.DataFrame(all_cpc_codes)

# Group by CPC code and year, then count filings
cpc_filings_yearly = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings_count')

# Calculate Exponential Moving Average
alpha = 0.2
ema_results = []
if not cpc_filings_yearly.empty:
    cpc_filings_yearly = cpc_filings_yearly.sort_values(by=['cpc_code', 'filing_year'])
    for cpc_code_group, group in cpc_filings_yearly.groupby('cpc_code'):
        group = group.copy()
        group['ema'] = group['filings_count'].ewm(alpha=alpha, adjust=False).mean()
        ema_results.append(group)

if ema_results:
    ema_df = pd.concat(ema_results)
    idx = ema_df.groupby('cpc_code')['ema'].idxmax()
    best_year_ema = ema_df.loc[idx]
    cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].tolist()
else:
    cpc_codes_2022_best = []

# Access the full result from the CPCDefinition_database for level 5 CPC codes
with open(locals()['var_function-call-1221715705209923609']['query_db_response']['results']) as f:
    level_5_cpc_data = json.load(f)

level_5_cpc_symbols = [item['symbol'] for item in level_5_cpc_data if 'symbol' in item]

# Filter the cpc_codes_2022_best to include only level 5 CPC codes
final_cpc_codes = [code for code in cpc_codes_2022_best if code in level_5_cpc_symbols]

print('__RESULT__:')
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-17903615919587865458': 'file_storage/function-call-17903615919587865458.json', 'var_function-call-17598841612245828655': 'file_storage/function-call-17598841612245828655.json', 'var_function-call-1221715705209923609': 'file_storage/function-call-1221715705209923609.json'}

exec(code, env_args)
