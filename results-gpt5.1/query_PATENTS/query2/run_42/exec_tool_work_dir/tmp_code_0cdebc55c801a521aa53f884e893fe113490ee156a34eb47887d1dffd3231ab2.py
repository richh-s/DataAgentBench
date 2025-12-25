code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_RK9mtT0CJ3Sjr4waejsYnD9b
with open(path) as f:
    data = json.load(f)

rows = []
for r in data:
    info = r.get('Patents_info','') or ''
    if 'Germany' not in info and 'DE-' not in info and ' country code DE' not in info:
        continue
    gd = r.get('grant_date') or ''
    if not gd:
        continue
    txt = gd.lower().replace('dated','').strip()
    txt = re.sub(r"(st|nd|rd|th)", '', txt)
    txt = txt.replace('of ','')
    try:
        dt = datetime.strptime(txt, '%d %B %Y')
    except:
        try:
            dt = datetime.strptime(txt, '%B %d %Y')
        except:
            continue
    if not (dt.year==2019 and dt.month>=7 and dt.month<=12):
        continue
    year = dt.year
    try:
        cpcs = json.loads(r.get('cpc') or '[]')
    except:
        continue
    codes = [c.get('code') for c in cpcs if isinstance(c,dict) and c.get('code')]
    if not codes:
        continue
    for code in codes:
        m = re.match(r'^([A-Z]\d+[A-Z]\d+)/', code)
        lvl4 = m.group(1) if m else code.split('/')[0]
        rows.append({'year': year, 'code_full': code, 'code_level4': lvl4})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['code_level4','year']).size().reset_index(name='filings')
    alpha = 0.1
    ema_rows = []
    for code, sub in counts.groupby('code_level4'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            f = row['filings']
            if ema is None:
                ema = f
            else:
                ema = alpha*f + (1-alpha)*ema
            ema_rows.append({'code_level4': code, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    idx = ema_df.groupby('code_level4')['ema'].idxmax()
    best = ema_df.loc[idx].copy()
    best.rename(columns={'year':'best_year','ema':'best_ema'}, inplace=True)
    result = best.sort_values('best_ema', ascending=False).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RK9mtT0CJ3Sjr4waejsYnD9b': 'file_storage/call_RK9mtT0CJ3Sjr4waejsYnD9b.json'}

exec(code, env_args)
