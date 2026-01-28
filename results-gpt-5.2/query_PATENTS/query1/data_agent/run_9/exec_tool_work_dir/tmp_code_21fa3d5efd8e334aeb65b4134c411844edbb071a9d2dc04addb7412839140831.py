code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

pub = load_records(var_call_fRNHNaqcJIKyaEQyG881jRMs)
lev5 = load_records(var_call_bxob8Cxu7dialuN21YmSHYNh)

lev5_syms = set([r['symbol'] for r in lev5 if r.get('symbol')])

# parse year from filing_date
month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    y = int(m.group(1))
    return y

code_pat = re.compile(r'^[A-HY]\d{2}[A-Z]\d*(?:/\d+)?$')

def to_group_level5(code):
    if not code or not isinstance(code, str):
        return None
    c = code.strip().replace(' ', '')
    # group codes have '/' ; take main group part (before '/')
    if '/' in c:
        c = c.split('/',1)[0]
    # keep only if symbol exists at level 5
    if c in lev5_syms:
        return c
    return None

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    if not isinstance(cpc_list, list):
        continue
    groups = set()
    for ent in cpc_list:
        if isinstance(ent, dict):
            g = to_group_level5(ent.get('code'))
            if g:
                groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')

    # compute EMA per symbol over years
    alpha = 0.2
    result_rows = []
    for sym, gdf in counts.groupby('symbol'):
        gdf2 = gdf.sort_values('year').copy()
        ema = None
        for _, row in gdf2.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            result_rows.append({'symbol': sym, 'year': int(row['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(result_rows)
    # For each year, pick symbol(s) with highest EMA
    top_by_year = ema_df.loc[ema_df.groupby('year')['ema'].transform('max') == ema_df['ema']].copy()
    # For each symbol, its best year is year with max EMA (tie -> latest year)
    best = (ema_df.sort_values(['symbol','ema','year'])
            .groupby('symbol')
            .tail(1)[['symbol','year','ema']]
            .rename(columns={'year':'best_year','ema':'best_ema'}))
    # keep those symbols whose best_year == 2022 and that are top in 2022
    top_2022_syms = set(top_by_year.loc[top_by_year['year']==2022, 'symbol'])
    final_syms = sorted([s for s in best.loc[best['best_year']==2022,'symbol'].tolist() if s in top_2022_syms])
    out = final_syms

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fRNHNaqcJIKyaEQyG881jRMs': 'file_storage/call_fRNHNaqcJIKyaEQyG881jRMs.json', 'var_call_bxob8Cxu7dialuN21YmSHYNh': 'file_storage/call_bxob8Cxu7dialuN21YmSHYNh.json'}

exec(code, env_args)
