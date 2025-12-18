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
    # Clean common prefixes/suffixes and normalize spaces
    date_str = date_str.lower().replace('dated', '').replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').strip()
    # Try to extract a 4-digit year directly
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if year_match:
        return int(year_match.group(0))
    # If direct year extraction fails, try a more general date parsing
    try:
        return pd.to_datetime(date_str, errors='coerce').year
    except:
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

# Pivot table for vectorized EMA calculation
pivoted_filings = filings_by_cpc_year.pivot_table(index='filing_year', columns='cpc_code', values='patent_count').fillna(0)

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
ema_df = pivoted_filings.ewm(alpha=alpha, adjust=False).mean()

# Unpivot EMA results back to long format
ema_df_long = ema_df.stack().reset_index(name='ema')
ema_df_long = ema_df_long.rename(columns={'level_1': 'cpc_code'})

# Find the year with the highest EMA for each CPC code
idx_max_ema = ema_df_long.groupby('cpc_code')['ema'].idxmax()
best_year_cpc = ema_df_long.loc[idx_max_ema]

# Filter for best year 2022
cpc_best_year_2022 = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].tolist()

# Filter for CPC group codes at level 5
# A CPC group code at level 5 usually has the format like 'A01B1/00'.
# This means a section (1 char), class (2 chars), subclass (1 char), main group (1-3 digits), slash, subgroup (2-3 digits).
# A common characteristic for level 5 in CPC codes is having a '/' and being longer than just the main group.
# The first 4 characters are usually the class and subclass (e.g., A01B). The 5th character being a digit often indicates the start of the main group.
# We are looking for group codes at level 5, which are often 4 characters followed by a number and a slash. E.g., A01B1/00.
# The definition of CPC levels can be complex, but a simple heuristic for level 5 can be codes with a length >= 6 and containing a '/'.
cpc_level_5_filtered = [cpc_code for cpc_code in cpc_best_year_2022 if '/' in cpc_code and len(cpc_code) >= 6]

print("__RESULT__:")
print(json.dumps(cpc_level_5_filtered))"""

env_args = {'var_function-call-9977547959283513273': 'file_storage/function-call-9977547959283513273.json'}

exec(code, env_args)
