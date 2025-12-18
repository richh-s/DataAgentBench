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
    # Looking for 'ID DE-' or 'In DE,'
    match_id = re.search(r'ID\s+DE-', patent_info)
    match_in = re.search(r'In\s+DE,', patent_info)
    if match_id or match_in:
        return 'DE'
    return None

with open(locals()['var_function-call-5068727344322754251'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Apply date parsing and country code extraction first
df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)
df['country_code'] = df['Patents_info'].apply(extract_country_code_strict)

# Filter for patents granted in the second half of 2019 in Germany
df_germany_filtered = df[(df['grant_date'].dt.year == 2019) & 
                         (df['grant_date'].dt.month >= 7) & 
                         (df['country_code'] == 'DE')].copy()

# Process CPC codes only for the filtered DataFrame
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

# Calculate filings per CPC group per year
filings_by_cpc_year = cpc_df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.1
ema_calculated_df = filings_by_cpc_year.sort_values(by=['cpc_group_4', 'filing_year'])
ema_calculated_df['ema'] = ema_calculated_df.groupby('cpc_group_4')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the best year (highest EMA) for each CPC group
best_ema_for_cpc = ema_calculated_df.loc[ema_calculated_df.groupby('cpc_group_4')['ema'].idxmax()]

final_ema_results = best_ema_for_cpc[['cpc_group_4', 'filing_year']].rename(columns={'filing_year': 'best_year'})

print("__RESULT__:")
print(final_ema_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json'}

exec(code, env_args)
