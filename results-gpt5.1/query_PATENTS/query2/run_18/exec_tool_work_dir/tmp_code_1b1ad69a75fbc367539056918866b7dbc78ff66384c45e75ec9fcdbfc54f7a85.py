code = """import json, re, pandas as pd
from datetime import datetime

# Load full patent data from file
file_path = var_call_XHN3C09VrOxSh9J15QGQGzkK
with open(file_path, 'r') as f:
    patent_data = json.load(f)

# Load CPC level 4 definitions
file_path_def = var_call_llat10MKWWFRRQWVHlD5bof8
with open(file_path_def, 'r') as f:
    cpc_defs = json.load(f)

# Helper to extract country code (assume pattern "The XX patent" or "In XX, the application" or "Application (ID EP-...) from EP")
country_pattern = re.compile(r"\b(?:The|the)\s+([A-Z]{2})\s+patent|In\s+([A-Z]{2}),\s+the application|from\s+([A-Z]{2}),", re.IGNORECASE)

def get_country(info):
    m = country_pattern.search(info or '')
    if not m:
        return None
    for g in m.groups():
        if g and len(g) == 2:
            return g.upper()
    return None

# Filter to Germany (DE)
patent_de = [r for r in patent_data if get_country(r.get('Patents_info','')) == 'DE']

# Parse grant year from natural language grant_date
month_map = {m: i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

ord_pattern = re.compile(r"(\d+)(st|nd|rd|th)?")


def parse_date(s):
    if not s:
        return None
    s = s.replace(',', '')
    # Try patterns like "July 8th 2019"
    parts = s.split()
    # Look for year as 4-digit
    year = None
    for p in parts:
        if re.fullmatch(r"\d{4}", p):
            year = int(p)
    if not year:
        return None
    # Find month
    month = None
    for name, num in month_map.items():
        if name in s:
            month = num
            break
    # Find day
    day = None
    for p in parts:
        m = ord_pattern.match(p)
        if m:
            day = int(m.group(1))
            break
    if not month or not day:
        return None
    try:
        return datetime(year, month, day)
    except Exception:
        return None

for r in patent_de:
    r['grant_dt'] = parse_date(r.get('grant_date',''))

# Keep patents granted in second half of 2019
patent_de_2019h2 = [r for r in patent_de if r['grant_dt'] and r['grant_dt'].year == 2019 and r['grant_dt'].month >=7]

# Extract CPC codes and truncate to level-4 group (section+class+subclass, e.g., A61 or G06 etc.)

all_rows = []
for r in patent_de_2019h2:
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    year = r['grant_dt'].year
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        # Level 4 in cpc_definition looks like top-level class (e.g., A61, G06). Take first 3 chars up to first non-alnum
        m = re.match(r"([A-Z][0-9]{2})", code)
        if not m:
            continue
        group = m.group(1)
        all_rows.append({'group': group, 'year': year})

if not all_rows:
    result = []
else:
    df = pd.DataFrame(all_rows)
    # Count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='filings')

    # Build full time series per group across years present
    years = sorted(counts['year'].unique())
    ema_records = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(years, fill_value=0).sort_index()
        ema = None
        for y in years:
            x = sub.loc[y, 'filings']
            if ema is None:
                ema = x
            else:
                ema = alpha * x + (1-alpha) * ema
            ema_records.append({'group': g, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)
    # For each group, find year with max EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].copy()

    # Map to CPC definitions
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df.rename(columns={'symbol':'group'})
    merged = best.merge(defs_df[['group','titleFull']], on='group', how='left')

    merged = merged.sort_values('ema', ascending=False)
    result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XHN3C09VrOxSh9J15QGQGzkK': 'file_storage/call_XHN3C09VrOxSh9J15QGQGzkK.json', 'var_call_llat10MKWWFRRQWVHlD5bof8': 'file_storage/call_llat10MKWWFRRQWVHlD5bof8.json', 'var_call_4rArNjDTiQlmPCd1JqSafsML': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
