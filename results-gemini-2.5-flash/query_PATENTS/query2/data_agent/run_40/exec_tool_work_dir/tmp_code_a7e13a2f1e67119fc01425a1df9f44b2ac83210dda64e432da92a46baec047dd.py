code = """import pandas as pd
import json
import re

# Load publication data
publication_records = pd.read_json(locals()['var_function-call-15691569362807671881'])

# Optimized Date parsing function
def parse_date_optimized(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_str_cleaned = date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('the ', '').replace('dated ', '').replace('issued ', '').strip()

    date_formats = [
        '%B %d, %Y', '%d %B %Y', '%b %d, %Y', '%d %b %Y',
        '%Y-%m-%d', '%m/%d/%Y', '%Y', 
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

# Optimized CPC Extraction and Filing Year Collection
cpc_filings_data = []
for _, row in filtered_df.iterrows():
    if pd.notna(row['cpc']) and isinstance(row['cpc'], str) and pd.notna(row['parsed_filing_date']):
        try:
            cpc_list = json.loads(row['cpc'])
            for cpc_item in cpc_list:
                code = cpc_item.get('code')
                if code and len(code) >= 4:
                    cpc_group_level_4 = code[:4]
                    filing_year = row['parsed_filing_date'].year
                    cpc_filings_data.append((cpc_group_level_4, filing_year))
        except json.JSONDecodeError:
            continue

cpc_filings_df = pd.DataFrame(cpc_filings_data, columns=['cpc_group_level_4', 'filing_year'])

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

env_args = {'var_function-call-8293969278468813104': 'file_storage/function-call-8293969278468813104.json', 'var_function-call-6758242112758697461': 'file_storage/function-call-6758242112758697461.json', 'var_function-call-15691569362807671881': 'file_storage/function-call-15691569362807671881.json'}

exec(code, env_args)
