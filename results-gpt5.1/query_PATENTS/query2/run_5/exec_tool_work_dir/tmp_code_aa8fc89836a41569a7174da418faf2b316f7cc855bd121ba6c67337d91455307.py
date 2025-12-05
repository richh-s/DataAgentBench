code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_YuWLwZPaOOAsTRTZactsHp86, 'r') as f:
    pubs = json.load(f)

# Filter to German patents via country code in Patents_info (pattern ' DE-')
pat_de = []
for r in pubs:
    info = r.get('Patents_info') or ''
    if ' DE-' not in info:
        continue
    gd = r.get('grant_date') or ''
    # parse year and month to filter 2nd half 2019
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{4})', gd)
    if not m:
        m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)[^0-9]*(\d{4})', gd)
        if not m:
            continue
        day = 1
        month_name, year = m.groups()
    else:
        day, month_name, year = m.groups()
        day = int(day)
    months = {m: i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}
    if isinstance(month_name, str):
        month = months.get(month_name.strip(','), None)
    else:
        month = None
    year = int(year)
    if year == 2019 and month and month >= 7:
        pat_de.append({'Patents_info': info, 'grant_date': gd, 'cpc': r.get('cpc')})

# Extract CPC codes and build year counts of filings per CPC level-4 group
# Need filing year; approximate from 'application no. DE-YYYY' pattern
records = []
for r in pat_de:
    info = r['Patents_info']
    # extract filing year from application pattern like DE-2018123456-A
    m = re.search(r'DE-(\d{4})', info)
    if not m:
        continue
    filing_year = int(m.group(1))
    cpc_str = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        # level-4 group approximated as first 3 characters (section+class) like "C01", "H01" etc.
        grp = code[:3]
        records.append({'group': grp, 'year': filing_year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # For each group, compute EMA over years sorted ascending, alpha=0.1
    out_rows = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        best_ema = None
        best_year = None
        for _, row in sub.iterrows():
            y, c = row['year'], row['count']
            if ema is None:
                ema = c
            else:
                ema = 0.1*c + 0.9*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        out_rows.append({'group': g, 'best_year': int(best_year), 'best_ema': float(best_ema)})
    out_df = pd.DataFrame(out_rows).sort_values('best_ema', ascending=False)
    top_groups = out_df.head(50)  # keep some top for joining titles
    result = top_groups.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YuWLwZPaOOAsTRTZactsHp86': 'file_storage/call_YuWLwZPaOOAsTRTZactsHp86.json', 'var_call_lCy1gnBmr0jviCz4yLbfPX5O': 'file_storage/call_lCy1gnBmr0jviCz4yLbfPX5O.json'}

exec(code, env_args)
