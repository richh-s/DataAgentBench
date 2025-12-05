code = """import json, pandas as pd
from datetime import datetime

# Load full CPC level-5 symbols from file
cpc_file = var_call_EnWkF7KVVQDse846XNEVFXWV
with open(cpc_file, 'r') as f:
    cpc_level5 = json.load(f)
level5_symbols = {r['symbol'] for r in cpc_level5}

# Load publication data
pub_file = var_call_G7kfVcG1fWJMWp9OMLOmE4l8
with open(pub_file, 'r') as f:
    pubs = json.load(f)

records = []
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

for row in pubs:
    date_str = row.get('publication_date')
    cpc_str = row.get('cpc')
    if not date_str or not cpc_str:
        continue
    try:
        parts = date_str.replace(',', '').split()
        if len(parts) >= 3:
            mon = parts[0][:3]
            day = int(parts[1].rstrip('stndrth'))
            year = int(parts[2])
        else:
            continue
    except Exception:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpc_str)]
    except Exception:
        continue
    for code in codes:
        base = code.split('(')[0].strip()
        if base in level5_symbols:
            records.append({'year': year, 'symbol': base, 'count': 1})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    yearly = df.groupby(['symbol','year'])['count'].sum().reset_index()
    years_sorted = sorted(yearly['year'].unique())

    # compute EMA per symbol over years
    alpha = 0.2
    ema_records = []
    for sym, g in yearly.groupby('symbol'):
        counts = {row['year']: row['count'] for _, row in g.iterrows()}
        ema = None
        for y in years_sorted:
            c = counts.get(y, 0)
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'symbol': sym, 'year': y, 'ema': ema})

    ema_df = pd.DataFrame(ema_records)

    # find best (max EMA) year per symbol
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # filter where best year is 2022
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_EnWkF7KVVQDse846XNEVFXWV': 'file_storage/call_EnWkF7KVVQDse846XNEVFXWV.json', 'var_call_G7kfVcG1fWJMWp9OMLOmE4l8': 'file_storage/call_G7kfVcG1fWJMWp9OMLOmE4l8.json', 'var_call_qu1uahdpw4ixTY4FDGoFXzht': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}]}

exec(code, env_args)
