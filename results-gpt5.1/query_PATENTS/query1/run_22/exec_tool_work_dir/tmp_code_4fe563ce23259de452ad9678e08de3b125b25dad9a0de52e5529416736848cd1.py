code = """import json, pandas as pd, datetime
from datetime import datetime

# Load full results from files
with open(var_call_5E2oUEGX7FqyEagflNC5p7ny, 'r') as f:
    cpc_level5 = json.load(f)
with open(var_call_0MQhvAe5ujVGg2Ukg5pPJb9T, 'r') as f:
    pub_rows = json.load(f)

level5_symbols = set(r['symbol'] for r in cpc_level5)

records = []
for row in pub_rows:
    cpc_str = row.get('cpc')
    pub_date_str = row.get('publication_date')
    if not cpc_str or not pub_date_str:
        continue
    try:
        year = datetime.strptime(pub_date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        try:
            year = datetime.strptime(pub_date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%B %d, %Y').year
        except Exception:
            continue
    try:
        codes = json.loads(cpc_str)
    except Exception:
        continue
    for c in codes:
        code = c.get('code')
        if not code:
            continue
        symbol = code.split('/')[0]
        if symbol in level5_symbols:
            records.append({'symbol': symbol, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # compute EMA per symbol ordered by year
    alpha = 0.2
    ema_rows = []
    for sym, grp in counts.groupby('symbol'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            if ema is None:
                ema = r['count']
            else:
                ema = alpha * r['count'] + (1-alpha) * ema
            ema_rows.append({'symbol': sym, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # for each symbol, find year with max ema
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx]
    # filter best year == 2022
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5E2oUEGX7FqyEagflNC5p7ny': 'file_storage/call_5E2oUEGX7FqyEagflNC5p7ny.json', 'var_call_0MQhvAe5ujVGg2Ukg5pPJb9T': 'file_storage/call_0MQhvAe5ujVGg2Ukg5pPJb9T.json'}

exec(code, env_args)
