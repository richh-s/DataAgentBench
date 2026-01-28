code = """import json, re
import pandas as pd

# Load publication rows (may be file path)
rows_src = var_call_Mw1YxHWA0dw2UnO4yk1vNwzd
if isinstance(rows_src, str):
    with open(rows_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = rows_src

level5_src = var_call_GiEcfwFSlfDCq73qndlcA9mn
level5 = set([r['symbol'] for r in level5_src]) if isinstance(level5_src, list) else set()
# If no level5 returned (unexpected), infer level5 as codes containing '/' and having >=5 hierarchy? fallback keep all

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str: return []
    try:
        lst = json.loads(cpc_str)
        codes = []
        for item in lst:
            c = item.get('code')
            if c: codes.append(c)
        return codes
    except Exception:
        # very simple regex fallback
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+\/[^\"]+)"', cpc_str)

records = []
for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None: continue
    codes = extract_codes(r.get('cpc'))
    if not codes: continue
    for c in codes:
        if level5 and c not in level5:
            continue
        records.append((c,y))

df = pd.DataFrame(records, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')

    alpha = 0.2
    # compute EMA per symbol over sorted years
    def ema_for_group(g):
        g = g.sort_values('year')
        ema = None
        emas=[]
        for v in g['filings'].tolist():
            ema = v if ema is None else alpha*v + (1-alpha)*ema
            emas.append(ema)
        g = g.copy()
        g['ema']=emas
        return g

    counts_ema = counts.groupby('symbol', group_keys=False).apply(ema_for_group)

    # For each year, find symbol(s) with max EMA
    year_max = counts_ema.groupby('year')['ema'].transform('max')
    top_each_year = counts_ema[counts_ema['ema'] == year_max][['year','symbol','ema']]

    # Determine best year per symbol (year where its ema is maximum; if tie choose latest)
    def best_year(g):
        m = g['ema'].max()
        gg = g[g['ema']==m]
        return int(gg['year'].max())
    best = counts_ema.groupby('symbol').apply(best_year).reset_index(name='best_year')

    # Among symbols that are top in at least one year AND best_year==2022, return unique symbols
    top_syms = set(top_each_year['symbol'].unique())
    res = best[(best['best_year']==2022) & (best['symbol'].isin(top_syms))]['symbol'].sort_values().tolist()
    out = res

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Mw1YxHWA0dw2UnO4yk1vNwzd': 'file_storage/call_Mw1YxHWA0dw2UnO4yk1vNwzd.json', 'var_call_GiEcfwFSlfDCq73qndlcA9mn': []}

exec(code, env_args)
