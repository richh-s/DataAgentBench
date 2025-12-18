code = """import pandas as pd
import json
import re

# Load publication data
publication_records = pd.read_json(locals()['var_function-call-8293969278468813104'])

# Date parsing function - optimized to handle more formats and return datetime directly
def parse_date_optimized(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_formats = [
        '%B %d, %Y', '%d %B %Y', '%b %d, %Y', '%d %b %Y',
        '%Y', '%B %dth, %Y', '%B %dnd, %Y', '%B %drd, %Y', '%B %dst, %Y',
        '%dth %B %Y', '%dnd %B %Y', '%drd %B %Y', '%dst %B %Y',
        'dated %B %d, %Y', 'dated %d %B %Y', 'dated %b %d, %Y', 'dated %d %b %Y',
        'dated %dth %B %Y', 'dated %dnd %B %Y', 'dated %drd %B %Y', 'dated %dst %B %Y',
        '%B the %dth, %Y', '%B the %dnd, %Y', '%B the %drd, %Y', '%B the %dst, %Y',
        '%dth of %B, %Y', '%dnd of %B, %Y', '%drd of %B, %Y', '%dst of %B, %Y',
        'dated %Y', 'issued %B %d, %Y', 'issued %d %B %Y', 'dated %m/%d/%Y', 'dated %Y-%m-%d'
    ]
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('the ', '').replace('dated ', '').strip(), format=fmt)
        except ValueError:
            continue
    return pd.NaT

publication_records['parsed_grant_date'] = publication_records['grant_date'].apply(parse_date_optimized)
publication_records['parsed_filing_date'] = publication_records['filing_date'].apply(parse_date_optimized)

# Filter for patents granted in the second half of 2019
filtered_df = publication_records[
    (publication_records['parsed_grant_date'].dt.year == 2019) &
    (publication_records['parsed_grant_date'].dt.month >= 7)
].copy() # Using .copy() to avoid SettingWithCopyWarning

# Extract country code and filter for Germany
def extract_country_code(patents_info):
    if isinstance(patents_info, str):
        match = re.search(r'\(ID ([A-Z]{2})-', patents_info)
        if match:
            return match.group(1)
        match = re.search(r'publication number ([A-Z]{2})-', patents_info)
        if match:
            return match.group(1)
    return None

filtered_df['country_code'] = filtered_df['Patents_info'].apply(extract_country_code)
filtered_df = filtered_df[filtered_df['country_code'] == 'DE']

# Extract CPC group level 4 and filing year
cpc_data = []
for _, row in filtered_df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_level_4 = code[:4]
                if pd.notna(row['parsed_filing_date']):
                    cpc_data.append({'cpc_group_level_4': cpc_group_level_4, 'filing_year': row['parsed_filing_date'].year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(cpc_data)

# Calculate patent counts per CPC group and filing year
patent_counts = cpc_filings_df.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='patent_count')

# Calculate Exponential Moving Average (EMA)
ema_results = []
alpha = 0.1
for cpc_group in patent_counts['cpc_group_level_4'].unique():
    group_df = patent_counts[patent_counts['cpc_group_level_4'] == cpc_group].sort_values(by='filing_year')
    if not group_df.empty:
        group_df['ema'] = group_df['patent_count'].ewm(alpha=alpha, adjust=False).mean()
        best_year_row = group_df.loc[group_df['ema'].idxmax()]
        ema_results.append({
            'cpc_group_level_4': cpc_group,
            'best_year': int(best_year_row['filing_year']),
            'highest_ema': best_year_row['ema']
        })

ema_df = pd.DataFrame(ema_results)

# Load CPC definitions
cpc_definitions = pd.read_json(locals()['var_function-call-6758242112758697461'])

# Merge with CPC definitions to get full titles
final_results = pd.merge(ema_df, cpc_definitions, left_on='cpc_group_level_4', right_on='symbol', how='left')
final_results = final_results[['titleFull', 'cpc_group_level_4', 'best_year', 'highest_ema']]
final_results.rename(columns={'cpc_group_level_4': 'CPC Group Code'}, inplace=True)

print('__RESULT__:')
print(final_results.to_json(orient='records'))"""

env_args = {'var_function-call-8293969278468813104': 'file_storage/function-call-8293969278468813104.json', 'var_function-call-6758242112758697461': 'file_storage/function-call-6758242112758697461.json'}

exec(code, env_args)
