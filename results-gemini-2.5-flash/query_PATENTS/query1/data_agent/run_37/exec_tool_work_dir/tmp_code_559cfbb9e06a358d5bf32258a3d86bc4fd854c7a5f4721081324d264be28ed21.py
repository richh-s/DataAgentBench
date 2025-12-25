code = """import pandas as pd
import json
import re

# Load the full result from the file path
with open(locals()['var_function-call-13431301354625501947'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Extract year from filing_date
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Explode CPC codes
all_cpc_codes = []
for index, row in df.iterrows():
    if pd.isna(row['cpc']):
        continue
    cpc_list = json.loads(row['cpc'])
    for cpc_item in cpc_list:
        code = cpc_item.get('code')
        if code and len(code) >= 7 and code[6].isalpha(): # Level 5 CPC codes have a letter at the 7th position (e.g., A61B5/0000)
             # Extract the first 7 characters for level 5 group code
            all_cpc_codes.append({'cpc_group_code': code[:7], 'filing_year': row['filing_year']})

cpc_df = pd.DataFrame(all_cpc_codes)

# Filter for years 2010-2022
cpc_df = cpc_df[(cpc_df['filing_year'] >= 2010) & (cpc_df['filing_year'] <= 2022)]

# Count filings per CPC code and year
filings_count = cpc_df.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
alpha = 0.2
ema_results = []
for cpc_code in filings_count['cpc_group_code'].unique():
    cpc_data = filings_count[filings_count['cpc_group_code'] == cpc_code].sort_values(by='filing_year')
    ema = []
    if not cpc_data.empty:
        # Initialize EMA for the first year with the actual filings count
        ema_current = cpc_data.iloc[0]['filings']
        ema.append({'cpc_group_code': cpc_code, 'filing_year': cpc_data.iloc[0]['filing_year'], 'ema': ema_current})

        for i in range(1, len(cpc_data)):
            ema_current = (cpc_data.iloc[i]['filings'] * alpha) + (ema_current * (1 - alpha))
            ema.append({'cpc_group_code': cpc_code, 'filing_year': cpc_data.iloc[i]['filing_year'], 'ema': ema_current})
    ema_results.extend(ema)

ema_df = pd.DataFrame(ema_results)

# Identify the best year for each CPC code
best_year_ema = ema_df.loc[ema_df.groupby('cpc_group_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_group_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-1162082034067506253': 'file_storage/function-call-1162082034067506253.json', 'var_function-call-2188090953045820560': 'file_storage/function-call-2188090953045820560.json', 'var_function-call-13431301354625501947': 'file_storage/function-call-13431301354625501947.json'}

exec(code, env_args)
