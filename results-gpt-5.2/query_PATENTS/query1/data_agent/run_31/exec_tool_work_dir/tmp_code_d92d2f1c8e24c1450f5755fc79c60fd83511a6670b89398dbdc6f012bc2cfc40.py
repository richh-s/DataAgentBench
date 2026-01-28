code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_FXfemooPIkVSaLrbvzgM9ReZ)
level5 = load_records(var_call_EVHqfamvMTIJdfVRJU8vpEr8)

level5_set = set(r['symbol'] for r in level5 if r.get('symbol') is not None)

year_re = re.compile(r'(19\d{2}|20\d{2})')

def extract_year(s):
    if not s:
        return None
    m = year_re.search(s)
    return int(m.group(1)) if m else None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for item in data:
            code = item.get('code') if isinstance(item, dict) else None
            if code:
                # normalize: remove spaces
                codes.append(code.strip())
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d\d[A-Z]\d+(?:/\d+)?)"', cpc_str)

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    for code in extract_cpc_codes(r.get('cpc')):
        grp = code.split('/')[0]  # level-5 group symbol (e.g., H01M)
        if grp in level5_set:
            rows.append((grp, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')
    # compute EMA per symbol across years
    alpha = 0.2
    def ema_for_symbol(g):
        g = g.sort_values('year')
        ema = []
        prev = None
        for v in g['filings'].tolist():
            prev = v if prev is None else alpha*v + (1-alpha)*prev
            ema.append(prev)
        g = g.copy()
        g['ema'] = ema
        return g
    emadf = counts.groupby('symbol', group_keys=False).apply(ema_for_symbol)
    # find best year per symbol (max ema; tie -> latest year)
    emadf = emadf.sort_values(['symbol','ema','year'], ascending=[True,False,False])
    best = emadf.groupby('symbol').head(1)
    out = sorted(best.loc[best['year']==2022, 'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FXfemooPIkVSaLrbvzgM9ReZ': 'file_storage/call_FXfemooPIkVSaLrbvzgM9ReZ.json', 'var_call_EVHqfamvMTIJdfVRJU8vpEr8': 'file_storage/call_EVHqfamvMTIJdfVRJU8vpEr8.json'}

exec(code, env_args)
