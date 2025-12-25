code = """import pandas as pd
import json
import re

# Access the full result from the file path
with open(locals()['var_function-call-17903615919587865458']['query_db_response']['results']) as f:
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

# Extract CPC codes and flatten the list
all_cpc_codes = []
for index, row in df.iterrows():
    cpc_str = row['cpc']
    if isinstance(cpc_str, str):
        try:
            cpc_list = json.loads(cpc_str)
            if isinstance(cpc_list, list):
                for cpc_item in cpc_list:
                    if isinstance(cpc_item, dict) and 'code' in cpc_item:
                        all_cpc_codes.append({'cpc_code': cpc_item['code'], 'filing_year': row['filing_year']})
        except json.JSONDecodeError:
            # Skip rows with malformed JSON in 'cpc'
            continue

cpc_df = pd.DataFrame(all_cpc_codes)

# Group by CPC code and year, then count filings
cpc_filings_yearly = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings_count')

# Calculate Exponential Moving Average
# Need to sort by year for correct EMA calculation
cpc_filings_yearly.sort_values(by=['cpc_code', 'filing_year'], inplace=True)

# Define smoothing factor alpha
alpha = 0.2

# Calculate EMA for each CPC code
ema_results = []
for cpc_code, group in cpc_filings_yearly.groupby('cpc_code'):
    group = group.sort_values(by='filing_year').copy() # Add .copy() to avoid SettingWithCopyWarning
    # Initialize EMA for the first year with the actual filings count
    group['ema'] = group['filings_count'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(group)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC code (year with highest EMA)
best_year_ema = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-17903615919587865458': 'file_storage/function-call-17903615919587865458.json'}

exec(code, env_args)
