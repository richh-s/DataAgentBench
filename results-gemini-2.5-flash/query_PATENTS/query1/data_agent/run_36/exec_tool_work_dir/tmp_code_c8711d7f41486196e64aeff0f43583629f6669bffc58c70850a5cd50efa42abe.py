code = """import pandas as pd
import json
import re

# Load the full result from the file
with open(locals()['var_function-call-9977547959283513273'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Optimized Date Parsing
def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    # Extract the first 4-digit number that looks like a year
    year_match = re.search(r'\\b(19|20)\\d{2}\\b', date_str)
    if year_match:
        return int(year_match.group(0))
    return None

df['filing_year'] = df['filing_date'].apply(parse_year)

# Filter out rows with invalid years
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Optimized CPC Extraction
def extract_cpc_codes(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        return [item['code'] for item in cpc_list if 'code' in item]
    except (json.JSONDecodeError, TypeError):
        return []

df['cpc_codes_list'] = df['cpc'].apply(extract_cpc_codes)

# Explode the list of CPC codes into separate rows
cpc_df = df.explode('cpc_codes_list')
cpc_df = cpc_df.rename(columns={'cpc_codes_list': 'cpc_code'})

# Drop rows where cpc_code is empty or None after explosion
cpc_df = cpc_df.dropna(subset=['cpc_code'])

# Count patent filings per CPC code and year
filings_by_cpc_year = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Filter for years up to 2022
filings_by_cpc_year = filings_by_cpc_year[filings_by_cpc_year['filing_year'] <= 2022]

# Prepare for EMA calculation more efficiently
# Create a MultiIndex for all possible cpc_code and year combinations
all_cpc_codes = filings_by_cpc_year['cpc_code'].unique()
all_years = range(filings_by_cpc_year['filing_year'].min(), 2023) # Up to 2022
idx = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])

# Reindex and fill missing values with 0
full_filings = filings_by_cpc_year.set_index(['cpc_code', 'filing_year']).reindex(idx, fill_value=0).reset_index()

# Sort for EMA calculation
full_filings = full_filings.sort_values(by=['cpc_code', 'filing_year'])

# Calculate EMA using groupby and transform
alpha = 0.2
full_filings['ema'] = full_filings.groupby('cpc_code')['patent_count'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
idx_max_ema = full_filings.groupby('cpc_code')['ema'].idxmax()
best_year_cpc = full_filings.loc[idx_max_ema]

# Filter for best year 2022
cpc_best_year_2022 = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_year_2022))"""

env_args = {'var_function-call-9977547959283513273': 'file_storage/function-call-9977547959283513273.json'}

exec(code, env_args)
