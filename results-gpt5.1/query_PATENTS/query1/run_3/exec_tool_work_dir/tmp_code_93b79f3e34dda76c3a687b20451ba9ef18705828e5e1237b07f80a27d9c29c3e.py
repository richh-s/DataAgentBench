code = """import json, pandas as pd, datetime as dt

# Load full results from files
with open(var_call_fXFdMdABgB5ge6D6lEOMfKFO, 'r') as f:
    cpc_defs = json.load(f)
with open(var_call_aA99C71opelSdfTtmRHHmTwF, 'r') as f:
    pubs = json.load(f)

# Get set of level-5 CPC symbols
level5 = {r['symbol'] for r in cpc_defs}

# Helper to parse publication year
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(date_str):
    if not date_str:
        return None
    try:
        parts = date_str.replace(',', '').split()
        mon = parts[0][:3]
        year = int(parts[-1])
        return year
    except Exception:
        return None

records = []
for row in pubs:
    year = parse_year(row['publication_date'])
    if year is None:
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for e in cpc_list:
        code = e.get('code')
        if not code:
            continue
        symbol = code.split()[0]
        # Normalize to class/group level without subgroup (e.g., H01M10/0565 -> H01M10/056)
        if '/' in symbol:
            main, sub = symbol.split('/')
            if len(sub) > 3:
                sub = sub[:3]
            symbol_norm = main + '/' + sub
        else:
            symbol_norm = symbol
        if symbol_norm in level5:
            records.append({'symbol': symbol_norm, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per symbol-year
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # Ensure continuous years per symbol within global min/max
    all_years = sorted(counts['year'].unique())
    sym_list = counts['symbol'].unique()
    full_idx = pd.MultiIndex.from_product([sym_list, all_years], names=['symbol','year'])
    counts = counts.set_index(['symbol','year']).reindex(full_idx, fill_value=0).reset_index()

    alpha = 0.2
    ema_rows = []
    for sym in sym_list:
        sub = counts[counts['symbol']==sym].sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'symbol': sym, 'year': r['year'], 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)
    # For each symbol, find year with max EMA
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # Keep only those whose best year is 2022
    best2022 = best[best['year']==2022]
    # Return sorted list of symbols
    result = sorted(best2022['symbol'].tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fXFdMdABgB5ge6D6lEOMfKFO': 'file_storage/call_fXFdMdABgB5ge6D6lEOMfKFO.json', 'var_call_aA99C71opelSdfTtmRHHmTwF': 'file_storage/call_aA99C71opelSdfTtmRHHmTwF.json'}

exec(code, env_args)
