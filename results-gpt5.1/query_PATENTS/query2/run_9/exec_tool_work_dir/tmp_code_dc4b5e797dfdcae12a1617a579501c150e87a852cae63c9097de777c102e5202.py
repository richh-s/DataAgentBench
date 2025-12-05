code = """import json, re, pandas as pd

# Load full results for publicationinfo query
data_path = var_call_tVQSFIBgc21wtqWz3AxWacOi
with open(data_path, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info country code 'DE-'
pattern = re.compile(r'\bDE-')
pubs_de = [p for p in pubs if pattern.search(p.get('Patents_info',''))]

# Parse cpc JSON-like strings and explode codes
records = []
for p in pubs_de:
    grant = p.get('grant_date') or ''
    # extract year from grant_date
    m = re.search(r'(19|20)\d{2}', grant)
    year = int(m.group(0)) if m else None
    if not year:
        continue
    cpc_str = p.get('cpc') or '[]'
    try:
        codes = json.loads(cpc_str)
    except Exception:
        continue
    for c in codes:
        code = c.get('code')
        if not code:
            continue
        # derive level 4 group: take leading letter+two digits (section+class) as in cpc_definition level 4 symbols
        m2 = re.match(r'^[A-Z]\d{2}', code)
        if not m2:
            continue
        group = m2.group(0)
        records.append({'year': year, 'group': group})

if not records:
    result = json.dumps([])
else:
    df = pd.DataFrame(records)
    # count filings per year-group
    counts = df.groupby(['group','year']).size().reset_index(name='filings')
    # compute EMA per group across years in ascending order
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.sort_values('year').groupby('group'):
        ema = None
        for _, row in sub.iterrows():
            y = int(row['year'])
            fcount = row['filings']
            ema = fcount if ema is None else alpha*fcount + (1-alpha)*ema
            ema_rows.append({'group': g, 'year': y, 'ema': ema})
    ema_df = pd.DataFrame(ema_rows)
    # for each group, find year with max ema
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_tVQSFIBgc21wtqWz3AxWacOi': 'file_storage/call_tVQSFIBgc21wtqWz3AxWacOi.json', 'var_call_bPm0VplgEig07o5s30skFAn3': 'file_storage/call_bPm0VplgEig07o5s30skFAn3.json'}

exec(code, env_args)
