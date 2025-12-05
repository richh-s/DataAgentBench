code = """import json, pandas as pd, datetime as dt

# Load full publication data
path_pub = var_call_6APh6Mq7rjBxRWXMUCAtS3dQ
with open(path_pub, 'r') as f:
    pub = json.load(f)

# Load level-5 CPC symbols
path_cpc = var_call_qd4GcvnfUjnVSNEERlClZ2vN
with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)

level5 = {r['symbol'] for r in cpc_defs}

rows = []
for r in pub:
    date_str = r.get('publication_date')
    cpc_raw = r.get('cpc')
    if not date_str or not cpc_raw:
        continue
    try:
        # parse like 'Aug 3rd, 2021'
        date_clean = date_str.replace('st','').replace('nd','').replace('rd','').replace('th','')
        d = dt.datetime.strptime(date_clean, '%b %d, %Y')
    except Exception:
        try:
            d = dt.datetime.strptime(date_clean, '%B %d, %Y')
        except Exception:
            continue
    year = d.year
    if year < 2000 or year > 2022:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # Map to level-5 "group" code: first 4 characters (section+class+subclass+main-group-digit) as per cpc_definition symbols
        group = code[:4]
        if group in level5:
            rows.append({'year': year, 'group': group})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # compute EMA per group sorted by year
    alpha = 0.2
    ema_records = []
    for g, sub in counts.sort_values('year').groupby('group'):
        ema = None
        for _, row in sub.iterrows():
            y = int(row['year'])
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'group': g, 'year': y, 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)
    # for each group, find year of max ema
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # filter for best year 2022
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['group'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_6APh6Mq7rjBxRWXMUCAtS3dQ': 'file_storage/call_6APh6Mq7rjBxRWXMUCAtS3dQ.json', 'var_call_qd4GcvnfUjnVSNEERlClZ2vN': 'file_storage/call_qd4GcvnfUjnVSNEERlClZ2vN.json'}

exec(code, env_args)
