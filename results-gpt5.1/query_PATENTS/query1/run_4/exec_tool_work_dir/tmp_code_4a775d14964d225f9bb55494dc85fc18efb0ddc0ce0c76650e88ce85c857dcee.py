code = """import json, pandas as pd, re, datetime as dt

with open(var_call_jLLNfyaKn33j8Dco9RglwGDv, 'r') as f:
    level5_defs = json.load(f)
with open(var_call_krZS9oman9pPad7qXewCAzqz, 'r') as f:
    pub_rows = json.load(f)

level5_symbols = set(r['symbol'] for r in level5_defs)

rows = []
for r in pub_rows:
    cpc_raw = r.get('cpc')
    pub_date_raw = r.get('publication_date')
    if not cpc_raw or not pub_date_raw:
        continue
    s = pub_date_raw.replace('st','').replace('nd','').replace('rd','').replace('th','')
    parsed = None
    for fmt in ('%b %d, %Y','%B %d, %Y'):
        try:
            parsed = dt.datetime.strptime(s, fmt)
            break
        except Exception:
            continue
    if not parsed:
        continue
    year = parsed.year
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for e in cpc_list:
        code = e.get('code')
        if not code:
            continue
        m = re.match(r'^[A-Z]\d\d[A-Z]\d+', code)
        if m:
            grp = m.group(0)
        else:
            m2 = re.match(r'^[A-Z]\d\d[A-Z]', code)
            grp = m2.group(0) if m2 else code
        if grp in level5_symbols:
            rows.append({'year': year, 'group': grp})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    alpha = 0.2
    def compute_ema(g):
        g = g.sort_values('year')
        ema = None
        emas = []
        for _, row in g.iterrows():
            c = row['count']
            ema = c if ema is None else alpha * c + (1-alpha) * ema
            emas.append(ema)
        g = g.copy()
        g['ema'] = emas
        return g
    counts = counts.groupby('group', group_keys=False).apply(compute_ema)
    idx = counts.groupby('group')['ema'].idxmax()
    best = counts.loc[idx, ['group','year','ema']]
    best2022 = best[best['year']==2022]
    result = sorted(best2022['group'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jLLNfyaKn33j8Dco9RglwGDv': 'file_storage/call_jLLNfyaKn33j8Dco9RglwGDv.json', 'var_call_krZS9oman9pPad7qXewCAzqz': 'file_storage/call_krZS9oman9pPad7qXewCAzqz.json', 'var_call_kO2eDFAlx1UZpfpsd9LpVxWB': [{'?column?': '1'}]}

exec(code, env_args)
