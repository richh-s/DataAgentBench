code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-1535884070543777370'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

# Filter for Germany first to reduce dataframe size, based on the problem description.
df_germany = df_publication[df_publication['Patents_info'].str.contains('Germany', na=False)].copy()

# Optimized date parsing function
def parse_date_robust(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NaT
    cleaned_date_str = date_str.replace('dated ', '').replace('the ', '')
    formats_to_try = [
        '%d %B %Y', '%B %d, %Y', '%B %dth, %Y', '%dth %B %Y', '%Y-%m-%d',
        '%Y, %B %d', '%Y, %B %dth', '%b %d, %Y', '%d %b %Y', '%b %dth, %Y' # Added more formats
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

# Calculate EMA using transform to ensure alignment
cpc_filing_counts['ema'] = cpc_filing_counts.groupby('cpc_level4', group_keys=False) \
                                         .apply(lambda x: x.sort_values(by='filing_year')['filing_count'].ewm(span=19, adjust=False).mean())

# Find the best year for each CPC group based on the highest EMA
best_cpc_ema = cpc_filing_counts.loc[cpc_filing_counts.groupby('cpc_level4')['ema'].idxmax()]

# Select relevant columns for the final output
result_df_for_cpc_lookup = best_cpc_ema[['cpc_level4', 'filing_year', 'ema']]

print("__RESULT__:")
print(result_df_for_cpc_lookup.to_json(orient="records"))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json', 'var_function-call-7372648690842701050': 'file_storage/function-call-7372648690842701050.json', 'var_function-call-1535884070543777370': 'file_storage/function-call-1535884070543777370.json', 'var_function-call-8059124700018447838': [], 'var_function-call-12114976582929715329': 'file_storage/function-call-12114976582929715329.json'}

exec(code, env_args)
