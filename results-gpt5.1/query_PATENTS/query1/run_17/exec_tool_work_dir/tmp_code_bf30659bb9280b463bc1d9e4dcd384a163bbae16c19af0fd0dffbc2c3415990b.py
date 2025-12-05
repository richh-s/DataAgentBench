code = """import json, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_qgqDs0gu0pcwZOACJWIDU0ah, 'r') as f:
    pub_data = json.load(f)

# Build dataframe with year and codes
rows = []
for rec in pub_data:
    date_str = rec.get('publication_date')
    cpc_str = rec.get('cpc')
    if not date_str or not cpc_str:
        continue
    try:
        year = datetime.strptime(date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpc_str)]
    except Exception:
        continue
    for code in codes:
        rows.append({'year': year, 'code': code})

if not rows:
    result = json.dumps([])
else:
    df = pd.DataFrame(rows)
    # Filter years up to 2022
    df = df[df['year'] <= 2022]
    # Count filings per code-year
    counts = df.groupby(['code','year']).size().reset_index(name='count')
    # Ensure full year range per code
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    codes = counts['code'].unique()
    idx = pd.MultiIndex.from_product([codes, all_years], names=['code','year'])
    counts_full = counts.set_index(['code','year']).reindex(idx, fill_value=0).reset_index()
    # Compute EMA per code sorted by year
    alpha = 0.2
    emas = []
    for code, grp in counts_full.groupby('code'):
        grp = grp.sort_values('year')
        ema_vals = []
        ema = None
        for c in grp['count']:
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_vals.append(ema)
        grp = grp.copy()
        grp['ema'] = ema_vals
        emas.append(grp)
    emas_df = pd.concat(emas, ignore_index=True)
    # For each code, find year with max EMA and that EMA value
    best = emas_df.loc[emas_df.groupby('code')['ema'].idxmax()][['code','year','ema']]
    # Keep only codes whose best year is 2022
    best_2022 = best[best['year'] == 2022]
    codes_2022 = best_2022['code'].tolist()

    # Now load level-5 CPC symbols
    with open(var_call_v5lkZzO6tWkJEvwfE6Fmp87d, 'r') as f:
        cpc_defs = json.load(f)
    lvl5 = pd.DataFrame(cpc_defs)
    lvl5_syms = set(lvl5['symbol'].astype(str).tolist())

    lvl5_codes_2022 = sorted([c for c in codes_2022 if c.split('/')[0] in lvl5_syms])

    result = json.dumps(lvl5_codes_2022)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_qgqDs0gu0pcwZOACJWIDU0ah': 'file_storage/call_qgqDs0gu0pcwZOACJWIDU0ah.json', 'var_call_v5lkZzO6tWkJEvwfE6Fmp87d': 'file_storage/call_v5lkZzO6tWkJEvwfE6Fmp87d.json'}

exec(code, env_args)
