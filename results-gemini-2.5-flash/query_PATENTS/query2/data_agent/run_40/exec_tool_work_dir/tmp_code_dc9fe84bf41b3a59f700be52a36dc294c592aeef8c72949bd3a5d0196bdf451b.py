code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-8293969278468813104'])

def parse_date(date_str):
    if not isinstance(date_str, str):
        return None
    try:
        date_str = date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('dated ', '').replace('the ', '')
        return pd.to_datetime(date_str, format='%B %d, %Y', errors='coerce')
    except ValueError:
        try:
            return pd.to_datetime(date_str, format='%d %B %Y', errors='coerce')
        except ValueError:
            try:
                return pd.to_datetime(date_str, format='%b %d, %Y', errors='coerce')
            except ValueError:
                try:
                    return pd.to_datetime(date_str, format='%d %b %Y', errors='coerce')
                except ValueError:
                    try:
                        return pd.to_datetime(date_str, format='%Y', errors='coerce')
                    except ValueError:
                        return None

df['parsed_grant_date'] = df['grant_date'].apply(parse_date)
df['parsed_filing_date'] = df['filing_date'].apply(parse_date)

df = df[df['parsed_grant_date'].dt.year == 2019]
df = df[df['parsed_grant_date'].dt.month.isin([7, 8, 9, 10, 11, 12])]

def extract_country_code(patents_info):
    if isinstance(patents_info, str):
        import re
        match = re.search(r'\(ID [A-Z]{2}-', patents_info)
        if match:
            return match.group(0)[4:6]
        match = re.search(r'publication number [A-Z]{2}-', patents_info)
        if match:
            return match.group(0)[19:21]
    return None

df['country_code'] = df['Patents_info'].apply(extract_country_code)
df = df[df['country_code'] == 'DE']

cpc_data = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_level_4 = code[:4]
                cpc_data.append({'cpc_group_level_4': cpc_group_level_4, 'filing_year': row['parsed_filing_date'].year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

patent_counts = cpc_df.groupby(['cpc_group_level_4', 'filing_year']).size().reset_index(name='patent_count')

ema_data = []
alpha = 0.1
for cpc_group in patent_counts['cpc_group_level_4'].unique():
    group_df = patent_counts[patent_counts['cpc_group_level_4'] == cpc_group].sort_values(by='filing_year')
    group_df['ema'] = group_df['patent_count'].ewm(alpha=alpha, adjust=False).mean()
    if not group_df.empty:
        best_year_row = group_df.loc[group_df['ema'].idxmax()]
        ema_data.append({'cpc_group_level_4': cpc_group, 'best_year': int(best_year_row['filing_year']), 'highest_ema': best_year_row['ema']})

ema_df = pd.DataFrame(ema_data)

print('__RESULT__:')
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-8293969278468813104': 'file_storage/function-call-8293969278468813104.json'}

exec(code, env_args)
