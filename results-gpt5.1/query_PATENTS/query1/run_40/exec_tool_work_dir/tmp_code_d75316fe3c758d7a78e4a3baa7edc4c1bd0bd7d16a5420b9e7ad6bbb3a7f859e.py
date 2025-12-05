code = """import json, pandas as pd, re, datetime

# Load full data from files
with open(var_call_chcVzP5GNBBTj7rPRnoOJl1G, 'r') as f:
    level5 = json.load(f)
with open(var_call_kCN9PnKKzD9EzmV6y01fZPe4, 'r') as f:
    pubs = json.load(f)

level5_codes = set(r['symbol'] for r in level5)

rows = []
for r in pubs:
    date_str = r['publication_date']
    if not date_str:
        continue
    try:
        date_parsed = datetime.datetime.strptime(date_str, '%b %dth, %Y')
    except ValueError:
        try:
            date_parsed = datetime.datetime.strptime(date_str, '%b %dst, %Y')
        except ValueError:
            try:
                date_parsed = datetime.datetime.strptime(date_str, '%b %dnd, %Y')
            except ValueError:
                try:
                    date_parsed = datetime.datetime.strptime(date_str, '%b %drd, %Y')
                except ValueError:
                    continue
    year = date_parsed.year
    if year < 2000 or year > 2022:
        continue
    cpc_raw = r['cpc']
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        group = code.split('/')[0]
        if group in level5_codes:
            rows.append({'year': year, 'group': group})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # build complete year range per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    groups = counts['group'].unique()
    records = []
    alpha = 0.2
    for g in groups:
        sub = counts[counts['group']==g].set_index('year')['count']
        ema_prev = None
        for y in all_years:
            c = sub.get(y, 0)
            if ema_prev is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema_prev
            records.append({'group': g, 'year': y, 'ema': float(ema)})
            ema_prev = ema
    ema_df = pd.DataFrame(records)
    # find best year per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    res_2022 = best[best['year']==2022]['group'].sort_values().tolist()
    result = res_2022

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_chcVzP5GNBBTj7rPRnoOJl1G': 'file_storage/call_chcVzP5GNBBTj7rPRnoOJl1G.json', 'var_call_kCN9PnKKzD9EzmV6y01fZPe4': 'file_storage/call_kCN9PnKKzD9EzmV6y01fZPe4.json'}

exec(code, env_args)
