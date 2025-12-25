code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-1535884070543777370'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

# Filter for Germany first to reduce dataframe size
df_germany = df_publication[df_publication['Patents_info'].str.contains('Germany', na=False)].copy()

# Optimized date parsing
def parse_date_robust(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NaT
    # Clean string
    cleaned_date_str = date_str.replace('dated ', '').replace('the ', '')
    formats_to_try = [
        '%d %B %Y', '%B %d, %Y', '%B %dth, %Y', '%dth %B %Y', '%Y-%m-%d'
    ]
    for fmt in formats_to_try:
        try:
            return pd.to_datetime(cleaned_date_str, format=fmt, errors='raise')
        except ValueError:
            continue
    return pd.NaT # Return NaT if no format matches

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
            if code and len(code) >= 7 and code[4] == '/':
                cpc_codes.append(code[:7])
    except (json.JSONDecodeError, TypeError):
        pass
    return list(set(cpc_codes))

df_filtered['cpc_level4'] = df_filtered['cpc'].apply(extract_cpc_level4)
df_filtered['filing_year'] = df_filtered['filing_date_parsed'].dt.year

# Explode and count
df_exploded = df_filtered.explode('cpc_level4').dropna(subset=['cpc_level4', 'filing_year'])
cpc_filing_counts = df_exploded.groupby(['cpc_level4', 'filing_year']).size().reset_index(name='filing_count')

print("__RESULT__:")
print(cpc_filing_counts.to_json(orient="records"))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json', 'var_function-call-7372648690842701050': 'file_storage/function-call-7372648690842701050.json', 'var_function-call-1535884070543777370': 'file_storage/function-call-1535884070543777370.json'}

exec(code, env_args)
