code = """import pandas as pd
import json
import re

# Load publication data
publication_records = pd.read_json(locals()['var_function-call-15691569362807671881'])

# Optimized Date parsing function
def parse_date_optimized(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    # Attempt to clean common date string artifacts once, if present and problematic
    date_str_cleaned = date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('the ', '').replace('dated ', '').replace('issued ', '').strip()

    # Prioritize specific formats if known to be common
    date_formats = [
        '%B %d, %Y', '%d %B %Y', '%b %d, %Y', '%d %b %Y',
        '%Y-%m-%d', '%m/%d/%Y', '%Y', # Common and numeric formats
    ]
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str_cleaned, format=fmt)
        except ValueError:
            continue
    return pd.NaT

publication_records['parsed_grant_date'] = publication_records['grant_date'].apply(parse_date_optimized)
publication_records['parsed_filing_date'] = publication_records['filing_date'].apply(parse_date_optimized)

# Filter for patents granted in the second half of 2019
filtered_df = publication_records[
    (publication_records['parsed_grant_date'].dt.year == 2019) &
    (publication_records['parsed_grant_date'].dt.month >= 7)
].copy()

# Extract country code and filter for Germany
def extract_country_code(patents_info):
    if isinstance(patents_info, str):
        match_id = re.search(r'\(ID ([A-Z]{2})-', patents_info)
        if match_id:
            return match_id.group(1)
        match_pub = re.search(r'publication number ([A-Z]{2})-', patents_info)
        if match_pub:
            return match_pub.group(1)
    return None

filtered_df['country_code'] = filtered_df['Patents_info'].apply(extract_country_code)
filtered_df = filtered_df[filtered_df['country_code'] == 'DE']

# Efficient CPC Extraction and Flattening
# Only proceed if filtered_df is not empty to avoid errors on empty dataframes
if not filtered_df.empty:
    filtered_df['cpc_parsed'] = filtered_df['cpc'].apply(lambda x: json.loads(x) if isinstance(x, str) else [])
    
    # Explode the list of CPC dictionaries into separate rows
    exploded_cpc_df = filtered_df.explode('cpc_parsed')
    
    # Extract CPC code and filing year
    exploded_cpc_df['cpc_group_level_4'] = exploded_cpc_df['cpc_parsed'].apply(lambda x: x['code'][:4] if isinstance(x, dict) and 'code' in x and len(x['code']) >= 4 else None)
    exploded_cpc_df['filing_year'] = exploded_cpc_df['parsed_filing_date'].dt.year
    
    # Drop rows where CPC code or filing year couldn't be extracted
    cpc_filings_df = exploded_cpc_df.dropna(subset=['cpc_group_level_4', 'filing_year'])[['cpc_group_level_4', 'filing_year']]
    cpc_filings_df['filing_year'] = cpc_filings_df['filing_year'].astype(int)
else:
    cpc_filings_df = pd.DataFrame(columns=['cpc_group_level_4', 'filing_year'])


# Calculate patent counts per CPC group and filing year
patent_counts = cpc_filings_df.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='patent_count')

# Calculate Exponential Moving Average (EMA)
ema_results_list = []
alpha = 0.1

if not patent_counts.empty:
    # Sort by CPC group and filing year for correct EMA calculation
    patent_counts = patent_counts.sort_values(by=['cpc_group_level_4', 'filing_year'])
    
    # Calculate EMA grouped by cpc_group_level_4
    # This operation applies EMA within each group, and `transform` ensures the output matches the original index for easy merging
    patent_counts['ema'] = patent_counts.groupby('cpc_group_level_4')['patent_count'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

    # Find the row with the highest EMA for each CPC group
    idx = patent_counts.groupby(['cpc_group_level_4'])['ema'].idxmax()
    ema_df = patent_counts.loc[idx]
    
    ema_df = ema_df[['cpc_group_level_4', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year', 'ema': 'highest_ema'})
else:
    ema_df = pd.DataFrame(columns=['cpc_group_level_4', 'best_year', 'highest_ema'])


# Load CPC definitions
cpc_definitions = pd.read_json(locals()['var_function-call-6758242112758697461'])

# Merge with CPC definitions to get full titles
if not ema_df.empty:
    final_results = pd.merge(ema_df, cpc_definitions, left_on='cpc_group_level_4', right_on='symbol', how='left')
    final_results = final_results[['titleFull', 'cpc_group_level_4', 'best_year']]
    final_results.rename(columns={'cpc_group_level_4': 'CPC Group Code'}, inplace=True)
else:
    final_results = pd.DataFrame(columns=['titleFull', 'CPC Group Code', 'best_year'])

print('__RESULT__:')
print(final_results.to_json(orient='records'))"""

env_args = {'var_function-call-8293969278468813104': 'file_storage/function-call-8293969278468813104.json', 'var_function-call-6758242112758697461': 'file_storage/function-call-6758242112758697461.json', 'var_function-call-15691569362807671881': 'file_storage/function-call-15691569362807671881.json'}

exec(code, env_args)
