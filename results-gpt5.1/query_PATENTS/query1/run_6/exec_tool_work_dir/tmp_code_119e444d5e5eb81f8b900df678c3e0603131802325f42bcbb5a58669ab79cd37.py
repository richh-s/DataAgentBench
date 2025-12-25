code = """import json, pandas as pd

# Stream-load publications file to reduce memory
with open(var_call_kCZxtxu6LfMAIZGr2LkCu56R, 'r') as f:
    pubs = json.load(f)

# Function to parse year
def get_year(s):
    if not isinstance(s, str) or len(s) < 4:
        return None
    tail = s.strip()[-4:]
    return int(tail) if tail.isdigit() else None

codes_records = []
for row in pubs:
    year = get_year(row.get('publication_date'))
    if year is None:
        continue
    cpc_str = row.get('cpc')
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        continue
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code:
            continue
        codes_records.append({'year': year, 'code': code})

codes_df = pd.DataFrame(codes_records)

# Count filings per code per year
counts = codes_df.groupby(['code','year']).size().reset_index(name='count')

# Compute EMA per code sorted by year with alpha=0.2
alpha = 0.2
ema_records = []
for code, grp in counts.sort_values('year').groupby('code'):
    ema = None
    for _, r in grp.iterrows():
        y = int(r['year'])
        c = r['count']
        ema = c if ema is None else alpha * c + (1-alpha) * ema
        ema_records.append({'code': code, 'year': y, 'ema': float(ema)})

ema_df = pd.DataFrame(ema_records)

# For each code, find year with max EMA
idx = ema_df.groupby('code')['ema'].idxmax()
best_df = ema_df.loc[idx].reset_index(drop=True)

# Keep only codes whose best year is 2022
best_2022 = best_df[best_df['year'] == 2022]

# Load level-5 CPC symbols
with open(var_call_GWbCuX4DXrgXZjv71mGDeYyW, 'r') as f:
    defs = json.load(f)
level5_df = pd.DataFrame(defs)
level5_symbols = set(level5_df['symbol'].astype(str))

# Filter codes to those that exactly match a level-5 symbol
result_codes = sorted([c for c in best_2022['code'].unique() if c in level5_symbols])

import json as _json
out = _json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kCZxtxu6LfMAIZGr2LkCu56R': 'file_storage/call_kCZxtxu6LfMAIZGr2LkCu56R.json', 'var_call_GWbCuX4DXrgXZjv71mGDeYyW': 'file_storage/call_GWbCuX4DXrgXZjv71mGDeYyW.json'}

exec(code, env_args)
