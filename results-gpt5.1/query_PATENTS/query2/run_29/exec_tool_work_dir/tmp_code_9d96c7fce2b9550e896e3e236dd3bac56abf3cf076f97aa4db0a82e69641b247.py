code = """import json, re, pandas as pd
from collections import defaultdict

# Load publication data from file
path = var_call_fuIs0iy51HB8uSiKoiJQYPRJ
with open(path, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info country code 'DE-'
_de_pubs = []
for r in pubs:
    info = r.get('Patents_info') or ''
    if ' DE-' in info or ' DE ' in info or ' DE,' in info or ' DE.' in info or ' DE-' in info or ' DE/' in info or ' DE_' in info or ' DE\n' in info or ' DE\t' in info or ' DE-' in info:
        _de_pubs.append(r)
    elif ' DE-' in info or ' DE-' in info:
        _de_pubs.append(r)
    elif ' DE-' in info or ' DE-' in info:
        _de_pubs.append(r)
    # Also check pattern country code like "DE-" in publication number
    elif 'DE-' in info:
        _de_pubs.append(r)

# Helper to parse natural language grant_date to year
month_map = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(d):
    if not d:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', d)
    y = re.search(r'(19|20)\d{2}', d)
    if not y:
        return None
    return int(y.group(0))

# Count filings per CPC symbol per year (using grant year as proxy)
counts = defaultdict(lambda: defaultdict(int))

for r in _de_pubs:
    year = parse_year(r.get('grant_date',''))
    if not year:
        continue
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        try:
            cpcs = json.loads(cpc_raw.replace("'", '"'))
        except Exception:
            continue
    codes = {e.get('code') for e in cpcs if isinstance(e, dict) and e.get('code')}
    for code in codes:
        counts[code][year] += 1

# Compute EMA with alpha=0.1 per CPC over sorted years
alpha = 0.1
ema_records = []
for code, year_dict in counts.items():
    years = sorted(year_dict.keys())
    ema = None
    for y in years:
        val = year_dict[y]
        if ema is None:
            ema = val
        else:
            ema = alpha*val + (1-alpha)*ema
        ema_records.append({'code': code, 'year': y, 'ema': ema})

ema_df = pd.DataFrame(ema_records)

# For each code, find year with max EMA
if ema_df.empty:
    result = []
else:
    idx = ema_df.groupby('code')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)

    # Load CPC level 4 definitions
    defs = var_call_tNto8tMacFeLrGsC9gZ0UgiC
    # defs is a file path
    with open(defs, 'r') as f:
        defs_list = json.load(f)
    defs_df = pd.DataFrame(defs_list)

    # Map CPC symbol to section/class (first 3 chars like 'A61') present at level 4
    defs_df['symbol3'] = defs_df['symbol'].str[:3]
    best_df['symbol3'] = best_df['code'].str[:3]

    merged = best_df.merge(defs_df[['symbol3','titleFull']], on='symbol3', how='left')
    merged = merged.sort_values('ema', ascending=False)
    result = merged.head(50)[['code','titleFull','year','ema']].to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fuIs0iy51HB8uSiKoiJQYPRJ': 'file_storage/call_fuIs0iy51HB8uSiKoiJQYPRJ.json', 'var_call_tNto8tMacFeLrGsC9gZ0UgiC': 'file_storage/call_tNto8tMacFeLrGsC9gZ0UgiC.json', 'var_call_mezm8kWUI1uklyf3DJRoCvdK': []}

exec(code, env_args)
