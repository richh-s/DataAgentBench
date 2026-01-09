code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_XSlEaZSv0NBhmnPUGoGFb0Bb)
level5 = load_records(var_call_10jcgYrKFwYt9Yl29lQHGkAM)

# Level 5 group codes are 4-character symbols like H01M, A01N, etc.
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

# parse year from filing_date natural language
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
        for e in arr:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        return []

def to_group(code):
    # remove spaces
    code = code.strip()
    return code[:4] if len(code) >= 4 else None

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    for c in parse_cpc_codes(r.get('cpc')):
        g = to_group(c)
        if g and g in level5_set:
            rows.append((y, g))

df = pd.DataFrame(rows, columns=['year','group'])
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='n')
    # ensure continuous years per group
    alpha = 0.2
    best = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        years = list(range(int(sub['year'].min()), int(sub['year'].max())+1))
        sub2 = sub.set_index('year').reindex(years, fill_value=0).reset_index().rename(columns={'index':'year'})
        ema = None
        ema_vals = []
        for n in sub2['n'].tolist():
            ema = n if ema is None else alpha*n + (1-alpha)*ema
            ema_vals.append(ema)
        sub2['ema'] = ema_vals
        # best year by ema (if ties pick latest year)
        mx = sub2['ema'].max()
        best_year = int(sub2.loc[sub2['ema']==mx, 'year'].max())
        best.append({'group': g, 'best_year': best_year, 'best_ema': float(mx)})
    best_df = pd.DataFrame(best)
    out = best_df[best_df['best_year']==2022].sort_values(['best_ema','group'], ascending=[False, True])['group'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XSlEaZSv0NBhmnPUGoGFb0Bb': 'file_storage/call_XSlEaZSv0NBhmnPUGoGFb0Bb.json', 'var_call_10jcgYrKFwYt9Yl29lQHGkAM': 'file_storage/call_10jcgYrKFwYt9Yl29lQHGkAM.json'}

exec(code, env_args)
