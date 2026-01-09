code = """import json, re
import pandas as pd

# Load publication rows (may be file path)
pub_src = var_call_9dw4jsqiFV2GiADr7jBvxzfe
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

lvl5_src = var_call_ehWODgDh6VTohCb03DTxka8K
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol') is not None)

month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for it in data:
            c = it.get('code') if isinstance(it, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for codes like H01M10/0565
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+(?:/\d+)?)"', cpc_str)

def normalize_symbol(code):
    # remove spaces
    code = code.strip().replace(' ', '')
    # take part before optional trailing annotations
    return code

rows = []
for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # count one filing per (year, symbol) per publication to avoid duplicates within same record
    sym_set = set()
    for c in codes:
        sym = normalize_symbol(c)
        if sym in lvl5_set:
            sym_set.add(sym)
    for sym in sym_set:
        rows.append((sym, y, 1))

df = pd.DataFrame(rows, columns=['symbol','year','cnt'])
if df.empty:
    out = []
else:
    annual = df.groupby(['symbol','year'], as_index=False)['cnt'].sum()

    alpha = 0.2
    def compute_ema(g):
        g = g.sort_values('year')
        ema = []
        prev = None
        for v in g['cnt'].tolist():
            prev = v if prev is None else (alpha*v + (1-alpha)*prev)
            ema.append(prev)
        g = g.copy()
        g['ema'] = ema
        return g

    annual_ema = annual.groupby('symbol', group_keys=False).apply(compute_ema)

    # for each year, find symbol(s) with highest ema
    idx = annual_ema.groupby('year')['ema'].transform('max') == annual_ema['ema']
    top_by_year = annual_ema[idx].copy()

    # best year per symbol (year where ema max; if ties choose latest year)
    sym_max = annual_ema.groupby('symbol')['ema'].transform('max')
    best = annual_ema[annual_ema['ema'] == sym_max].copy()
    best_year = best.groupby('symbol')['year'].max().reset_index(name='best_year')

    top_by_year = top_by_year.merge(best_year, on='symbol', how='left')
    # keep only whose best year is 2022
    res = top_by_year[top_by_year['best_year'] == 2022]

    out = sorted(res['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9dw4jsqiFV2GiADr7jBvxzfe': 'file_storage/call_9dw4jsqiFV2GiADr7jBvxzfe.json', 'var_call_ehWODgDh6VTohCb03DTxka8K': 'file_storage/call_ehWODgDh6VTohCb03DTxka8K.json'}

exec(code, env_args)
