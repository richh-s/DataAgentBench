code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_vUsVGQabstUH6Pt1Q3U3QgMT
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

months_h2 = {'july','august','september','october','november','december'}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_grant_h2_2019(s):
    if not s: return False
    y = parse_year(s)
    if y != 2019: return False
    sl = s.lower()
    return any(mon in sl for mon in months_h2)

def country_is_de(patents_info):
    if not patents_info: return False
    return bool(re.search(r'\bDE\b', patents_info)) or bool(re.search(r'\bGermany\b', patents_info, flags=re.I))

rows=[]
for r in recs:
    if not is_grant_h2_2019(r.get('grant_date')):
        continue
    if not country_is_de(r.get('Patents_info')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_txt = r.get('cpc')
    if not cpc_txt:
        continue
    try:
        cpcs = json.loads(cpc_txt)
    except Exception:
        continue
    codes = []
    for c in cpcs:
        code = c.get('code') if isinstance(c, dict) else None
        if not code: continue
        # level 4 group like 'G06F21/31' -> 'G06F21/00'
        m = re.match(r'^([A-HY]\d\d[A-Z]\d+)/(\d+)$', code)
        if m:
            grp = f"{m.group(1)}/00"
            codes.append(grp)
    if not codes:
        continue
    # de-duplicate per patent
    for grp in sorted(set(codes)):
        rows.append({'cpc4': grp, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='n')
    # compute EMA per cpc4 over years
    alpha = 0.1
    best = []
    for cpc4, g in counts.groupby('cpc4'):
        g2 = g.sort_values('filing_year')
        ema = None
        for _, row in g2.iterrows():
            x = float(row['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            best.append({'cpc4': cpc4, 'year': int(row['filing_year']), 'ema': float(ema)})
    bestdf = pd.DataFrame(best)
    idx = bestdf.groupby('cpc4')['ema'].idxmax()
    top = bestdf.loc[idx].sort_values(['ema','cpc4'], ascending=[False, True])
    out = top.to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4XFfd7A7C23DbTY8XxRkcxdZ': ['publicationinfo'], 'var_call_X7PSuLjTPfBuTGXj9ZaSnDQm': ['cpc_definition'], 'var_call_vUsVGQabstUH6Pt1Q3U3QgMT': 'file_storage/call_vUsVGQabstUH6Pt1Q3U3QgMT.json'}

exec(code, env_args)
