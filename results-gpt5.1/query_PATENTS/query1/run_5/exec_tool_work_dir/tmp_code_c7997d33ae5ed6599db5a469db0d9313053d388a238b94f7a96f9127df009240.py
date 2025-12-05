code = """import json, pandas as pd
from datetime import datetime

# load full publication data
with open(var_call_Fm51PKqfx0jJcKTq8dARulZo, 'r') as f:
    pubs = json.load(f)

# load full level-5 CPC symbols
with open(var_call_SEFOL42xQFjeCnuIcQYWTyz2, 'r') as f:
    cpc_defs = json.load(f)

level5_symbols = set([r['symbol'] for r in cpc_defs])

records = []
for row in pubs:
    date_str = row['publication_date']
    if not date_str:
        continue
    try:
        dt = datetime.strptime(date_str.replace('st', '').replace('nd', '').replace('rd', '').replace('th', ''), '%b %d, %Y')
    except Exception:
        try:
            dt = datetime.strptime(date_str.replace('st', '').replace('nd', '').replace('rd', '').replace('th', ''), '%B %d, %Y')
        except Exception:
            continue
    year = dt.year
    if year is None:
        continue
    cpc_raw = row['cpc']
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for e in cpc_list:
        code = e.get('code')
        if not code:
            continue
        # normalize code to group level 5: take up to first space or the whole code
        code_norm = code.strip()
        if code_norm in level5_symbols:
            records.append({'year': year, 'symbol': code_norm})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol', 'year']).size().reset_index(name='count')
    # complete years per symbol
    all_years = sorted(counts['year'].unique())
    sy = counts.set_index(['symbol','year'])['count'].unstack(fill_value=0)
    sy = sy.reindex(columns=all_years, fill_value=0)

    alpha = 0.2
    ema = pd.DataFrame(index=sy.index, columns=sy.columns, dtype=float)
    for sym in sy.index:
        prev = None
        for y in all_years:
            x = sy.loc[sym, y]
            if prev is None:
                prev = x
            else:
                prev = alpha * x + (1-alpha) * prev
            ema.loc[sym, y] = prev

    # find best year (max EMA) per symbol
    best_year = ema.idxmax(axis=1)
    best_val = ema.max(axis=1)
    res_df = pd.DataFrame({'symbol': ema.index, 'best_year': best_year, 'best_ema': best_val})

    # keep only best year 2022
    res_2022 = res_df[res_df['best_year'] == 2022]
    # sort descending by best_ema
    res_2022 = res_2022.sort_values('best_ema', ascending=False)
    result = res_2022['symbol'].tolist()

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Fm51PKqfx0jJcKTq8dARulZo': 'file_storage/call_Fm51PKqfx0jJcKTq8dARulZo.json', 'var_call_SEFOL42xQFjeCnuIcQYWTyz2': 'file_storage/call_SEFOL42xQFjeCnuIcQYWTyz2.json'}

exec(code, env_args)
