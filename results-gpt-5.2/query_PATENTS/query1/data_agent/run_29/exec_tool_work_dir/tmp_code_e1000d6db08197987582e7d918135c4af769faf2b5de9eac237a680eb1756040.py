code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_YU1zNJQrfJPggOHMVuG2wvGd)
level5 = load_records(var_call_h0JG7tD3F2YQcnpk2QzRtwuh)
level5_set = set([r['symbol'] for r in level5 if r.get('symbol')])

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

# parse year from natural language dates
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(s):
    if not s:
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# parse CPC list json-like

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback: find patterns like A01B33/00 etc
        return re.findall(r'\b[A-HY][0-9]{2}[A-Z][0-9]+\/[0-9A-Z]+\b', cpc_str)

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each level-5 group once per publication record
    used = set()
    for c in codes:
        if c in level5_set and c not in used:
            rows.append((c, y))
            used.add(c)

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings').sort_values(['symbol','year'])
    alpha = 0.2
    # compute EMA per symbol by ascending year
    def ema_group(g):
        g = g.sort_values('year').copy()
        ema = []
        prev = None
        for v in g['filings'].tolist():
            prev = v if prev is None else (alpha*v + (1-alpha)*prev)
            ema.append(prev)
        g['ema'] = ema
        return g
    ema_df = counts.groupby('symbol', group_keys=False).apply(ema_group)
    # best year per symbol = year with max EMA; tie -> latest year
    best = (ema_df.sort_values(['symbol','ema','year'])
                  .groupby('symbol', as_index=False)
                  .tail(1)[['symbol','year','ema']]
                  .rename(columns={'year':'best_year','ema':'best_ema'}))
    out = sorted(best.loc[best['best_year']==2022, 'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YU1zNJQrfJPggOHMVuG2wvGd': 'file_storage/call_YU1zNJQrfJPggOHMVuG2wvGd.json', 'var_call_h0JG7tD3F2YQcnpk2QzRtwuh': 'file_storage/call_h0JG7tD3F2YQcnpk2QzRtwuh.json'}

exec(code, env_args)
