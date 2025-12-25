code = """import pandas as pd
import json
import re

def parse_date_optimized(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    date_str = date_str.replace('dated ', '').replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
    date_formats = [
        '%d %B %Y',
        '%B %d, %Y',
        '%Y on %B %d',
        '%d %b %Y',
        '%b %d, %Y',
        '%Y-%m-%d',
        '%d-%m-%Y',
        '%Y-%m-%d %H:%M:%S',
        '%d/%m/%Y'
    ]
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str, format=fmt, errors='raise')
        except ValueError:
            continue
    return pd.to_datetime(date_str, errors='coerce')

def extract_country_code_from_patents_info(patent_info):
    if isinstance(patent_info, str):
        match = re.search(r'\b(DE)\b', patent_info)
        if match:
            return match.group(1)
    return None

# Load the JSON data from the file
with open(locals()['var_function-call-18001159190617317211'], 'r') as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)

# Apply country code extraction
df['country_code'] = df['Patents_info'].apply(extract_country_code_from_patents_info)

# Filter for German patents
df_de = df[df['country_code'] == 'DE'].copy()

# Convert date columns for filtered DataFrame
df_de['grant_date_parsed'] = df_de['grant_date'].apply(parse_date_optimized)
df_de['filing_date_parsed'] = df_de['filing_date'].apply(parse_date_optimized)

# Filter for patents granted in the second half of 2019
start_date = pd.to_datetime('2019-07-01')
end_date = pd.to_datetime('2019-12-31')

filtered_df = df_de[(df_de['grant_date_parsed'] >= start_date) &
                    (df_de['grant_date_parsed'] <= end_date)].copy()

# Extract CPC level 4 codes and filing year
cpc_data_list = []
for _, row in filtered_df.iterrows():
    if pd.notna(row['cpc']):
        try:
            cpc_entries = json.loads(row['cpc'])
            for entry in cpc_entries:
                code = entry.get('code')
                if code and len(code) >= 4:
                    cpc_group_level4 = code[:4]
                    if pd.notna(row['filing_date_parsed']):
                        filing_year = row['filing_date_parsed'].year
                        cpc_data_list.append({'cpc_group_level4': cpc_group_level4, 'filing_year': filing_year})
        except json.JSONDecodeError:
            continue

cpc_df = pd.DataFrame(cpc_data_list)

ema_df = pd.DataFrame(columns=['cpc_group_level4', 'best_year', 'highest_ema'])

if not cpc_df.empty:
    # Calculate annual filing counts for each CPC group
    filings_by_cpc_year = cpc_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='filings')

    # Calculate EMA
    smoothing_factor = 0.1
    ema_results = []

    for cpc_group in filings_by_cpc_year['cpc_group_level4'].unique():
        group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group_level4'] == cpc_group].sort_values(by='filing_year')

        if not group_df.empty:
            min_year = int(group_df['filing_year'].min())
            max_year = int(group_df['filing_year'].max())
            all_years_range = pd.Series(range(min_year, max_year + 1), name='filing_year')

            group_df_reindexed = pd.merge(all_years_range, group_df, on='filing_year', how='left').fillna(0)
            group_df_reindexed['filings'] = group_df_reindexed['filings'].astype(int)

            group_df_reindexed['ema'] = group_df_reindexed['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
            if not group_df_reindexed.empty:
                best_year_row = group_df_reindexed.loc[group_df_reindexed['ema'].idxmax()]
                ema_results.append({
                    'cpc_group_level4': cpc_group,
                    'best_year': int(best_year_row['filing_year']),
                    'highest_ema': best_year_row['ema']
                })
    ema_df = pd.DataFrame(ema_results)

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-18001159190617317211': 'file_storage/function-call-18001159190617317211.json', 'var_function-call-8012184922050959362': [], 'var_function-call-13376446072317083405': 'file_storage/function-call-13376446072317083405.json', 'var_function-call-13873714782935837261': [], 'var_function-call-9883835784648554032': {'german_patents_found': 0}}

exec(code, env_args)
