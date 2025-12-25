code = """import json, pandas as pd, re

# Load full publication data
file_path = var_call_qcYtQkV97j1uc2EQWvjIMQKN
with open(file_path, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year
years = []
for d in pub_df['publication_date'].astype(str):
    m = re.search(r'(19|20)\d{2}', d)
    years.append(int(m.group(0)) if m else None)
pub_df['year'] = years
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)
pub_df = pub_df[pub_df['year'] <= 2022]

codes = []
years_list = []
for _, row in pub_df.iterrows():
    y = row['year']
    cpc_raw = row['cpc']
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        try:
            cpcs = json.loads(cpc_raw.replace("'", '"'))
        except Exception:
            continue
    if isinstance(cpcs, dict):
        cpcs_list = cpcs.get('cpc', [])
    else:
        cpcs_list = cpcs
    for ent in cpcs_list:
        if not isinstance(ent, dict):
            continue
        code = ent.get('code') or ent.get('symbol') or ent.get('cpc')
        if code:
            codes.append(code)
            years_list.append(y)

cpc_df = pd.DataFrame({'code': codes, 'year': years_list})

# Load level-5 CPC symbols
file_path2 = var_call_YDOWIXfGBQO0uO6gzuUGi3xH
with open(file_path2, 'r') as f:
    level5_data = json.load(f)
level5_set = set(d['symbol'] for d in level5_data)

cpc_df = cpc_df[cpc_df['code'].isin(level5_set)]

counts = cpc_df.groupby(['code','year']).size().reset_index(name='count')

results = []
alpha = 0.2
for code, grp in counts.groupby('code'):
    grp = grp.sort_values('year')
    years_range = list(range(grp['year'].min(), grp['year'].max()+1))
    year_to_count = {int(r['year']): int(r['count']) for _, r in grp.iterrows()}
    ema = None
    for y in years_range:
        c = year_to_count.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha*c + (1-alpha)*ema
        results.append({'code': code, 'year': y, 'ema': ema})

ema_df = pd.DataFrame(results)

if ema_df.empty:
    result = json.dumps([])
else:
    idx = ema_df.groupby('code')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)
    best_2022 = best_df[best_df['year'] == 2022]
    codes_2022 = sorted(best_2022['code'].unique())
    result = json.dumps(codes_2022)

print('__RESULT__:')
print(result)"""

env_args = {'var_call_qcYtQkV97j1uc2EQWvjIMQKN': 'file_storage/call_qcYtQkV97j1uc2EQWvjIMQKN.json', 'var_call_YDOWIXfGBQO0uO6gzuUGi3xH': 'file_storage/call_YDOWIXfGBQO0uO6gzuUGi3xH.json', 'var_call_4juKV2Ji76izWvkTQb2Zf80M': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}]}

exec(code, env_args)
