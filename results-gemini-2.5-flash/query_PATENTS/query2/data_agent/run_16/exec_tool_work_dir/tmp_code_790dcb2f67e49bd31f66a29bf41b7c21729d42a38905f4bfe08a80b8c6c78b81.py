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

def extract_country_code(patent_info):
    match = re.search(r'(ID\s+([A-Z]{2})-\d+)|(In\s+([A-Z]{2}),)', patent_info)
    if match:
        return match.group(2) or match.group(4)
    return None

with open(locals()['var_function-call-297126640787404012'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)

df_filtered = df[(df['grant_date'].dt.year == 2019) & (df['grant_date'].dt.month >= 7)].copy()

df_filtered['country_code'] = df_filtered['Patents_info'].apply(extract_country_code)
df_germany = df_filtered[df_filtered['country_code'] == 'DE'].copy()

# Process CPC codes using pandas operations for efficiency
df_germany['cpc_list'] = df_germany['cpc'].apply(lambda x: json.loads(x) if pd.notna(x) else [])
exploded_cpc = df_germany.explode('cpc_list')

exploded_cpc['cpc_code'] = exploded_cpc['cpc_list'].apply(lambda x: x.get('code') if isinstance(x, dict) else None)
exploded_cpc['cpc_group_4'] = exploded_cpc['cpc_code'].apply(lambda x: x[:4] if isinstance(x, str) and len(x) >= 4 else None)
exploded_cpc['filing_year'] = exploded_cpc['filing_date'].dt.year

cpc_df_cleaned = exploded_cpc.dropna(subset=['cpc_group_4', 'filing_year'])

filings_by_cpc_year = cpc_df_cleaned.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

smoothing_factor = 0.1
ema_calculated_df = filings_by_cpc_year.sort_values(by=['cpc_group_4', 'filing_year'])
ema_calculated_df['ema'] = ema_calculated_df.groupby('cpc_group_4')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

best_ema_for_cpc = ema_calculated_df.loc[ema_calculated_df.groupby('cpc_group_4')['ema'].idxmax()]

final_ema_results = best_ema_for_cpc[['cpc_group_4', 'filing_year']].rename(columns={'filing_year': 'best_year'})

print("__RESULT__:")
print(final_ema_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json'}

exec(code, env_args)
