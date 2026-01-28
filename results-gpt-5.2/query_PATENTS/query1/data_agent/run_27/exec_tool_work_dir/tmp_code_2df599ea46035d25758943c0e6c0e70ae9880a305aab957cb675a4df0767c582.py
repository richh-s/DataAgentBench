code = """import json, re
import pandas as pd

# Load filings
src = var_call_t5NveMPRv20pUtiHHB9B7YA3
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        filings = json.load(f)
else:
    filings = src

# Load level-5 CPC symbols
src2 = var_call_Gq7pWuzXJmfDiHkXEhYOpvdU
if isinstance(src2, str):
    with open(src2, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = src2
lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol') is not None)

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    if not m:
        return None
    return int(m.group(0))

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code')
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d\d[A-Z]\d+(?:/\d+)?)"', cpc_str)

rows = []
for r in filings:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # unique per patent record to avoid duplicates within same doc
    for c in set(codes):
        if c in lvl5_set:
            rows.append((c, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    alpha = 0.2

    # compute EMA per symbol across full year range
    res = []
    for sym, g in counts.groupby('symbol'):
        g2 = g.sort_values('year')
        years = list(range(int(g2['year'].min()), int(g2['year'].max())+1))
        s = pd.Series(0, index=years, dtype='float64')
        s.loc[g2['year'].astype(int).tolist()] = g2['filings'].astype(float).tolist()
        ema = []
        prev = None
        for v in s.values:
            prev = v if prev is None else (alpha*v + (1-alpha)*prev)
            ema.append(prev)
        ema_s = pd.Series(ema, index=years)
        best_year = int(ema_s.idxmax())
        if best_year == 2022:
            res.append(sym)

    out = sorted(set(res))

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_t5NveMPRv20pUtiHHB9B7YA3': 'file_storage/call_t5NveMPRv20pUtiHHB9B7YA3.json', 'var_call_Gq7pWuzXJmfDiHkXEhYOpvdU': 'file_storage/call_Gq7pWuzXJmfDiHkXEhYOpvdU.json'}

exec(code, env_args)
