code = """import json, pandas as pd, datetime

# load full results
with open(var_call_iGyGCRCHNawAc5WBxTnCOMH4, 'r') as f:
    level5 = json.load(f)
with open(var_call_mxLikvJnLSRTETlH0aFsiPNn, 'r') as f:
    pubs = json.load(f)

level5_codes = set([r['symbol'] for r in level5])

rows = []
for r in pubs:
    date_str = r['publication_date']
    cpc_raw = r['cpc']
    if not date_str or not cpc_raw:
        continue
    try:
        year = datetime.datetime.strptime(date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpc_raw)]
    except Exception:
        continue
    for code in codes:
        # map to group level 5: take section+class+subclass+group up to first space or to slash structure
        base = code.split()[0]
        # CPCDefinition level 5 symbols often like 'H01M' (subclass) or 'H01M4' (main group). Use prefix until non-alnum.
        prefix = ''.join(ch for ch in base if ch.isalnum())
        # generate all possible decreasing prefixes and match those that are in level5_codes
        match = None
        for i in range(len(prefix), 3, -1):
            p = prefix[:i]
            if p in level5_codes:
                match = p
                break
        if match:
            rows.append({'year': year, 'symbol': match})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # compute EMA per symbol sorted by year
    alpha = 0.2
    ema_records = []
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        ema = None
        for _, row in g.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_records.append({'symbol': sym, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    # for each symbol, find best year (max ema)
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx]
    # filter best year == 2022
    best2022 = best[best['year']==2022]
    result = sorted(best2022['symbol'].unique())

import json as jsonlib
out = jsonlib.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iGyGCRCHNawAc5WBxTnCOMH4': 'file_storage/call_iGyGCRCHNawAc5WBxTnCOMH4.json', 'var_call_mxLikvJnLSRTETlH0aFsiPNn': 'file_storage/call_mxLikvJnLSRTETlH0aFsiPNn.json'}

exec(code, env_args)
