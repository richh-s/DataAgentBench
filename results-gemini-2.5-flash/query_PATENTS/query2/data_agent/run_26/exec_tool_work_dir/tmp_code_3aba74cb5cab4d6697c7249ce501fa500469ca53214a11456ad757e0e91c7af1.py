code = """import pandas as pd
import json

with open(locals()['var_function-call-8434204621663570373'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Function to parse date strings
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    date_str = date_str.lower()
    for fmt in [
        '%dth %B %Y',
        '%d %B %Y',
        '%d %B, %Y',
        '%B %dth, %Y',
        '%B %d, %Y',
        '%d-%m-%Y',
        '%Y-%m-%d',
        '%d %b %Y',
        '%d %b, %Y',
        '%B the %dth, %Y',
        'dated %dth %B %Y',
        '%B the %d, %Y',
        '%d of %B, %Y',
        '%d of %B %Y',
        '%dnd %B %Y',
        '%dst %B %Y',
        '%brd %B %Y',
        '%d %B %Y',
        '%B %dst %Y',
        '%B %dth %Y',
        '%B %d %Y',
        '%B %dth, %Y',
        '%d-%m-%Y',
        '%d/%m/%Y',
        '%Y/%m/%d',
        '%Y-%m-%d',
    ]:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            pass
    return None

df['parsed_grant_date'] = df['grant_date'].apply(parse_date)
df['parsed_filing_date'] = df['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019
df_filtered_by_grant_date = df[
    (df['parsed_grant_date'] >= '2019-07-01') & (df['parsed_grant_date'] <= '2019-12-31')
].copy()

# Extract country code from Patents_info and filter for Germany
def extract_country_code(patents_info):
    if isinstance(patents_info, str):
        import re
        match = re.search(r'country_code\s*([A-Z]{2})', patents_info)
        if match:
            return match.group(1)
        match = re.search(r'\(ID ([A-Z]{2})-', patents_info)
        if match:
            return match.group(1)
        match = re.search(r'application no. ([A-Z]{2})-', patents_info)
        if match:
            return match.group(1)
    return None

df_filtered_by_grant_date['country_code'] = df_filtered_by_grant_date['Patents_info'].apply(extract_country_code)
df_germany = df_filtered_by_grant_date[df_filtered_by_grant_date['country_code'] == 'DE'].copy()

# Extract CPC codes and filing year
cpc_data = []
for _, row in df_germany.iterrows():
    if row['cpc']:
        try:
            cpc_list = json.loads(row['cpc'])
            for cpc_entry in cpc_list:
                if 'code' in cpc_entry and row['parsed_filing_date']:
                    cpc_data.append({
                        'cpc_code': cpc_entry['code'],
                        'filing_year': row['parsed_filing_date'].year
                    })
        except json.JSONDecodeError:
            continue

df_cpc = pd.DataFrame(cpc_data)

# Filter for CPC level 4 and extract group code
df_cpc['cpc_group_level_4'] = df_cpc['cpc_code'].apply(lambda x: x[:4] if isinstance(x, str) and len(x) >= 4 else None)
df_cpc = df_cpc.dropna(subset=['cpc_group_level_4'])

# Group by CPC group and filing year to count filings
filings_count = df_cpc.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA for each CPC group
smoothing_factor = 0.1
ema_results = []

for cpc_group in filings_count['cpc_group_level_4'].unique():
    group_df = filings_count[filings_count['cpc_group_level_4'] == cpc_group].sort_values(by='filing_year')
    if not group_df.empty:
        group_df['ema'] = group_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
        best_year_row = group_df.loc[group_df['ema'].idxmax()]
        ema_results.append({
            'cpc_group_level_4': cpc_group,
            'best_year': int(best_year_row['filing_year']),
            'highest_ema': best_year_row['ema']
        })

df_ema = pd.DataFrame(ema_results)

print("__RESULT__:")
print(df_ema.to_json(orient='records'))"""

env_args = {'var_function-call-7298381649333719606': ['publicationinfo'], 'var_function-call-8434204621663570373': 'file_storage/function-call-8434204621663570373.json'}

exec(code, env_args)
