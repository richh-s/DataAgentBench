code = """import json, pandas as pd
from datetime import datetime

# Load full results
with open(var_call_P1RByfKHYdxfxrPLRXUZ9yL2, 'r') as f:
    level5_symbols = json.load(f)
with open(var_call_5uwFSZC2WwFPb8zUMt43oWYn, 'r') as f:
    pubs = json.load(f)

level5_set = {r['symbol'] for r in level5_symbols}

rows = []
for r in pubs:
    date_str = r['publication_date']
    cpc_str = r['cpc']
    if not date_str or not cpc_str:
        continue
    try:
        pub_year = datetime.strptime(date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        try:
            pub_year = datetime.strptime(date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%B %d, %Y').year
        except Exception:
            continue
    try:
        codes = [e['code'] for e in json.loads(cpc_str)]
    except Exception:
        continue
    for code in codes:
        # map to level 5 by truncating at first non alnum or '/'
        # CPCDefinition symbols in this dataset look like section+2digits+letter(s). We'll generalize: take leading alnum letters until a non-alnum.
        base = ''
        for ch in code:
            if ch.isalnum():
                base += ch
            else:
                break
        if base in level5_set:
            rows.append({'symbol': base, 'year': pub_year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    grp = df.groupby(['symbol','year']).size().rename('count').reset_index()
    # compute EMA per symbol over years sorted
    alpha = 0.2
    ema_records = []
    for sym, g in grp.groupby('symbol'):
        g = g.sort_values('year')
        ema = None
        for _, row in g.iterrows():
            y = row['year']
            c = row['count']
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            ema_records.append({'symbol': sym, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    # for each symbol, find year with max ema
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx]
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['symbol'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_P1RByfKHYdxfxrPLRXUZ9yL2': 'file_storage/call_P1RByfKHYdxfxrPLRXUZ9yL2.json', 'var_call_5uwFSZC2WwFPb8zUMt43oWYn': 'file_storage/call_5uwFSZC2WwFPb8zUMt43oWYn.json'}

exec(code, env_args)
