code = """import pandas as pd
import json

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        try:
            return pd.to_datetime(date_str.replace('dated ', ''), errors='coerce', dayfirst=False)
        except:
            try:
                return pd.to_datetime(date_str.replace('the ', '').replace('th,', '').replace('st,', '').replace('nd,', '').replace('rd,', ''), errors='coerce', dayfirst=False)
            except:
                return pd.NaT


def extract_country_code(patent_info):
    parts = patent_info.split(' ')
    if 'ID' in parts:
        try:
            idx = parts.index('ID')
            country_code = parts[idx + 1].split('-')[0]
            return country_code
        except (IndexError, ValueError):
            pass
    elif 'In' in parts and len(parts) > 1 and len(parts[1]) == 2 and parts[1].isupper():
        return parts[1].replace(',', '')
    return None


with open(locals()['var_function-call-297126640787404012'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)

df = df[(df['grant_date'].dt.year == 2019) & (df['grant_date'].dt.month >= 7)]

df['country_code'] = df['Patents_info'].apply(extract_country_code)
df_germany = df[df['country_code'] == 'DE']

all_cpc_codes = []
for index, row in df_germany.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date'].year
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_4 = code[:4]
                all_cpc_codes.append({'cpc_group_4': cpc_group_4, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(all_cpc_codes)

filings_by_cpc_year = cpc_df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

ema_results = []
smoothing_factor = 0.1

for cpc_group in filings_by_cpc_year['cpc_group_4'].unique():
    group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group_4'] == cpc_group].sort_values(by='filing_year')
    
    if not group_df.empty:
        ema = [0.0] * len(group_df)
        ema[0] = group_df['filings'].iloc[0]

        for i in range(1, len(group_df)):
            ema[i] = (group_df['filings'].iloc[i] * smoothing_factor) + (ema[i-1] * (1 - smoothing_factor))
        
        best_year_idx = pd.Series(ema).idxmax()
        best_year = group_df['filing_year'].iloc[best_year_idx]
        max_ema = ema[best_year_idx]
        ema_results.append({'cpc_group_4': cpc_group, 'best_year': best_year, 'max_ema': max_ema})

ema_df = pd.DataFrame(ema_results)

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json'}

exec(code, env_args)
