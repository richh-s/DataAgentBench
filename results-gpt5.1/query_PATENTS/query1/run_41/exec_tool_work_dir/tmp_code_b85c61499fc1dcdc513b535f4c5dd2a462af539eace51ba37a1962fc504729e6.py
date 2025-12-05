code = """import json, pandas as pd, datetime

with open(var_call_QwjBdkCZO53ltRQj9ghilH7o, 'r') as f:
    pub_data = json.load(f)
with open(var_call_mOjt8h9ZYUNSviUHHPLcoBCH, 'r') as f:
    cpc_level5_data = json.load(f)

df_pub = pd.DataFrame(pub_data)
df_cpc5 = pd.DataFrame(cpc_level5_data)

import re

def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    m = re.search(r'(19|20)\d{2}', date_str)
    return int(m.group(0)) if m else None


df_pub['year'] = df_pub['publication_date'].apply(parse_year)
df_pub = df_pub.dropna(subset=['year'])
df_pub['year'] = df_pub['year'].astype(int)

codes_records = []
for _, row in df_pub.iterrows():
    year = row['year']
    cpc_str = row['cpc']
    if not isinstance(cpc_str, str):
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        try:
            cpc_list = json.loads(cpc_str.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for entry in cpc_list:
        if isinstance(entry, dict) and 'code' in entry:
            code = entry['code']
        elif isinstance(entry, str):
            code = entry
        else:
            continue
        codes_records.append({'year': year, 'code': code})

codes_df = pd.DataFrame(codes_records)

level5_symbols = set(df_cpc5['symbol'].astype(str).tolist())
level5_df = codes_df[codes_df['code'].isin(level5_symbols)].copy()

counts = level5_df.groupby(['code', 'year']).size().reset_index(name='count')

alpha = 0.2
ema_records = []
for code, grp in counts.groupby('code'):
    grp_sorted = grp.sort_values('year')
    ema = None
    for _, r in grp_sorted.iterrows():
        y = r['year']
        c = r['count']
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_records.append({'code': code, 'year': int(y), 'ema': float(ema)})

ema_df = pd.DataFrame(ema_records)

idx = ema_df.groupby('code')['ema'].idxmax()
best_df = ema_df.loc[idx].copy()

best_2022 = best_df[best_df['year'] == 2022]

result_codes = sorted(best_2022['code'].unique().tolist())

import json as _json
out = _json.dumps(result_codes)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_QwjBdkCZO53ltRQj9ghilH7o': 'file_storage/call_QwjBdkCZO53ltRQj9ghilH7o.json', 'var_call_mOjt8h9ZYUNSviUHHPLcoBCH': 'file_storage/call_mOjt8h9ZYUNSviUHHPLcoBCH.json'}

exec(code, env_args)
