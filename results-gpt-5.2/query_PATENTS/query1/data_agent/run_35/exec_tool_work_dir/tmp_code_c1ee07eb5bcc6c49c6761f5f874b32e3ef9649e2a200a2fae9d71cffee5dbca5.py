code = """import json, re
import pandas as pd

# load publication records
src = var_call_qpR3ATeoCwFUAOHtgVtCxk1N
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

# load level-5 CPC symbols
lvl5 = var_call_BTnT0f3EcukTChQ9TdHWuB0j
if isinstance(lvl5, str):
    with open(lvl5, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

def parse_cpc_codes(s):
    if not s:
        return []
    try:
        arr = json.loads(s)
        codes = []
        for o in arr:
            c = o.get('code') if isinstance(o, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback: regex for CPC-like codes
        return re.findall(r'\b[A-HY][0-9]{2}[A-Z]\s*\d+\/\d+\b', s)

def lvl5_group(code):
    # take part before '/', then first 4 chars
    if not code:
        return None
    code = code.strip().replace(' ', '')
    pre = code.split('/')[0]
    if len(pre) >= 4:
        return pre[:4]
    return None

rows = []
for r in recs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    groups = set()
    for c in codes:
        g = lvl5_group(c)
        if g and g in lvl5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
    raise SystemExit

counts = df.groupby(['symbol','year']).size().reset_index(name='filings')

alpha = 0.2

def ema_for_group(gdf):
    gdf = gdf.sort_values('year').copy()
    ema = []
    prev = None
    for v in gdf['filings'].tolist():
        if prev is None:
            prev = float(v)
        else:
            prev = alpha*float(v) + (1-alpha)*prev
        ema.append(prev)
    gdf['ema'] = ema
    return gdf

ema_df = counts.groupby('symbol', group_keys=False).apply(ema_for_group)

# For each year, find max EMA across symbols, then keep symbols achieving it (ties allowed)
yearly_max = ema_df.groupby('year')['ema'].max().reset_index(name='max_ema')
merged = ema_df.merge(yearly_max, on='year', how='inner')
leaders = merged[merged['ema'] == merged['max_ema']][['symbol','year','ema']]

# For each symbol, determine its best year among years it led (highest ema; tie -> latest year)
leaders_sorted = leaders.sort_values(['symbol','ema','year'], ascending=[True, False, False])
best = leaders_sorted.groupby('symbol', as_index=False).first()

# filter whose best year is 2022
result = sorted(best[best['year']==2022]['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qpR3ATeoCwFUAOHtgVtCxk1N': 'file_storage/call_qpR3ATeoCwFUAOHtgVtCxk1N.json', 'var_call_BTnT0f3EcukTChQ9TdHWuB0j': 'file_storage/call_BTnT0f3EcukTChQ9TdHWuB0j.json'}

exec(code, env_args)
