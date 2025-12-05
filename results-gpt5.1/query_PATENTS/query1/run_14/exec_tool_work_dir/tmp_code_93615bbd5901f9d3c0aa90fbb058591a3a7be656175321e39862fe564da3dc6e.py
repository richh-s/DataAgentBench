code = """import json, pandas as pd, re, datetime

# Load full publication data
file_path = var_call_qcYtQkV97j1uc2EQWvjIMQKN
with open(file_path, 'r') as f:
    pub_data = json.load(f)

# Convert to DataFrame
pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
month_map = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

years = []
for d in pub_df['publication_date'].astype(str):
    # Try patterns like 'Aug 3rd, 2021' or 'August 3rd, 2021'
    year = None
    m = re.search(r'(19|20)\d{2}', d)
    if m:
        year = int(m.group(0))
    years.append(year)

pub_df['year'] = years
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Keep only years up to 2022
pub_df = pub_df[pub_df['year'] <= 2022]

# Expand CPC JSON-like strings
codes = []
years_list = []
for _, row in pub_df.iterrows():
    y = row['year']
    cpc_raw = row['cpc']
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        # Try to fix common issues
        try:
            cpcs = json.loads(cpc_raw.replace("'", '"'))
        except Exception:
            continue
    for ent in cpcs:
        code = ent.get('code')
        if code:
            codes.append(code)
            years_list.append(y)

cpc_df = pd.DataFrame({'code': codes, 'year': years_list})

# Load level-5 CPC symbols
file_path2 = var_call_YDOWIXfGBQO0uO6gzuUGi3xH
with open(file_path2, 'r') as f:
    level5_data = json.load(f)
level5_set = set(d['symbol'] for d in level5_data)

# Filter to codes that are exactly level-5 symbols
cpc_df = cpc_df[cpc_df['code'].isin(level5_set)]

# Count filings per year per CPC code
counts = cpc_df.groupby(['code','year']).size().reset_index(name='count')

# For EMA we need continuous years per code
results = []
alpha = 0.2
for code, grp in counts.groupby('code'):
    grp = grp.sort_values('year')
    years_range = list(range(grp['year'].min(), grp['year'].max()+1))
    year_to_count = {r['year']: r['count'] for _, r in grp.iterrows()}
    ema = None
    for y in years_range:
        c = year_to_count.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha*c + (1-alpha)*ema
        results.append({'code': code, 'year': y, 'ema': ema})

ema_df = pd.DataFrame(results)

# For each code, find year with highest EMA
idx = ema_df.groupby('code')['ema'].idxmax()
best_df = ema_df.loc[idx].reset_index(drop=True)

# Keep only those whose best year is 2022
best_2022 = best_df[best_df['year'] == 2022]

codes_2022 = sorted(best_2022['code'].unique())

import json as _json
result = _json.dumps(codes_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_qcYtQkV97j1uc2EQWvjIMQKN': 'file_storage/call_qcYtQkV97j1uc2EQWvjIMQKN.json', 'var_call_YDOWIXfGBQO0uO6gzuUGi3xH': 'file_storage/call_YDOWIXfGBQO0uO6gzuUGi3xH.json', 'var_call_4juKV2Ji76izWvkTQb2Zf80M': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}]}

exec(code, env_args)
