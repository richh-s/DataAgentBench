code = """import json, pandas as pd, datetime as dt

# Load full results if stored as file paths
from pathlib import Path

# Handle cpc_definition symbols (level 5)
path_defs = Path(var_call_y16mH7P8X3KlDfkzEsRprvOe)
with open(path_defs, 'r') as f:
    defs = json.load(f)
level5_symbols = set(d['symbol'] for d in defs)

# Handle publication data
path_pubs = Path(var_call_wgHuUHn03oc82TUXtBia4Oz9)
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

records = []
for row in pubs:
    pub_date = row.get('publication_date')
    cpc_raw = row.get('cpc')
    if not pub_date or not cpc_raw:
        continue
    try:
        year = dt.datetime.strptime(pub_date, '%b %dth, %Y').year
    except Exception:
        try:
            year = dt.datetime.strptime(pub_date, '%B %dth, %Y').year
        except Exception:
            # Try generic parse by removing suffixes
            try:
                parts = pub_date.replace('st','').replace('nd','').replace('rd','').replace('th','')
                year = dt.datetime.strptime(parts, '%b %d, %Y').year
            except Exception:
                try:
                    year = dt.datetime.strptime(parts, '%B %d, %Y').year
                except Exception:
                    continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    codes = {entry.get('code') for entry in cpc_list if isinstance(entry, dict) and entry.get('code')}
    for code in codes:
        # normalize to level 5 group code: use part before last '/'
        if '/' in code:
            group = code.split('/')[0]
        else:
            group = code
        if group in level5_symbols:
            records.append({'year': year, 'group': group})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # compute EMA per group, per year sorted
    alpha = 0.2
    ema_rows = []
    for grp, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'group': grp, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    # For each year, find groups with highest EMA
    best_per_year = ema_df.loc[ema_df.groupby('year')['ema'].idxmax()].copy()

    # Filter to best year 2022 and return group codes
    best_2022 = best_per_year[best_per_year['year']==2022]['group'].unique().tolist()
    result = best_2022

import json
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_y16mH7P8X3KlDfkzEsRprvOe': 'file_storage/call_y16mH7P8X3KlDfkzEsRprvOe.json', 'var_call_wgHuUHn03oc82TUXtBia4Oz9': 'file_storage/call_wgHuUHn03oc82TUXtBia4Oz9.json'}

exec(code, env_args)
