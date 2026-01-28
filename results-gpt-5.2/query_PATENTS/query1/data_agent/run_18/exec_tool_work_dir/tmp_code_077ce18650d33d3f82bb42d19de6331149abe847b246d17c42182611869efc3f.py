code = """import json, re
import pandas as pd

# Load publication rows
path_pubs = var_call_fgNcjHiX2ZnR3oINNJFhIFOt
with open(path_pubs, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Load level-5 CPC symbols
path_lvl5 = var_call_Zk5tWT6XM6KdZPOGViHgQCuu
with open(path_lvl5, 'r', encoding='utf-8') as f:
    lvl5_rows = json.load(f)

lvl5_set = set(r['symbol'] for r in lvl5_rows if r.get('symbol'))

# Helpers
month_map = {m.lower(): i for i,m in enumerate([
    'January','February','March','April','May','June','July','August','September','October','November','December'
], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        if isinstance(data, list):
            return [d.get('code') for d in data if isinstance(d, dict) and d.get('code')]
        return []
    except Exception:
        # fallback: regex find like A01B1/00 etc
        return re.findall(r'[A-HY]\\d{2}[A-Z]\\d+(?:/\\d+)?', cpc_str)

def to_lvl5_group(code):
    # level-5 group code in this dataset appears as 4 chars (e.g., H01M) rather than full subclass/group.
    # We'll map any CPC code to its first 4 chars if in lvl5 symbols.
    if not code or len(code) < 4:
        return None
    sym = code[:4]
    return sym if sym in lvl5_set else None

# Build counts per (symbol, year): count unique publications? No pub id available; count filings as rows.
# We'll count each publication row once per CPC symbol present (dedup within row).
records = []
for r in pubs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    syms = {to_lvl5_group(c) for c in codes}
    syms.discard(None)
    for s in syms:
        records.append((s, y))

df = pd.DataFrame(records, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # compute EMA per symbol across years ascending
    alpha = 0.2
    def ema_for_group(g):
        g = g.sort_values('year')
        ema = []
        prev = None
        for v in g['filings'].tolist():
            prev = v if prev is None else (alpha*v + (1-alpha)*prev)
            ema.append(prev)
        g = g.copy()
        g['ema'] = ema
        return g
    ema_df = counts.groupby('symbol', group_keys=False).apply(ema_for_group)
    # For each year, pick symbol(s) with highest ema
    year_max = ema_df.groupby('year')['ema'].transform('max')
    top_each_year = ema_df[ema_df['ema'] == year_max][['symbol','year','ema']]
    # Determine best year per symbol (year of max ema; choose latest if tie)
    sym_best = ema_df.sort_values(['symbol','ema','year']).groupby('symbol').tail(1)[['symbol','year','ema']]
    sym_best = sym_best.rename(columns={'year':'best_year','ema':'best_year_ema'})
    # Filter symbols whose best year is 2022
    syms_2022 = set(sym_best.loc[sym_best['best_year'] == 2022, 'symbol'])
    # among top_each_year, keep only those symbols with best year 2022 (question asks: highest EMA each year, return only codes whose best year is 2022)
    # This implies: collect symbols that are ever yearly-top AND have best year 2022.
    result_syms = sorted(set(top_each_year.loc[top_each_year['symbol'].isin(syms_2022), 'symbol']))
    out = result_syms

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fgNcjHiX2ZnR3oINNJFhIFOt': 'file_storage/call_fgNcjHiX2ZnR3oINNJFhIFOt.json', 'var_call_Zk5tWT6XM6KdZPOGViHgQCuu': 'file_storage/call_Zk5tWT6XM6KdZPOGViHgQCuu.json'}

exec(code, env_args)
