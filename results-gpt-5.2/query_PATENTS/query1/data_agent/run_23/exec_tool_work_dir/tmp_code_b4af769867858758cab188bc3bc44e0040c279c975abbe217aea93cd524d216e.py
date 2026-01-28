code = """import json, re
import pandas as pd
from datetime import datetime

# Load publication records
pub_src = var_call_ztOLPWFoF3umUFsjZIdxDk3c
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

# Load level-5 symbols
lvl_src = var_call_xfpYG51OnHniDvl22CP8MGyJ
if isinstance(lvl_src, str):
    with open(lvl_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl_src
lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol') is not None)

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    y = int(m.group(1))
    return y

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for it in arr:
            c = it.get('code') if isinstance(it, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for CPC-like tokens
        return re.findall(r'\b[A-HY][0-9]{2}[A-Z]\s*\d+(?:/\d+)?\b', cpc_str)

def group_level5(code):
    # group as first 4 chars (e.g., H01M) to match lvl5_set
    if not code:
        return None
    code = code.strip().replace(' ', '')
    if len(code) < 4:
        return None
    g = code[:4]
    return g if g in lvl5_set else None

rows = []
for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    gs = set(filter(None, (group_level5(c) for c in codes)))
    for g in gs:
        rows.append((y,g))

df = pd.DataFrame(rows, columns=['year','group'])
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='filings')

    # compute EMA per group over years
    alpha = 0.2
    def ema_for_group(gdf):
        gdf = gdf.sort_values('year').copy()
        ema = None
        emas = []
        for v in gdf['filings'].tolist():
            ema = v if ema is None else alpha*v + (1-alpha)*ema
            emas.append(ema)
        gdf['ema'] = emas
        return gdf

    ema_df = counts.groupby('group', group_keys=False).apply(ema_for_group)

    # for each year, find max EMA, possibly multiple groups
    max_by_year = ema_df.groupby('year')['ema'].max().reset_index(name='max_ema')
    top = ema_df.merge(max_by_year, on='year')
    top = top[top['ema'] == top['max_ema']]

    # for each group, find best year (max EMA; tie -> latest year)
    def best_year(gdf):
        m = gdf['ema'].max()
        yrs = gdf.loc[gdf['ema'] == m, 'year']
        return int(yrs.max())

    best = ema_df.groupby('group').apply(best_year).reset_index(name='best_year')
    best_2022 = set(best.loc[best['best_year'] == 2022, 'group'])

    # return only CPC group codes at level 5 whose best year is 2022 and that are yearly top EMA at least in 2022? 
    # Interpretation: technology areas with the highest EMA of filings each year; then filter to those groups where their best year is 2022.
    # So keep groups that appear in `top` (top per year) and have best_year==2022.
    res = sorted(set(top.loc[top['group'].isin(best_2022), 'group']))
    out = res

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ztOLPWFoF3umUFsjZIdxDk3c': 'file_storage/call_ztOLPWFoF3umUFsjZIdxDk3c.json', 'var_call_xfpYG51OnHniDvl22CP8MGyJ': 'file_storage/call_xfpYG51OnHniDvl22CP8MGyJ.json'}

exec(code, env_args)
