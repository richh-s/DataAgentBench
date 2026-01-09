code = """import json, re
import pandas as pd

rows_src = var_call_Mw1YxHWA0dw2UnO4yk1vNwzd
if isinstance(rows_src, str):
    with open(rows_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = rows_src

# Precompiled regex for code values
code_re = re.compile(r'"code"\s*:\s*"([^\"]+)"')
year_re = re.compile(r'(19|20)\d{2}')

def parse_year(s):
    if not s: return None
    m = year_re.search(s)
    return int(m.group(0)) if m else None

def iter_codes_fast(cpc_str):
    if not cpc_str: return
    # Try json loads quickly for small strings, else regex
    if len(cpc_str) < 50000:
        try:
            lst = json.loads(cpc_str)
            for it in lst:
                c = it.get('code')
                if c: yield c
            return
        except Exception:
            pass
    for m in code_re.finditer(cpc_str):
        yield m.group(1)

# Aggregate counts per (symbol,year) without exploding fully
from collections import defaultdict
counts = defaultdict(int)

for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None: continue
    cpc_str = r.get('cpc')
    if not cpc_str: continue
    # count each occurrence
    for c in iter_codes_fast(cpc_str):
        counts[(c,y)] += 1

if not counts:
    out = []
else:
    df = pd.DataFrame([(k[0],k[1],v) for k,v in counts.items()], columns=['symbol','year','filings'])

    alpha = 0.2
    df = df.sort_values(['symbol','year'])

    # compute EMA with groupby + manual loop over values for speed
    emas = []
    prev_sym = None
    ema = None
    for sym, year, filings in df[['symbol','year','filings']].itertuples(index=False, name=None):
        if sym != prev_sym:
            ema = None
            prev_sym = sym
        ema = filings if ema is None else alpha*filings + (1-alpha)*ema
        emas.append(ema)
    df['ema'] = emas

    # top per year
    max_by_year = df.groupby('year')['ema'].max().to_dict()
    top_syms = set(df.loc[df.apply(lambda r: r['ema']==max_by_year.get(r['year']), axis=1), 'symbol'])

    # best year per symbol (max ema, tie -> latest year)
    g = df.groupby('symbol')
    best_year = {}
    for sym, sub in g:
        m = sub['ema'].max()
        by = int(sub.loc[sub['ema']==m, 'year'].max())
        best_year[sym]=by

    out = sorted([s for s in top_syms if best_year.get(s)==2022])

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Mw1YxHWA0dw2UnO4yk1vNwzd': 'file_storage/call_Mw1YxHWA0dw2UnO4yk1vNwzd.json', 'var_call_GiEcfwFSlfDCq73qndlcA9mn': []}

exec(code, env_args)
