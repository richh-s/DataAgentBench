code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

recs = load_records(var_call_26NxjiFPE4G45QY8BaciXuQ1)

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

rows = []
for r in recs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    codes = []
    for e in cpc_list if isinstance(cpc_list, list) else []:
        code = e.get('code') if isinstance(e, dict) else None
        if not code:
            continue
        # normalize: remove spaces
        code = code.strip()
        # keep CPC group code at level 5: heuristic = contains '/' and has exactly one slash with subgroup digits
        if '/' not in code:
            continue
        # exclude Y, etc? keep all
        codes.append(code)
    # unique per patent-year to avoid duplicates within same record
    for code in set(codes):
        rows.append((y, code))

df = pd.DataFrame(rows, columns=['year','symbol'])
# counts per year-symbol
counts = df.value_counts(['symbol','year']).reset_index(name='filings')
# compute EMA per symbol over years
alpha = 0.2
emas = []
for sym, g in counts.sort_values('year').groupby('symbol'):
    years = g['year'].tolist()
    vals = g['filings'].tolist()
    ema = None
    for v in vals:
        ema = v if ema is None else alpha*v + (1-alpha)*ema
    # also need best year by ema each year, so compute series
    ema_series = []
    ema = None
    for y,v in zip(years, vals):
        ema = v if ema is None else alpha*v + (1-alpha)*ema
        ema_series.append((sym,y,ema))
    emas.extend(ema_series)

ema_df = pd.DataFrame(emas, columns=['symbol','year','ema'])
# for each year, pick symbol(s) with max ema
max_by_year = ema_df.loc[ema_df.groupby('year')['ema'].transform('max') == ema_df['ema']]
# for each symbol, find its best year (year where its ema is max for that symbol)
best_year_for_symbol = ema_df.loc[ema_df.groupby('symbol')['ema'].transform('max') == ema_df['ema']]
# if ties, take latest year
best_year_for_symbol = best_year_for_symbol.sort_values(['symbol','ema','year']).groupby('symbol').tail(1)
# symbols that are top-of-year in their best year and best year is 2022
syms_best_2022 = set(best_year_for_symbol.loc[best_year_for_symbol['year']==2022,'symbol'])
# But also require they are 'technology areas with the highest EMA of filings each year' => must be among max_by_year for 2022
max_2022_syms = set(max_by_year.loc[max_by_year['year']==2022,'symbol'])
result_syms = sorted(syms_best_2022.intersection(max_2022_syms))

out = json.dumps(result_syms)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Wr5AkkKgRQFg3IXXi6gFR1iQ': ['publicationinfo'], 'var_call_mazQx8KWl35bSq2GtQFGz43r': ['cpc_definition'], 'var_call_26NxjiFPE4G45QY8BaciXuQ1': 'file_storage/call_26NxjiFPE4G45QY8BaciXuQ1.json'}

exec(code, env_args)
