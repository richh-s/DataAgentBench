code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data from storage variables
# var_call_2pU7qpbodgrBQjz6xrzi0VTt and var_call_J4ONTrtmjePN0UVRr01dFYJg are available

def load_storage(var):
    if isinstance(var, str):
        # it's a filepath to a json
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business_records = load_storage(var_call_2pU7qpbodgrBQjz6xrzi0VTt)
review_records = load_storage(var_call_J4ONTrtmjePN0UVRr01dFYJg)

# Create DataFrames
biz_df = pd.DataFrame(business_records)
rev_df = pd.DataFrame(review_records)

# Ensure ratings numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Compute average ratings per gmap_id
avg_ratings = rev_df.groupby('gmap_id', as_index=False)['rating'].mean()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Merge with business
merged = biz_df.merge(avg_ratings, on='gmap_id', how='inner')

# Helper to parse time string to minutes since midnight
ampm_re = re.compile(r"(?i)^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$")

def time_str_to_minutes(tstr):
    tstr = tstr.strip().upper()
    # Fix spaces (e.g., '9:30PM')
    # Try to match
    m = ampm_re.match(tstr)
    if not m:
        # Sometimes there might be no AM/PM; fail gracefully
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return hour * 60 + minute

# Function to check if any weekday closing time > 6:00 PM
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def closes_after_6pm(hours_field):
    if not hours_field or hours_field == 'None':
        return False
    try:
        data = json.loads(hours_field)
    except Exception:
        # try literal_eval fallback
        try:
            from ast import literal_eval
            data = literal_eval(hours_field)
        except Exception:
            return False
    for entry in data:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in weekdays:
            continue
        if not times or 'Closed' in times:
            continue
        # Split on dash variants
        parts = re.split(r"[-	6\u2013\u2014\u2015]", times)
        # The above includes various dash types; fallback to non-dash splitting
        if len(parts) < 2:
            # try splitting on en-dash or em-dash explicitly
            parts = re.split(r'[–—-]', times)
        if len(parts) < 2:
            continue
        end_part = parts[-1].strip()
        # Sometimes there may be additional text; extract time token with AM/PM
        m = re.search(r"(\d{1,2}(?::\d{2})?\s*[AP]M)", end_part, flags=re.IGNORECASE)
        if not m:
            # maybe the end is like '6PM' without space
            m = re.search(r"(\d{1,2}(?::\d{2})?[AP]M)", end_part, flags=re.IGNORECASE)
        if not m:
            continue
        end_time_str = m.group(1).upper().replace(' ', '')
        minutes = time_str_to_minutes(end_time_str)
        if minutes is None:
            continue
        if minutes > 18 * 60:
            return True
    return False

# Apply filter
merged['opens_after_6pm_weekday'] = merged['hours'].apply(closes_after_6pm)
filtered = merged[merged['opens_after_6pm_weekday'] == True].copy()

# If avg_rating missing, drop
filtered = filtered.dropna(subset=['avg_rating'])

# Sort by avg_rating desc and take top 5
filtered['avg_rating'] = filtered['avg_rating'].astype(float)
result = filtered.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# Prepare output list
out = []
for _, row in result.iterrows():
    out.append({
        'name': row.get('name'),
        'gmap_id': row.get('gmap_id'),
        'hours': row.get('hours'),
        'average_rating': round(float(row.get('avg_rating')), 2)
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2pU7qpbodgrBQjz6xrzi0VTt': 'file_storage/call_2pU7qpbodgrBQjz6xrzi0VTt.json', 'var_call_J4ONTrtmjePN0UVRr01dFYJg': 'file_storage/call_J4ONTrtmjePN0UVRr01dFYJg.json'}

exec(code, env_args)
