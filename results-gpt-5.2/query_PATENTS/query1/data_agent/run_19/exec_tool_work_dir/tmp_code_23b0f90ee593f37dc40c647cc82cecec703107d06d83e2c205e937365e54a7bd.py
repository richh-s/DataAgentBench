code = """import json, re
import pandas as pd
from datetime import datetime

# Load filings
path_filings = var_call_pWNmJ3lun31aTiN9dAL3F0Sr
with open(path_filings, 'r', encoding='utf-8') as f:
    filings = json.load(f)

# Load level-5 CPC symbols list
path_lvl5 = var_call_DPWC6wU7f14T4iWWpeusqtKa
with open(path_lvl5, 'r', encoding='utf-8') as f:
    lvl5 = json.load(f)

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_codes(s):
    if not s:
        return []
    try:
        data = json.loads(s)
        codes = []
        for item in data:
            code = item.get('code') if isinstance(item, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # fallback: extract patterns like H01M10/0565
        return re.findall(r'[A-HY]\d{2}[A-Z]\d+(?:/\d+)?', s)

rows = []
for rec in filings:
    y = parse_year(rec.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(rec.get('cpc'))
    if not codes:
        continue
    # count each unique level-5 group once per patent record
    groups = set()
    for c in codes:
        g = c.split('/')[0]
        if g in lvl5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['cpc5','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['cpc5','year']).reset_index(name='filings')
    # ensure continuous years per cpc between min and max for EMA
    results = []
    alpha = 0.2
    for cpc5, grp in counts.groupby('cpc5'):
        g = grp.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        m = pd.DataFrame({'year': years}).merge(g[['year','filings']], on='year', how='left').fillna({'filings':0})
        ema = None
        emas = []
        for v in m['filings'].tolist():
            if ema is None:
                ema = float(v)
            else:
                ema = alpha*float(v) + (1-alpha)*ema
            emas.append(ema)
        m['ema'] = emas
        best_idx = m['ema'].idxmax()
        best_year = int(m.loc[best_idx,'year'])
        best_ema = float(m.loc[best_idx,'ema'])
        results.append({'cpc5': cpc5, 'best_year': best_year, 'best_ema': best_ema})
    resdf = pd.DataFrame(results)
    # filter best year 2022
    out = resdf[resdf['best_year']==2022].sort_values(['best_ema','cpc5'], ascending=[False, True])['cpc5'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pWNmJ3lun31aTiN9dAL3F0Sr': 'file_storage/call_pWNmJ3lun31aTiN9dAL3F0Sr.json', 'var_call_DPWC6wU7f14T4iWWpeusqtKa': 'file_storage/call_DPWC6wU7f14T4iWWpeusqtKa.json'}

exec(code, env_args)
