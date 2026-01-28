code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_5uYSuV3L4jlp95OBj7Ma0iY6)
lev5 = load_records(var_call_B9mFhLn60b93hDJBAJldJNMN)

lev5_set = set(r['symbol'] for r in lev5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    if m:
        return int(m.group(0))
    return None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        obj = json.loads(cpc_str)
        codes = []
        for e in obj:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for codes like H01M10/0565
        return re.findall(r'\"code\"\s*:\s*\"([^\"]+)\"', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    # unique per publication to avoid duplicates within same record
    codes = list(dict.fromkeys(codes))
    for c in codes:
        # keep only level-5 symbols (as provided)
        if c in lev5_set:
            rows.append((c, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().rename('filings').reset_index()
    # ensure continuous years per symbol
    alpha = 0.2
    ema_records = []
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        m = dict(zip(g['year'].astype(int), g['filings'].astype(float)))
        ema = None
        for yr in years:
            x = float(m.get(yr, 0.0))
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            ema_records.append((yr, sym, x, ema))
    ema_df = pd.DataFrame(ema_records, columns=['year','symbol','filings','ema'])
    # pick symbol with highest ema each year
    idx = ema_df.groupby('year')['ema'].idxmax()
    top = ema_df.loc[idx, ['year','symbol','ema']].sort_values('year')
    # for each symbol, determine best year (max ema; if tie choose latest)
    sym_best = (ema_df.sort_values(['symbol','ema','year'], ascending=[True, False, False])
                .groupby('symbol').head(1)[['symbol','year']]
                .rename(columns={'year':'best_year'}))
    top = top.merge(sym_best, on='symbol', how='left')
    out = top[top['best_year']==2022]['symbol'].drop_duplicates().tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5uYSuV3L4jlp95OBj7Ma0iY6': 'file_storage/call_5uYSuV3L4jlp95OBj7Ma0iY6.json', 'var_call_B9mFhLn60b93hDJBAJldJNMN': 'file_storage/call_B9mFhLn60b93hDJBAJldJNMN.json'}

exec(code, env_args)
