code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_WAOcv3U8LTlO91e3PRbkY8eH, 'r') as f:
    pubs = json.load(f)

# Filter to German patents by parsing Patents_info (look for ' DE-' or ' Germany ' or country_code DE patterns)
# Here, we assume country_code like 'DE-' in the application or publication identifiers.

def is_germany(pinfo: str) -> bool:
    if not isinstance(pinfo, str):
        return False
    # Common pattern: ' DE-' in IDs or ' Germany ' mention
    if re.search(r'\bDE-\d', pinfo):
        return True
    if ' Germany ' in pinfo or ' German ' in pinfo:
        return True
    # country_code DE
    if 'country code DE' in pinfo or 'country_code DE' in pinfo or 'country code: DE' in pinfo:
        return True
    return False

# Parse natural-language grant date to datetime
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_grant_date(s):
    if not isinstance(s, str):
        return None
    s = s.strip()
    # Normalize ordinal suffixes
    s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
    # Remove leading words like 'dated'
    s = re.sub(r'^(dated|on) ', '', s, flags=re.IGNORECASE)
    # Patterns: '3 August 2021', '3 August, 2021', 'August 3 2021', 'August 3, 2021', '21st of September, 2021'
    s = re.sub(r' of ', ' ', s)
    s = s.replace(',', '')
    parts = s.split()
    if len(parts) < 3:
        return None
    # Try detect format
    try:
        # if first is digit -> D M Y
        if parts[0].isdigit():
            day = int(parts[0])
            month = months.get(parts[1], None)
            year = int(parts[2]) if parts[2].isdigit() else None
        else:
            # M D Y
            month = months.get(parts[0], None)
            day = int(parts[1]) if parts[1].isdigit() else None
            year = int(parts[2]) if parts[2].isdigit() else None
        if None in (day, month, year):
            return None
        return datetime(year, month, day)
    except Exception:
        return None

records = []
for r in pubs:
    if not is_germany(r.get('Patents_info','')):
        continue
    gd = parse_grant_date(r.get('grant_date'))
    if gd is None:
        continue
    # second half of 2019
    if not (gd.year == 2019 and gd.month >= 7):
        continue
    cpc_raw = r.get('cpc')
    if not isinstance(cpc_raw, str):
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # Level 4 group: take first 4 chars before slash or as-is
        main = code.split('/')[0]
        group4 = main[:4]
        records.append({'year': gd.year, 'cpc_group4': group4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count patents per year per CPC group
    counts = df.groupby(['cpc_group4','year']).size().reset_index(name='count')
    # Compute EMA by year for each group, sorted by year
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.groupby('cpc_group4'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            y = row['year']
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'cpc_group4': g, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # For each group, find year with highest EMA
    idx = ema_df.groupby('cpc_group4')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_WAOcv3U8LTlO91e3PRbkY8eH': 'file_storage/call_WAOcv3U8LTlO91e3PRbkY8eH.json', 'var_call_txSRDQ7zWiIytacg9L5eIUgY': 'file_storage/call_txSRDQ7zWiIytacg9L5eIUgY.json'}

exec(code, env_args)
