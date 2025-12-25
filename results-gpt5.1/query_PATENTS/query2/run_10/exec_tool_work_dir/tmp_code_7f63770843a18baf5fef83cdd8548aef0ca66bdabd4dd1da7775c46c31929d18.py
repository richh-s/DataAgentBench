code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data
path = var_call_A0bEfxAb8BJdDXh9sjJaK9Mr
with open(path, 'r') as f:
    pubs = json.load(f)

# Helper to extract country code from Patents_info (assumes pattern "holds the XX patent" or "In XX, the application")
cc_pattern1 = re.compile(r"\bthe\s+([A-Z]{2})\s+patent")
cc_pattern2 = re.compile(r"In\s+([A-Z]{2}),\s+the application")

def get_country(info):
    for pat in (cc_pattern2, cc_pattern1):
        m = pat.search(info)
        if m:
            return m.group(1)
    return None

# Parse natural-language grant date into datetime, return None if fail
MONTHS = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_date(s):
    if not s:
        return None
    s = s.strip()
    s = s.replace('dated ','')
    s = s.replace('the ','')
    s = s.replace(',', '')
    # normalize ordinals
    s = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", s)
    parts = s.split()
    try:
        if len(parts) == 3:
            # e.g. 3 August 2021 or August 3 2021
            if parts[0] in MONTHS:
                month = MONTHS[parts[0]]; day = int(parts[1]); year = int(parts[2])
            else:
                day = int(parts[0]); month = MONTHS[parts[1]]; year = int(parts[2])
        elif len(parts) == 4 and parts[1] == 'of':
            # e.g. 21st of September 2021 -> 21 September 2021 already normalized
            day = int(parts[0]); month = MONTHS[parts[2]]; year = int(parts[3])
        else:
            return None
        return datetime(year, month, day)
    except Exception:
        return None

records = []
for r in pubs:
    cc = get_country(r.get('Patents_info','') or '')
    if cc != 'DE':
        continue
    gd = parse_date(r.get('grant_date'))
    if not gd:
        continue
    # second half of 2019
    if not (gd.year == 2019 and gd.month >= 7 and gd.month <= 12):
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpc_raw)]
    except Exception:
        continue
    for code in codes:
        # level 4 group: take first 3 chars (section+class) or main group? Here assume first 3 chars like 'A01'
        grp = code[:3]
        records.append({'year': gd.year, 'cpc_group': grp})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per year per group
    counts = df.groupby(['cpc_group','year']).size().reset_index(name='filings')
    # compute EMA by year for each group with alpha=0.1 sorted by year
    alpha = 0.1
    ema_rows = []
    for grp, g in counts.groupby('cpc_group'):
        g = g.sort_values('year')
        ema = None
        for _, row in g.iterrows():
            y = int(row['year']); x = row['filings']
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            ema_rows.append({'cpc_group': grp, 'year': y, 'filings': int(x), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # best year = year with max EMA per group
    idx = ema_df.groupby('cpc_group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_A0bEfxAb8BJdDXh9sjJaK9Mr': 'file_storage/call_A0bEfxAb8BJdDXh9sjJaK9Mr.json', 'var_call_7irkwpaIQLFxCB0EfAT39hED': 'file_storage/call_7irkwpaIQLFxCB0EfAT39hED.json'}

exec(code, env_args)
