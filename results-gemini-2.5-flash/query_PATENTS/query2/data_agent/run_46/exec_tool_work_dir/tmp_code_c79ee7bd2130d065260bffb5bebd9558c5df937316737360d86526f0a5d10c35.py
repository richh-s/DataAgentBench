code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-1535884070543777370'], 'r') as f:
    publication_data = json.load(f)

df_publication = pd.DataFrame(publication_data)

def extract_country_code(patents_info):
    if pd.isna(patents_info):
        return None
    match = re.search(r'\(ID [A-Z]{2}-\d{12}-A\)', patents_info) # for US-201916293577-A format
    if match:
        return match.group(0)[4:6]
    match = re.search(r'application no. ([A-Z]{2})-\d{12}-A', patents_info) # for application no. US-201916355911-A
    if match:
        return match.group(1)
    match = re.search(r'publication no. ([A-Z]{2})-\d{10}-B\d', patents_info) # for publication number US-11081687-B2
    if match:
        return match.group(1)
    match = re.search(r'In ([A-Z]{2}), the application', patents_info)
    if match:
        return match.group(1)
    match = re.search(r'Patent application \(ID ([A-Z]{2})-\d{12}-A\)', patents_info)
    if match:
        return match.group(1)
    return None

df_publication['country_code'] = df_publication['Patents_info'].apply(extract_country_code)
df_germany = df_publication[df_publication['country_code'] == 'DE'].copy()


def parse_date_robust(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NaT
    cleaned_date_str = date_str.replace('dated ', '').replace('the ', '')
    try:
        return pd.to_datetime(cleaned_date_str, infer_datetime_format=True, errors='coerce')
    except Exception:
        return pd.NaT

df_germany['grant_date_parsed'] = df_germany['grant_date'].apply(parse_date_robust)
df_germany['filing_date_parsed'] = df_germany['filing_date'].apply(parse_date_robust)

df_filtered = df_germany[
    (df_germany['grant_date_parsed'].dt.year == 2019) &
    (df_germany['grant_date_parsed'].dt.month.isin([7, 8, 9, 10, 11, 12]))
].copy()

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

df_exploded = df_filtered.explode('cpc_level4').dropna(subset=['cpc_level4', 'filing_year'])
cpc_filing_counts = df_exploded.groupby(['cpc_level4', 'filing_year']).size().reset_index(name='filing_count')

# Calculate EMA
def calculate_ema(group):
    return group.sort_values(by='filing_year')['filing_count'].ewm(span=19, adjust=False).mean()

cpc_filing_counts['ema'] = cpc_filing_counts.groupby('cpc_level4', group_keys=False).apply(calculate_ema)

best_cpc_ema = cpc_filing_counts.loc[cpc_filing_counts.groupby('cpc_level4')['ema'].idxmax()]

result_df = best_cpc_ema[['cpc_level4', 'filing_year', 'ema']]

print("__RESULT__:")
print(result_df.to_json(orient="records"))"""

env_args = {'var_function-call-9977173352170465390': 'file_storage/function-call-9977173352170465390.json', 'var_function-call-7372648690842701050': 'file_storage/function-call-7372648690842701050.json', 'var_function-call-1535884070543777370': 'file_storage/function-call-1535884070543777370.json', 'var_function-call-8059124700018447838': [], 'var_function-call-12114976582929715329': 'file_storage/function-call-12114976582929715329.json'}

exec(code, env_args)
