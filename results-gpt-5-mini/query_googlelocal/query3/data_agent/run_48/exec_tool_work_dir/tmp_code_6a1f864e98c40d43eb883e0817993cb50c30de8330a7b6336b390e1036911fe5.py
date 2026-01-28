code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data from storage file paths
businesss_fp = var_call_17dHCtrMXNTzfn65zgQX1Dy3
reviews_fp = var_call_Eo0sZiihehCibzOB6V9442qN

with open(businesss_fp, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(reviews_fp, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Clean ratings
if not df_r.empty:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.Series(dtype=float)

# Compute average ratings per gmap_id
avg_r = df_r.groupby('gmap_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Merge with businesses
df = pd.merge(df_b, avg_r, on='gmap_id', how='left')

# Helper to parse time strings like '6:30AM' or '6PM'
def parse_time(tstr):
    if not isinstance(tstr, str):
        return None
    t = tstr.strip().upper()
    # remove spaces
    t = re.sub(r'\s+', '', t)
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$', t, flags=re.IGNORECASE)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3).upper()
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else: # PM
        if hour != 12:
            hour += 12
    return hour*60 + minute

# Helper to determine if a closing time string is after 6:00PM

def closes_after_6(interval_str):
    if not isinstance(interval_str, str):
        return False
    s = interval_str.strip()
    if s.lower() == 'closed':
        return False
    # Replace unicode dashes with normal hyphen
    s2 = re.sub('[\u2013\u2014\u2012\u2011–—−]', '-', s)
    # split by hyphen
    parts = re.split('-|to', s2, flags=re.IGNORECASE)
    if len(parts) < 2:
        return False
    end = parts[-1]
    # Some intervals may include extra text; extract time like 9PM or 9:30AM
    time_match = re.search(r'(\d{1,2}(?::\d{2})?\s*[AP]M)', end, flags=re.IGNORECASE)
    if not time_match:
        return False
    end_time_str = time_match.group(1)
    minutes = parse_time(end_time_str)
    if minutes is None:
        return False
    return minutes > (18*60)  # strictly after 18:00

# Weekdays set
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

# For each business, parse hours and check weekday closings
results = []
for idx, row in df.iterrows():
    hours = row.get('hours')
    if not hours or not isinstance(hours, str) or hours.strip().lower()=='none':
        continue
    # Try to load hours as JSON
    parsed = None
    try:
        parsed = json.loads(hours)
    except Exception:
        # try literal eval fallback
        try:
            import ast
            parsed = ast.literal_eval(hours)
        except Exception:
            parsed = None
    if not parsed:
        continue
    # parsed expected as list of [day, timestr]
    open_after_6 = False
    for item in parsed:
        if not (isinstance(item, list) or isinstance(item, tuple)):
            continue
        if len(item) < 2:
            continue
        day = item[0]
        timestr = item[1]
        if day in weekdays:
            if closes_after_6(timestr):
                open_after_6 = True
                break
    if not open_after_6:
        continue
    # Only include if avg_rating exists
    if pd.isna(row.get('avg_rating')):
        continue
    results.append({
        'name': row.get('name'),
        'gmap_id': row.get('gmap_id'),
        'hours': row.get('hours'),
        'avg_rating': round(float(row.get('avg_rating')), 2)
    })

# Sort by avg_rating desc and take top 5
results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], x['name']))[:5]

# Prepare final JSON string
final = results_sorted

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_uUHscIHenEGxfl7Y59kSvzmJ': ['business_description'], 'var_call_17dHCtrMXNTzfn65zgQX1Dy3': 'file_storage/call_17dHCtrMXNTzfn65zgQX1Dy3.json', 'var_call_P0toIZYRsxOwXaM1NKJCpT82': ['review'], 'var_call_Eo0sZiihehCibzOB6V9442qN': 'file_storage/call_Eo0sZiihehCibzOB6V9442qN.json'}

exec(code, env_args)
