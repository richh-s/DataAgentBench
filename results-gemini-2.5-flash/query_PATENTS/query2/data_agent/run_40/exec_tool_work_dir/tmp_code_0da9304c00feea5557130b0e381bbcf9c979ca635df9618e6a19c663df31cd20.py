code = """import pandas as pd
import json
import re

# Load publication data
publication_records = pd.read_json(locals()['var_function-call-14779514846413808933'])

# Streamlined Date parsing function using simpler to_datetime with errors='coerce'
def parse_date_simple(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_str_cleaned = date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('the ', '').replace('dated ', '').replace('issued ', '').strip()
    return pd.to_datetime(date_str_cleaned, errors='coerce')

publication_records['parsed_grant_date'] = publication_records['grant_date'].apply(parse_date_simple)
publication_records['parsed_filing_date'] = publication_records['filing_date'].apply(parse_date_simple)

# Filter for patents granted in the second half of 2019
filtered_df = publication_records[
    (publication_records['parsed_grant_date'].dt.year == 2019) &
    (publication_records['parsed_grant_date'].dt.month >= 7)
].copy()

# Extract country code and filter for Germany
def extract_country_code_optimized(patents_info):
    if isinstance(patents_info, str):
        match = re.search(r'(?:ID|number) ([A-Z]{2})-', patents_info)
        if match:
            return match.group(1)
    return None

filtered_df['country_code'] = filtered_df['Patents_info'].apply(extract_country_code_optimized)
filtered_df = filtered_df[filtered_df['country_code'] == 'DE']

# Optimized CPC Extraction and Filing Year Collection
# Only proceed if filtered_df is not empty
if not filtered_df.empty:
    # Apply json.loads only to non-NaN string values of 'cpc' and handle errors
    # Using list comprehension for efficiency over apply for json.loads
    parsed_cpc_lists = [json.loads(cpc_str) if isinstance(cpc_str, str) else [] for cpc_str in filtered_df['cpc']]
    filtered_df['cpc_parsed'] = parsed_cpc_lists
    
    # Explode the list of dictionaries and extract 'code' directly
    exploded_cpc_df = filtered_df.explode('cpc_parsed')
    
    # Filter out rows where cpc_parsed is not a dictionary or 'code' is missing/invalid
    exploded_cpc_df = exploded_cpc_df[exploded_cpc_df['cpc_parsed'].apply(lambda x: isinstance(x, dict) and x.get('code') and len(x['code']) >= 4)]

    # Extract CPC group level 4 and filing year using vectorized operations
    exploded_cpc_df['cpc_group_level_4'] = exploded_cpc_df['cpc_parsed'].apply(lambda x: x['code'][:4])
    exploded_cpc_df['filing_year'] = exploded_cpc_df['parsed_filing_date'].dt.year
    
    cpc_filings_df = exploded_cpc_df.dropna(subset=['cpc_group_level_4', 'filing_year'])[['cpc_group_level_4', 'filing_year']] # Select relevant columns
    cpc_filings_df['filing_year'] = cpc_filings_df['filing_year'].astype(int)
else:
    cpc_filings_df = pd.DataFrame(columns=['cpc_group_level_4', 'filing_year'])


# Proceed only if cpc_filings_df is not empty
if not cpc_filings_df.empty:
    # Calculate patent counts per CPC group and filing year
    patent_counts = cpc_filings_df.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='patent_count')

    # Calculate Exponential Moving Average (EMA)
    patent_counts = patent_counts.sort_values(by=['cpc_group_level_4', 'filing_year'])

    patent_counts['ema'] = patent_counts.groupby('cpc_group_level_4')['patent_count'].transform(
        lambda x: x.ewm(alpha=0.1, adjust=False).mean()
    )

    idx = patent_counts.groupby(['cpc_group_level_4'])['ema'].idxmax()
    ema_df = patent_counts.loc[idx]

    ema_df = ema_df[['cpc_group_level_4', 'filing_year', 'ema']].rename(
        columns={'filing_year': 'best_year', 'ema': 'highest_ema'}
    )
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

env_args = {'var_function-call-8293969278468813104': 'file_storage/function-call-8293969278468813104.json', 'var_function-call-6758242112758697461': 'file_storage/function-call-6758242112758697461.json', 'var_function-call-15691569362807671881': 'file_storage/function-call-15691569362807671881.json', 'var_function-call-14779514846413808933': 'file_storage/function-call-14779514846413808933.json'}

exec(code, env_args)
