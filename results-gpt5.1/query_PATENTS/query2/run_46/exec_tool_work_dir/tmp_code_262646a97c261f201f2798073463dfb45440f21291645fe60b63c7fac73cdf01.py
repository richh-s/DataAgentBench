code = """import json, re, pandas as pd
from datetime import datetime

path_pubs = var_call_6lQKo9EgQXpgAhmiCE6jXIC0
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

# Filter German patents via country_code in Patents_info
pat_de = []
for r in pubs:
    info = r.get('Patents_info') or ''
    m = re.search(r'\b([A-Z]{2}) patent', info)
    if not m:
        continue
    if m.group(1) != 'DE':
        continue
    pat_de.append(r)

# Parse grant_date natural language and filter to second half 2019
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}

selected = []
for r in pat_de:
    gd = (r.get('grant_date') or '').strip()
    if not gd:
        continue
    gd_clean = gd.replace('dated ','').replace('of ','')
    gd_clean = re.sub(r'(st|nd|rd|th)', '', gd_clean)
    m = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', gd_clean)
    if not m:
        continue
    d, mon, y = int(m.group(1)), m.group(2), int(m.group(3))
    if mon not in months:
        continue
    dt = datetime(y, months[mon], d)
    if dt.year == 2019 and dt.month >= 7:
        r2 = dict(r)
        r2['grant_year'] = dt.year
        selected.append(r2)

# Extract CPC symbols (full code) and aggregate counts per year and CPC
rows = []
for r in selected:
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        # level 4 group: section+class+subclass, i.e., first 3 chars until non-letter/number? take first 3 for simplicity
        grp = code[:3]
        rows.append({'year': r['grant_year'], 'group': grp})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # build full time series per group from min to max year
    all_years = sorted(counts['year'].unique())
    records = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0)
        ema = []
        prev = None
        for y in all_years:
            x = sub.loc[y, 'count']
            prev = x if prev is None else alpha*x + (1-alpha)*prev
            ema.append({'group': g, 'year': y, 'ema': prev})
        # find best year
        best = max(ema, key=lambda r:r['ema'])
        records.append(best)

    ema_df = pd.DataFrame(records)

# load CPC level 4 definitions
path_def = var_call_XPIvN1v7EDza6IHRUK25OSph
with open(path_def, 'r') as f:
    defs = json.load(f)

def_df = pd.DataFrame(defs)[['symbol','titleFull']]

if rows:
    merged = ema_df.merge(def_df, left_on='group', right_on='symbol', how='left')
    merged = merged.sort_values('ema', ascending=False).head(20)
    out = merged[['group','titleFull','year','ema']].rename(columns={'year':'best_year'}).to_dict(orient='records')
else:
    out = []

res = json.dumps(out)
print('__RESULT__:')
print(res)"""

env_args = {'var_call_6lQKo9EgQXpgAhmiCE6jXIC0': 'file_storage/call_6lQKo9EgQXpgAhmiCE6jXIC0.json', 'var_call_XPIvN1v7EDza6IHRUK25OSph': 'file_storage/call_XPIvN1v7EDza6IHRUK25OSph.json'}

exec(code, env_args)
