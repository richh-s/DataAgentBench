code = """import json, re, pandas as pd

# Load full publication data
with open(var_call_CJrgdXl4wZ91r10K1UJetCXL, 'r') as f:
    pubs = json.load(f)

# Filter to German patents via country code "DE" in Patents_info
pattern_de = re.compile(r'\bDE-\d', re.IGNORECASE)

def is_german(info):
    if not isinstance(info, str):
        return False
    return bool(pattern_de.search(info))

filtered = [r for r in pubs if is_german(r.get('Patents_info')) and isinstance(r.get('grant_date'), str)]

# Parse natural-language grant_date and keep those in second half of 2019
from datetime import datetime

months = {m.lower(): i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

suffix_re = re.compile(r'(st|nd|rd|th)', re.IGNORECASE)


def parse_date(s):
    if not isinstance(s, str):
        return None
    s = s.strip()
    # remove leading words like 'dated' or 'on'
    s = re.sub(r'^(dated|on)\s+', '', s, flags=re.IGNORECASE)
    # handle formats like '3rd August 2021', '21st of September, 2021', 'July 15th, 2019'
    s = s.replace(',', '')
    parts = s.split()
    try:
        if len(parts) == 3:  # '3rd August 2021' or 'July 3rd 2021'
            if parts[0][0].isdigit():
                day = int(suffix_re.sub('', parts[0]))
                month = months.get(parts[1].lower())
                year = int(parts[2])
            else:
                month = months.get(parts[0].lower())
                day = int(suffix_re.sub('', parts[1]))
                year = int(parts[2])
        elif len(parts) == 4 and parts[1].lower() == 'of':  # '21st of September 2021'
            day = int(suffix_re.sub('', parts[0]))
            month = months.get(parts[2].lower())
            year = int(parts[3])
        else:
            return None
        if not month:
            return None
        return datetime(year, month, day)
    except Exception:
        return None

for r in filtered:
    r['grant_dt'] = parse_date(r.get('grant_date'))

filtered = [r for r in filtered if r['grant_dt'] is not None and r['grant_dt'].year == 2019 and r['grant_dt'].month >= 7]

# Extract year of filing for EMA -- question says EMA of patent filings each year; but we only have grant filter, so count by filing year if available, else by grant year

def extract_year(date_str, fallback_year):
    d = parse_date(date_str) if isinstance(date_str, str) else None
    return d.year if d else fallback_year

records = []
for r in filtered:
    cpc_raw = r.get('cpc')
    try:
        cpc_list = json.loads(cpc_raw) if isinstance(cpc_raw, str) else []
    except Exception:
        continue
    filing_year = extract_year(r.get('filing_date'), r['grant_dt'].year)
    for c in cpc_list:
        code = c.get('code') if isinstance(c, dict) else None
        if not code:
            continue
        # level 4 group code taken as first 3 chars (section+class) per definitions table preview
        group = code[:3]
        records.append({'group': group, 'year': filing_year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per group-year
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # for each group, compute EMA over years sorted ascending
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            y = row['year']
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'group': g, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # pick best year (highest EMA) per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CJrgdXl4wZ91r10K1UJetCXL': 'file_storage/call_CJrgdXl4wZ91r10K1UJetCXL.json', 'var_call_I4sJeyS7IKseQktMhMFgZRCR': 'file_storage/call_I4sJeyS7IKseQktMhMFgZRCR.json'}

exec(code, env_args)
