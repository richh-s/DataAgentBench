code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_6oGX5jW2XE0VkcSfWsubh8mx)
lev5 = load_records(var_call_oHKfXpvK8y8Gd0VqYO1zqGbG)

lev5_set = set(r['symbol'] for r in lev5 if r.get('symbol'))

months = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for o in arr:
            c = o.get('code') if isinstance(o, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for codes like H01M10/0565
        return re.findall(r'"code"\s*:\s*"([A-Z]\\d{2}[A-Z]\\d+(?:/\\d+)?(?:\\d+)?)"', cpc_str)

def to_level5_group(code):
    # group at level 5 in this DB seems to be subclass like H01M, C01B, etc.
    m = re.match(r'^([A-HY]\\d{2}[A-Z])', code)
    return m.group(1) if m else None

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    for c in codes:
        g = to_level5_group(c)
        if g and g in lev5_set:
            rows.append((g, y))

if not rows:
    out = []
else:
    df = pd.DataFrame(rows, columns=['group','year'])
    counts = df.groupby(['group','year']).size().rename('n').reset_index()
    # build full year index per group
    alpha = 0.2
    res = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        years = list(range(int(sub['year'].min()), int(sub['year'].max())+1))
        sub2 = pd.DataFrame({'year': years}).merge(sub[['year','n']], on='year', how='left').fillna({'n':0})
        ema = None
        best_year = None
        best_val = None
        for yy, n in zip(sub2['year'].tolist(), sub2['n'].tolist()):
            if ema is None:
                ema = float(n)
            else:
                ema = alpha*float(n) + (1-alpha)*ema
            if best_val is None or ema > best_val:
                best_val = ema
                best_year = int(yy)
        if best_year == 2022:
            res.append(g)
    out = sorted(set(res))

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6oGX5jW2XE0VkcSfWsubh8mx': 'file_storage/call_6oGX5jW2XE0VkcSfWsubh8mx.json', 'var_call_oHKfXpvK8y8Gd0VqYO1zqGbG': 'file_storage/call_oHKfXpvK8y8Gd0VqYO1zqGbG.json'}

exec(code, env_args)
