code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_1rIsZOJEB4jB1o9ksUP8AYMx)
lev5 = load_records(var_call_Z4rqYJdneODke1MwTuYJOXZM)

lev5_set = set(r['symbol'] for r in lev5 if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for x in arr:
            code = x.get('code') if isinstance(x, dict) else None
            if code:
                # normalize: take main symbol before any spaces
                code = code.strip()
                codes.append(code)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+(?:/\d+)?)"', cpc_str)

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    for code in codes:
        if code in lev5_set:
            rows.append((code, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().rename('count').reset_index()
    years = sorted(counts['year'].unique().tolist())
    alpha = 0.2
    # compute ema per symbol across full year range, filling missing with 0
    ema_rows = []
    for sym, g in counts.groupby('symbol'):
        s = g.set_index('year')['count']
        prev = None
        for y in years:
            x = float(s.get(y, 0.0))
            if prev is None:
                prev = x
            else:
                prev = alpha * x + (1-alpha) * prev
            ema_rows.append((sym, y, prev))
    ema = pd.DataFrame(ema_rows, columns=['symbol','year','ema'])
    # for each year, get symbols with max ema
    idx = ema.groupby('year')['ema'].transform('max') == ema['ema']
    top = ema[idx].copy()
    # for each symbol, best year = year where ema max; if tie take latest year
    smax = ema.sort_values(['symbol','ema','year']).groupby('symbol').tail(1)[['symbol','year','ema']]
    smax = smax.rename(columns={'year':'best_year','ema':'best_ema'})
    eligible = smax[smax['best_year']==2022]
    out = sorted(eligible['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1rIsZOJEB4jB1o9ksUP8AYMx': 'file_storage/call_1rIsZOJEB4jB1o9ksUP8AYMx.json', 'var_call_Z4rqYJdneODke1MwTuYJOXZM': 'file_storage/call_Z4rqYJdneODke1MwTuYJOXZM.json'}

exec(code, env_args)
