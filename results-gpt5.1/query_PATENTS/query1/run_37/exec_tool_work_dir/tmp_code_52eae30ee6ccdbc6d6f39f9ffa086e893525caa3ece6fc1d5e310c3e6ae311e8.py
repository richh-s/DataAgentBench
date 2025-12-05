code = """import json, pandas as pd
from datetime import datetime

# Load full results if file paths
cpc_defs_file = var_call_fFJFAZ68l4hV2iyOQYaGaU6K
pubs_file = var_call_UIP2lNpSDHfifqmAOjz8OGHz

with open(cpc_defs_file, 'r') as f:
    cpc_defs = json.load(f)
with open(pubs_file, 'r') as f:
    pubs = json.load(f)

level5_symbols = {row['symbol'] for row in cpc_defs}

records = []
for row in pubs:
    cpc_raw = row.get('cpc')
    pub_date = row.get('publication_date')
    if not cpc_raw or not pub_date:
        continue
    try:
        year = datetime.strptime(pub_date.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        try:
            year = datetime.strptime(pub_date.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%B %d, %Y').year
        except Exception:
            continue
    if year is None:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        group = code.split(' ')[0]
        if group in level5_symbols:
            records.append({'symbol': group, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # compute EMA per symbol over years
    out_rows = []
    alpha = 0.2
    for sym, g in counts.groupby('symbol'):
        g2 = g.sort_values('year')
        ema = None
        best_year = None
        best_ema = None
        for _, r in g2.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            y = int(r['year'])
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        if best_year == 2022:
            out_rows.append({'symbol': sym, 'best_year': best_year, 'best_ema': best_ema})
    # keep only symbols whose best year (max EMA) is 2022, return CPC group codes level 5
    result = sorted([r['symbol'] for r in out_rows])

import json as _json
res_json = _json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_fFJFAZ68l4hV2iyOQYaGaU6K': 'file_storage/call_fFJFAZ68l4hV2iyOQYaGaU6K.json', 'var_call_UIP2lNpSDHfifqmAOjz8OGHz': 'file_storage/call_UIP2lNpSDHfifqmAOjz8OGHz.json', 'var_call_kQY2B2i7ZhLwaDWIn7RHTcOw': 'file_storage/call_kQY2B2i7ZhLwaDWIn7RHTcOw.json'}

exec(code, env_args)
