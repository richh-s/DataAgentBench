code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication query result
path = var_call_OE8GeDdgCCxwiYDzBSPeJ0QT
with open(path, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using country code "DE" in Patents_info
de_pubs = [p for p in pubs if ' DE ' in p['Patents_info'] or ' DE-' in p['Patents_info'] or ' DE,' in p['Patents_info']]

# Parse grant year (already 2019 but keep structure) and build yearly counts per CPC group (level 4 approximated as first 4 chars of code before slash)
records = []
for p in de_pubs:
    gd = p['grant_date']
    # map natural language year
    m = re.search(r'(20\d{2})', gd)
    if not m:
        continue
    year = int(m.group(1))
    # parse CPC JSON-like string
    try:
        cpc_list = json.loads(p['cpc'])
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        base = code.split('/')[0]
        group4 = base[:4]
        records.append({'year': year, 'group4': group4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # yearly counts per group4
    yearly = df.groupby(['group4','year']).size().reset_index(name='count')
    # build EMA over years per group using alpha=0.1
    alpha = 0.1
    ema_rows = []
    for g, sub in yearly.groupby('group4'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            y = row['year']; c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'group4': g, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # best year (max EMA) per group
    idx = ema_df.groupby('group4')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OE8GeDdgCCxwiYDzBSPeJ0QT': 'file_storage/call_OE8GeDdgCCxwiYDzBSPeJ0QT.json', 'var_call_RQMkdOxbboHOoG5OYvHvc0bt': 'file_storage/call_RQMkdOxbboHOoG5OYvHvc0bt.json'}

exec(code, env_args)
