code = """import json, re
import pandas as pd

# Load filings+cpc rows
src = var_call_4aY2EFJ1MU6nCizPEx5c3n9p
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        rows = json.load(f)
else:
    rows = src

# Load level-5 CPC symbols list
src2 = var_call_OWTEgJglW25jcbiwjAsHCmwv
if isinstance(src2, str):
    with open(src2, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = src2
lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

# explode into (year, cpc_symbol) counting each publication once per CPC code (dedup within record)
out = []
for r in rows:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    codes = []
    for c in cpcs:
        code = c.get('code') if isinstance(c, dict) else None
        if code:
            codes.append(code.strip())
    if not codes:
        continue
    # dedup per publication
    for code in sorted(set(codes)):
        # keep only exact level-5 symbols
        if code in lvl5_set:
            out.append((y, code))

df = pd.DataFrame(out, columns=['year','symbol'])
if df.empty:
    res = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')
    # build EMA per symbol across years (fill missing years with 0 between min/max per symbol)
    alpha = 0.2
    best = []
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        m = pd.DataFrame({'year': years})
        m = m.merge(g[['year','filings']], on='year', how='left').fillna({'filings':0})
        ema = None
        emas = []
        for v in m['filings'].tolist():
            ema = v if ema is None else alpha*v + (1-alpha)*ema
            emas.append(ema)
        m['ema'] = emas
        idx = m['ema'].idxmax()
        best_year = int(m.loc[idx,'year'])
        best_ema = float(m.loc[idx,'ema'])
        best.append((sym, best_year, best_ema))
    best_df = pd.DataFrame(best, columns=['symbol','best_year','best_ema'])
    res = sorted(best_df.loc[best_df['best_year']==2022,'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_4aY2EFJ1MU6nCizPEx5c3n9p': 'file_storage/call_4aY2EFJ1MU6nCizPEx5c3n9p.json', 'var_call_OWTEgJglW25jcbiwjAsHCmwv': 'file_storage/call_OWTEgJglW25jcbiwjAsHCmwv.json'}

exec(code, env_args)
