code = """import json, pandas as pd, datetime as dt

# Load full results from files
with open(var_call_b1sMqcCRU8KQ11YaSGx5lCO9, 'r') as f:
    cpc_level5 = json.load(f)
with open(var_call_ZITR2v8sILtRSAdtAqwLpaqz, 'r') as f:
    pubs = json.load(f)

# Prepare set of level 5 symbols (groups)
level5_syms = set(r['symbol'] for r in cpc_level5)

# Helper to parse natural-language dates to year
def parse_year(s):
    if not s:
        return None
    try:
        return dt.datetime.strptime(s, '%b %dth, %Y').year
    except Exception:
        try:
            return dt.datetime.strptime(s, '%b %dst, %Y').year
        except Exception:
            try:
                return dt.datetime.strptime(s, '%b %dnd, %Y').year
            except Exception:
                try:
                    return dt.datetime.strptime(s, '%b %drd, %Y').year
                except Exception:
                    return None

records = []
for row in pubs:
    year = parse_year(row['publication_date'])
    if year is None:
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for ent in cpc_list:
        code = ent.get('code')
        if not code:
            continue
        group = code.split('/')[0]  # group-level symbol
        if group in level5_syms:
            records.append({'symbol': group, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # Compute EMA per symbol sorted by year ascending
    alphas = 0.2
    ema_rows = []
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        ema = None
        for _, r in g.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alphas * c + (1-alphas) * ema
            ema_rows.append({'symbol': sym, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # For each symbol, find year with max EMA
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # Filter to those whose best year is 2022
    best2022 = best[best['year'] == 2022]
    result = sorted(best2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_b1sMqcCRU8KQ11YaSGx5lCO9': 'file_storage/call_b1sMqcCRU8KQ11YaSGx5lCO9.json', 'var_call_ZITR2v8sILtRSAdtAqwLpaqz': 'file_storage/call_ZITR2v8sILtRSAdtAqwLpaqz.json'}

exec(code, env_args)
