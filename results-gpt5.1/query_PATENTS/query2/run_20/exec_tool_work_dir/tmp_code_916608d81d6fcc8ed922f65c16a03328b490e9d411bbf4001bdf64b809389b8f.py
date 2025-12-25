code = """import json, re, pandas as pd
from datetime import datetime

# Load full results if stored as file paths
pub_data = var_call_bxXn7oC8jUw99FWHIXIlUHdO
if isinstance(pub_data, str):
    with open(pub_data, 'r') as f:
        pub_data = json.load(f)

cpc_defs = var_call_fhTet7uhoTnen8it3sA1IBM9
if isinstance(cpc_defs, str):
    with open(cpc_defs, 'r') as f:
        cpc_defs = json.load(f)

# Filter to Germany using Patents_info country code 'DE'
country_pattern = re.compile(r"\bDE\b")
filtered = []
for rec in pub_data:
    info = rec.get('Patents_info','') or ''
    if country_pattern.search(info):
        filtered.append(rec)

# Parse grant year from natural-language grant_date
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(d):
    if not d:
        return None
    # Try to find 4-digit year
    m = re.search(r"(19|20)\d{2}", d)
    if m:
        return int(m.group(0))
    return None

# Extract CPC codes and years
rows = []
for rec in filtered:
    year = parse_year(rec.get('grant_date',''))
    if year is None:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    codes = [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('code')]
    for code in codes:
        # Level-4 group: take main class up to first space or slash? CPCDefinition symbols here are section-class (e.g., A61).
        # We map by the first 3 characters (letter+2 digits) to match cpc_definition symbols like 'A61'.
        m = re.match(r"([A-HY]\d{2})", code)
        if not m:
            continue
        group = m.group(1)
        rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count patents per group per year
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # For EMA, need continuous years per group
    all_years = sorted(counts['year'].unique())
    groups = []
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0)
        # compute EMA with alpha=0.1
        ema = []
        prev = None
        for y in all_years:
            c = sub.loc[y,'count']
            if prev is None:
                prev = c
            else:
                prev = 0.1 * c + 0.9 * prev
            ema.append({'group': g, 'year': y, 'ema': float(prev)})
        groups.extend(ema)
    ema_df = pd.DataFrame(groups)
    # Get max EMA and year per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # Map titles from cpc_defs
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['level'] = defs_df['level'].astype(float)
    defs4 = defs_df[defs_df['level'] == 4.0][['symbol','titleFull']]
    merged = best.merge(defs4, left_on='group', right_on='symbol', how='left')
    merged = merged[['group','titleFull','year','ema']].sort_values('ema', ascending=False)
    # Take top, but user asked for areas with highest EMA each year; interpret as top group overall
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_bxXn7oC8jUw99FWHIXIlUHdO': 'file_storage/call_bxXn7oC8jUw99FWHIXIlUHdO.json', 'var_call_fhTet7uhoTnen8it3sA1IBM9': 'file_storage/call_fhTet7uhoTnen8it3sA1IBM9.json'}

exec(code, env_args)
