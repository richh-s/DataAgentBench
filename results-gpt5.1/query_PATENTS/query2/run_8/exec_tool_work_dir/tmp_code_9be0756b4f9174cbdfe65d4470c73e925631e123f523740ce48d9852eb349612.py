code = """import json, re, pandas as pd
from datetime import datetime

# Load full publication data from file
file_path = var_call_O7x0H6MwHWn7bMuOX2zmmWih
with open(file_path, 'r') as f:
    pubs = json.load(f)

# Helper to parse country code from Patents_info (look for ' In <country_code>,' or ' In <country_code> ' or ' the <country_code> patent')
country_pattern = re.compile(r"\b([A-Z]{2})\b")

def is_germany(patent_info):
    # Heuristic: look for ' In DE,' or ' the DE patent' etc.
    # But many summaries say 'In US,' etc. We'll specifically look for ' In DE,' or ' DE patent'
    if ' DE patent' in patent_info or ' DE,' in patent_info or ' DE ' in patent_info:
        return True
    # Also check 'In Germany' textual
    if 'In Germany' in patent_info or 'German patent' in patent_info:
        return True
    return False

# Parse natural-language grant date
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

ord_suffix = re.compile(r"(st|nd|rd|th)")

def parse_date(text):
    if not text:
        return None
    text = text.strip()
    text = re.sub(r"^dated ", "", text)
    text = re.sub(r"^on ", "", text)
    text = re.sub(r"^on ", "", text)
    text = text.replace(' of ', ' ')
    text = text.replace(' ,', ',')
    # Examples: '3rd August 2021', '21st of September, 2021', 'Mar 23rd, 2021', 'March 15th, 2020'
    # Try multiple patterns
    # Remove ordinal suffix from day
    text = ord_suffix.sub('', text)
    # Normalize commas
    text = text.replace(',', '')
    parts = text.split()
    if len(parts) < 3:
        return None
    # Handle formats like '3 August 2021' or 'August 3 2021'
    try:
        # Try day month year
        if parts[1] in months:
            day = int(parts[0])
            month = months[parts[1]]
            year = int(parts[2])
        elif parts[0] in months:
            month = months[parts[0]]
            day = int(parts[1])
            year = int(parts[2])
        else:
            # Try abbreviated month
            abbr_months = {m[:3]: i for m, i in months.items()}
            if parts[1][:3] in abbr_months:
                day = int(parts[0])
                month = abbr_months[parts[1][:3]]
                year = int(parts[2])
            elif parts[0][:3] in abbr_months:
                month = abbr_months[parts[0][:3]]
                day = int(parts[1])
                year = int(parts[2])
            else:
                return None
        return datetime(year, month, day)
    except Exception:
        return None

# Filter for German patents granted in 2nd half of 2019
filtered_records = []
for rec in pubs:
    info = rec.get('Patents_info','') or ''
    if not is_germany(info):
        continue
    gd = parse_date(rec.get('grant_date'))
    if not gd:
        continue
    if gd.year == 2019 and gd.month >= 7:
        filtered_records.append({'Patents_info': info, 'grant_date': gd, 'cpc': rec.get('cpc')})

# If no German patents found, return message
if not filtered_records:
    result = {'error': 'No German patents with clearly identifiable country code found in the dataset for 2nd half of 2019 using simple text heuristics.'}
    out = json.dumps(result)
    print("__RESULT__:")
    print(out)
else:
    # Build per-year filing counts per CPC group code (we don't have filing year; approximate with grant year)
    # Parse CPC JSON-like string
    def parse_cpc(cpc_str):
        if not cpc_str:
            return []
        try:
            return json.loads(cpc_str)
        except Exception:
            return []
    records = []
    for rec in filtered_records:
        year = rec['grant_date'].year
        for c in parse_cpc(rec['cpc']):
            code = c.get('code')
            if not code:
                continue
            # Level-4 group approximated as first 3 characters (section+class) or up to first '/'
            grp = code.split('/')[0][:3]
            records.append({'year': year, 'group': grp})

    if not records:
        result = {'error': 'No CPC codes parsed for selected German patents.'}
        out = json.dumps(result)
    else:
        df = pd.DataFrame(records)
        counts = df.groupby(['group','year']).size().reset_index(name='count')
        # Compute EMA per group sorted by year
        alpha = 0.1
        ema_rows = []
        for grp, sub in counts.groupby('group'):
            sub = sub.sort_values('year')
            ema = None
            for _, row in sub.iterrows():
                y = row['year']
                x = row['count']
                ema = x if ema is None else alpha * x + (1-alpha)*ema
                ema_rows.append({'group': grp, 'year': int(y), 'ema': float(ema)})
        ema_df = pd.DataFrame(ema_rows)
        idx = ema_df.groupby('group')['ema'].idxmax()
        best = ema_df.loc[idx].reset_index(drop=True)
        result = best.to_dict(orient='records')
        out = json.dumps(result)
    print("__RESULT__:")
    print(out)"""

env_args = {'var_call_O7x0H6MwHWn7bMuOX2zmmWih': 'file_storage/call_O7x0H6MwHWn7bMuOX2zmmWih.json', 'var_call_JUKBtYps6dWEHUWqqNQmWVHy': 'file_storage/call_JUKBtYps6dWEHUWqqNQmWVHy.json', 'var_call_nBUJK6egGwu7GqAvvOgGwacW': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
