code = """import pandas as pd
import json
import re

def parse_date(date_str):
    try:
        if 'dated ' in date_str:
            date_str = date_str.replace('dated ', '')
        date_str = re.sub(r'(st|nd|rd|th),', ',', date_str)
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        return pd.NaT

def extract_country_code_strict(patent_info):
    match_id = re.search(r'ID\s+DE-', patent_info)
    match_in = re.search(r'In\s+DE,', patent_info)
    if match_id or match_in:
        return 'DE'
    return None

with open(locals()['var_function-call-5068727344322754251'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)
df['country_code'] = df['Patents_info'].apply(extract_country_code_strict)

df_germany_filtered = df[(df['grant_date'].dt.year == 2019) & 
                         (df['grant_date'].dt.month >= 7) & 
                         (df['country_code'] == 'DE')].copy()

cpc_data = []
for index, row in df_germany_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date'].year
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if isinstance(code, str) and len(code) >= 4:
                cpc_group_4 = code[:4]
                cpc_data.append({'cpc_group_4': cpc_group_4, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

filings_by_cpc_year = cpc_df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

smoothing_factor = 0.1
ema_calculated_df = filings_by_cpc_year.sort_values(by=['cpc_group_4', 'filing_year'])
ema_calculated_df['ema'] = ema_calculated_df.groupby('cpc_group_4')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

best_ema_for_cpc = ema_calculated_df.loc[ema_calculated_df.groupby('cpc_group_4')['ema'].idxmax()]

final_ema_results = best_ema_for_cpc[['cpc_group_4', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year', 'ema': 'max_ema'})

print("__RESULT__:")
print(final_ema_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json'}

exec(code, env_args)
