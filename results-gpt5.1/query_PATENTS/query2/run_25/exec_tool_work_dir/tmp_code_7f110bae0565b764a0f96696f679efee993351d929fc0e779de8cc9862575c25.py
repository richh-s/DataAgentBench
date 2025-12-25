code = """import json, re, pandas as pd
from datetime import datetime

# Load full data from file paths
with open(var_call_LVMpzIRJOBz1gPpc3WT0TtmA, 'r') as f:
    pubs = json.load(f)
with open(var_call_YOeuEkHAQisp0JI81TU3UqD2, 'r') as f:
    cpc_defs = json.load(f)

pubs_df = pd.DataFrame(pubs)

# Filter to Germany by country_code in Patents_info
pubs_df = pubs_df[pubs_df['Patents_info'].str.contains(' country code DE', case=False, na=False)]

# Parse natural-language grant_date to datetime
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_date(text):
    if not isinstance(text, str):
        return None
    text = text.replace('dated ','').replace('on ','')
    # patterns like '3rd August 2021', '21st of September, 2021', 'July 15th, 2019'
    # Remove ordinal suffixes
    text = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', text)
    text = text.replace(' of','').replace(',', '')
    parts = text.split()
    if len(parts) < 3:
        return None
    # try day month year or month day year
    try:
        if parts[0] in months:
            month = months[parts[0]]; day = int(parts[1]); year = int(parts[2])
        else:
            day = int(parts[0]); month = months.get(parts[1], None); year = int(parts[2])
        if not month:
            return None
        return datetime(year, month, day)
    except Exception:
        return None

pubs_df['grant_dt'] = pubs_df['grant_date'].apply(parse_date)

# Filter granted in second half of 2019 (Jul 1 - Dec 31, 2019)
start = datetime(2019,7,1)
end = datetime(2019,12,31)
mask = pubs_df['grant_dt'].between(start, end, inclusive='both')
subset = pubs_df[mask].copy()

# Extract CPC codes
records = []
for _, row in subset.iterrows():
    cpc_raw = row.get('cpc')
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        codes = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in codes:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # level-4 group: take first 3 characters of main section? But CPC group: first 4? We'll use first 3 (like B29) then join with defs
        group = re.match(r'^[A-Z]\d\d', code)
        if not group:
            continue
        group_code = group.group(0)
        records.append({'group_code': group_code, 'year': row['grant_dt'].year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per group per year
    counts = df.groupby(['group_code','year']).size().reset_index(name='count')

    # Compute EMA (alpha=0.1) over years for each group
    alpha = 0.1
    ema_rows = []
    for group, grp in counts.groupby('group_code'):
        grp_sorted = grp.sort_values('year')
        ema = None
        for _, r in grp_sorted.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha)*ema
            ema_rows.append({'group_code': group, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    # For each group, find year with highest EMA
    idx = ema_df.groupby('group_code')['ema'].idxmax()
    best = ema_df.loc[idx].copy()

    # Map to CPC definitions (level 4)
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df[defs_df['level'].astype(float) == 4.0][['symbol','titleFull']]
    merged = best.merge(defs_df, left_on='group_code', right_on='symbol', how='left')

    merged = merged[['group_code','titleFull','year','ema']].sort_values('ema', ascending=False)
    result = merged.to_dict(orient='records')

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_LVMpzIRJOBz1gPpc3WT0TtmA': 'file_storage/call_LVMpzIRJOBz1gPpc3WT0TtmA.json', 'var_call_YOeuEkHAQisp0JI81TU3UqD2': 'file_storage/call_YOeuEkHAQisp0JI81TU3UqD2.json'}

exec(code, env_args)
