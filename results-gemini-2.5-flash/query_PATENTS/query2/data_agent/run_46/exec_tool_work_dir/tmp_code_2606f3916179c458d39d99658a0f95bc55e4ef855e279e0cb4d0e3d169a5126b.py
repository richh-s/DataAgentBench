code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-17420446429769094488'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

# Filter for Germany first to reduce dataframe size, based on the problem description.
def extract_country_code_from_patents_info(patents_info):
    if pd.isna(patents_info):
        return None
    if 'Germany' in patents_info:
        return 'DE'
    # Fallback to other methods if 'Germany' not found but still want a country code
    match = re.search(r'\(ID ([A-Z]{2})-\d{12}-A\)', patents_info)
    if match:
        return match.group(1)
    match = re.search(r'application no. ([A-Z]{2})-\d{12}-A', patents_info)
    if match:
        return match.group(1)
    match = re.search(r'publication no. ([A-Z]{2})-\d{10}-B\d', patents_info)
    if match:
        return match.group(1)
    match = re.search(r'In ([A-Z]{2}), the application', patents_info)
    if match:
        return match.group(1)
    match = re.search(r'Patent application \(ID ([A-Z]{2})-\d{12}-A\)', patents_info)
    if match:
        return match.group(1)
    return None

df_publication['country_code'] = df_publication['Patents_info'].apply(extract_country_code_from_patents_info)
df_germany = df_publication[df_publication['country_code'] == 'DE'].copy()

# Optimized date parsing function
def parse_date_robust(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NaT
    cleaned_date_str = date_str.replace('dated ', '').replace('the ', '').strip()
    formats_to_try = [
        '%d %B %Y', '%B %d, %Y', '%B %dth, %Y', '%dth %B %Y', '%Y-%m-%d',
        '%Y, %B %d', '%Y, %B %dth', '%b %d, %Y', '%d %b %Y', '%b %dth, %Y',
        '%d %b, %Y', '%Y %b %d', '%Y %B %d' # Added more formats for better parsing
    ]
    for fmt in formats_to_try:
        try:
            return pd.to_datetime(cleaned_date_str, format=fmt, errors='raise')
        except ValueError:
            continue
    return pd.NaT

df_germany['grant_date_parsed'] = df_germany['grant_date'].apply(parse_date_robust)
df_germany['filing_date_parsed'] = df_germany['filing_date'].apply(parse_date_robust)

# Filter for grant date in H2 2019
df_filtered = df_germany[
    (df_germany['grant_date_parsed'].dt.year == 2019) &
    (df_germany['grant_date_parsed'].dt.month.isin([7, 8, 9, 10, 11, 12]))
].copy()

# Extract CPC level 4 codes
def extract_cpc_level4(cpc_json):
    cpc_codes = []
    if pd.isna(cpc_json) or not isinstance(cpc_json, str):
        return []
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code and len(code) >= 7 and code[4] == '/': # Ensure it's a level 4 code, e.g., A01B1/00
                cpc_codes.append(code[:7])
    except (json.JSONDecodeError, TypeError):
        pass
    return list(set(cpc_codes))

df_filtered['cpc_level4'] = df_filtered['cpc'].apply(extract_cpc_level4)
df_filtered['filing_year'] = df_filtered['filing_date_parsed'].dt.year

# Explode and count filings per CPC level 4 and year
df_exploded = df_filtered.explode('cpc_level4').dropna(subset=['cpc_level4', 'filing_year'])
cpc_filing_counts = df_exploded.groupby(['cpc_level4', 'filing_year']).size().reset_index(name='filing_count')

# Calculate EMA
# For smoothing factor alpha=0.1, span = (2/alpha) - 1 = (2/0.1) - 1 = 19.
# Calculate EMA for each CPC group and then merge back.
ema_results = cpc_filing_counts.sort_values(by=['cpc_level4', 'filing_year']) \
                               .groupby('cpc_level4')['filing_count'] \
                               .transform(lambda x: x.ewm(span=19, adjust=False).mean())
cpc_filing_counts['ema'] = ema_results

# Find the best year for each CPC group based on the highest EMA
best_cpc_ema = cpc_filing_counts.loc[cpc_filing_counts.groupby('cpc_level4')['ema'].idxmax()]

# Select relevant columns for the final output
result_df_for_cpc_lookup = best_cpc_ema[['cpc_level4', 'filing_year', 'ema']]

# Get unique CPC level 4 codes to query CPCDefinition_database
cpc_symbols_to_query = result_df_for_cpc_lookup['cpc_level4'].unique().tolist()

print("__RESULT__:")
print(json.dumps(cpc_symbols_to_query))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json', 'var_function-call-7372648690842701050': 'file_storage/function-call-7372648690842701050.json', 'var_function-call-1535884070543777370': 'file_storage/function-call-1535884070543777370.json', 'var_function-call-8059124700018447838': [], 'var_function-call-12114976582929715329': 'file_storage/function-call-12114976582929715329.json', 'var_function-call-10464469190898668953': [], 'var_function-call-17032710537122925813': 'file_storage/function-call-17032710537122925813.json', 'var_function-call-17420446429769094488': 'file_storage/function-call-17420446429769094488.json'}

exec(code, env_args)
