code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_yeg3fuEGMay4iL9yBVnrfy62)
level5 = load_records(var_call_YiwvPi5kx8U426WgUhBtvuOZ)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_codes(s):
    if not s:
        return []
    try:
        arr = json.loads(s)
        codes = []
        for e in arr:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d?.*?)"', s)

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # count each level5 symbol at most once per publication record
    seen = set()
    for c in codes:
        sym = c.split('/')[0]
        if sym in level5_set and sym not in seen:
            rows.append((sym, y, 1))
            seen.add(sym)

df = pd.DataFrame(rows, columns=['symbol','year','cnt'])
if df.empty:
    out = []
else:
    yearly = df.groupby(['symbol','year'], as_index=False)['cnt'].sum()
    # compute EMA per symbol across years
    alpha = 0.2
    res = []
    for sym, g in yearly.groupby('symbol'):
        g = g.sort_values('year')
        ema = None
        for _, rr in g.iterrows():
            x = float(rr['cnt'])
            ema = x if ema is None else (alpha * x + (1-alpha) * ema)
            res.append({'symbol': sym, 'year': int(rr['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(res)
    # for each year, find symbol(s) with max ema
    max_per_year = ema_df.loc[ema_df.groupby('year')['ema'].transform('max') == ema_df['ema']]
    # determine best year per symbol among years where it was max
    # choose year with maximum ema for symbol; tie -> latest year
    best = (max_per_year.sort_values(['symbol','ema','year']).groupby('symbol').tail(1))
    out = sorted(best.loc[best['year']==2022, 'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yeg3fuEGMay4iL9yBVnrfy62': 'file_storage/call_yeg3fuEGMay4iL9yBVnrfy62.json', 'var_call_YiwvPi5kx8U426WgUhBtvuOZ': 'file_storage/call_YiwvPi5kx8U426WgUhBtvuOZ.json'}

exec(code, env_args)
