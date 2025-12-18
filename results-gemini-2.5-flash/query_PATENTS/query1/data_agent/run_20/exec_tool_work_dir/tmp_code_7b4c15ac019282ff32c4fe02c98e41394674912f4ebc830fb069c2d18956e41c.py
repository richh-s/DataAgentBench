code = """import pandas as pd
import json
import re

# Access the full result from the file path
with open(locals()['var_function-call-17598841612245828655']['query_db_response']['results']) as f:
    publication_data = json.load(f)

# Create a DataFrame
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
    if isinstance(cpc_raw, str):
        try:
            cpc_data = json.loads(cpc_raw)
            if isinstance(cpc_data, list):
                for item in cpc_data:
                    if isinstance(item, dict) and 'code' in item and isinstance(item['code'], str):
                        all_cpc_codes.append({'cpc_code': item['code'], 'filing_year': row['filing_year']})
        except json.JSONDecodeError:
            # Malformed JSON string, skip
            continue
    # If cpc_raw is not a string, or if it's None, it will be skipped.

cpc_df = pd.DataFrame(all_cpc_codes)

# Group by CPC code and year, then count filings
cpc_filings_yearly = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings_count')

# Calculate Exponential Moving Average
alpha = 0.2
ema_results = []
for cpc_code, group in cpc_filings_yearly.groupby('cpc_code'):
    group = group.sort_values(by='filing_year').copy()
    group['ema'] = group['filings_count'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(group)

if ema_results:
    ema_df = pd.concat(ema_results)

    # Find the best year for each CPC code (year with highest EMA)
    idx = ema_df.groupby('cpc_code')['ema'].idxmax()
    best_year_ema = ema_df.loc[idx]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].tolist()
else:
    cpc_codes_2022_best = []

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-17903615919587865458': 'file_storage/function-call-17903615919587865458.json', 'var_function-call-17598841612245828655': 'file_storage/function-call-17598841612245828655.json'}

exec(code, env_args)
