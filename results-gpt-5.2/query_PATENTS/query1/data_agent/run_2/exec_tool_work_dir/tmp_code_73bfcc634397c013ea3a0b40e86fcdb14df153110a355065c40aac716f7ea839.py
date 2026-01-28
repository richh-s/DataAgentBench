code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_zLxqwcTubAb9o0F4K8uVgQ4A)
level5 = load_records(var_call_8LhNwzTFHwpqo0vFOclXZqHL)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

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
        for e in data:
            c = e.get('code')
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fallback: regex-like
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+(?:/\d+)?)"', s)

def to_level5(code):
    if not code:
        return None
    # normalize spaces
    code = code.strip().replace(' ', '')
    if '/' in code:
        return code.split('/')[0]
    return code

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # count a filing once per CPC group (deduplicate within publication)
    groups = {to_level5(c) for c in codes}
    groups.discard(None)
    groups = [g for g in groups if g in level5_set]
    for g in groups:
        rows.append((g, y, 1))

df = pd.DataFrame(rows, columns=['symbol','year','cnt'])
if df.empty:
    out = []
else:
    yearly = df.groupby(['symbol','year'], as_index=False)['cnt'].sum()
    # ensure continuous years per symbol for EMA by filling missing with 0
    res = []
    alpha = 0.2
    for sym, g in yearly.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        s = pd.Series(0.0, index=years)
        s.loc[g['year'].astype(int).tolist()] = g['cnt'].astype(float).tolist()
        ema = None
        for yr in years:
            x = float(s.loc[yr])
            if ema is None:
                ema = x
            else:
                ema = alpha*x + (1-alpha)*ema
            res.append({'symbol': sym, 'year': int(yr), 'ema': float(ema)})
    ema_df = pd.DataFrame(res)
    # find best year per symbol (max ema; tie -> latest year)
    ema_df = ema_df.sort_values(['symbol','ema','year'], ascending=[True, False, False])
    best = ema_df.groupby('symbol', as_index=False).first()
    out = sorted(best.loc[best['year']==2022, 'symbol'].tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zLxqwcTubAb9o0F4K8uVgQ4A': 'file_storage/call_zLxqwcTubAb9o0F4K8uVgQ4A.json', 'var_call_8LhNwzTFHwpqo0vFOclXZqHL': 'file_storage/call_8LhNwzTFHwpqo0vFOclXZqHL.json'}

exec(code, env_args)
