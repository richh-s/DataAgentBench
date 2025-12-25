code = """import json, re, pandas as pd
from datetime import datetime

# Load publication data
path_pub = var_call_pJElfgQTTH7bcGaPvoq90XXA
with open(path_pub, 'r') as f:
    pub_data = json.load(f)

# Filter to Germany using country_code DE in Patents_info
de_pubs = []
for row in pub_data:
    info = row.get('Patents_info','') or ''
    if ' DE ' in info or ' DE-' in info or 'from DE,' in info or 'In DE,' in info or 'the DE application' in info:
        de_pubs.append(row)

# Parse grant year and CPC codes
records = []
for row in de_pubs:
    gd = row.get('grant_date') or ''
    # extract year as 4-digit 20..
    m = re.search(r'(20\d{2})', gd)
    if not m:
        continue
    year = int(m.group(1))
    cpc_raw = row.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # level-4 group: first 3 characters (section+class+subclass?) or up to first space/"/"; but we need CPC group code at level 4.
        # Approximate by taking first 3 characters (letter+2 digits)
        m2 = re.match(r'([A-HY][0-9]{2})', code)
        if not m2:
            continue
        group = m2.group(1)
        records.append({'year': year, 'group': group})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # build complete year range per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    groups = []
    best_rows = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0)
        ema = []
        prev = None
        for y in all_years:
            x = sub.loc[y, 'count']
            if prev is None:
                prev = x
            else:
                prev = alpha * x + (1-alpha) * prev
            ema.append({'year': y, 'ema': float(prev)})
        ema_df = pd.DataFrame(ema)
        idx = ema_df['ema'].idxmax()
        best = ema_df.loc[idx]
        best_rows.append({'group': g, 'best_year': int(best['year']), 'max_ema': float(best['ema'])})

    best_df = pd.DataFrame(best_rows)
    # keep top N groups with highest max_ema
    top = best_df.sort_values('max_ema', ascending=False).head(20)
    result = top.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pJElfgQTTH7bcGaPvoq90XXA': 'file_storage/call_pJElfgQTTH7bcGaPvoq90XXA.json', 'var_call_IrVqEbdgOY8EMxXqILKIqbJw': 'file_storage/call_IrVqEbdgOY8EMxXqILKIqbJw.json'}

exec(code, env_args)
