code = """import json
import pandas as pd
import math
import ast

# Load data from storage variables
business_data = None
reviews_data = None

# var_call_ENvHJNqhqjsCK9RfUlp1j2Iu and var_call_339SjRX2zZOOYj64qMKxLcX1 are provided in storage
try:
    if isinstance(var_call_ENvHJNqhqjsCK9RfUlp1j2Iu, str):
        with open(var_call_ENvHJNqhqjsCK9RfUlp1j2Iu, 'r', encoding='utf-8') as f:
            business_data = json.load(f)
    else:
        business_data = var_call_ENvHJNqhqjsCK9RfUlp1j2Iu
except Exception as e:
    business_data = []

try:
    if isinstance(var_call_339SjRX2zZOOYj64qMKxLcX1, str):
        with open(var_call_339SjRX2zZOOYj64qMKxLcX1, 'r', encoding='utf-8') as f:
            reviews_data = json.load(f)
    else:
        reviews_data = var_call_339SjRX2zZOOYj64qMKxLcX1
except Exception as e:
    reviews_data = []

# Convert to DataFrame
bd = pd.DataFrame(business_data)
rv = pd.DataFrame(reviews_data)

# Ensure rating numeric
if not rv.empty:
    rv['rating'] = pd.to_numeric(rv['rating'], errors='coerce')

# Helper to parse hours field
import re

def try_load_hours(val):
    if val is None:
        return None
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        s = val.strip()
        if s == '' or s.lower() == 'none' or s.lower() == 'null':
            return None
        # Try JSON load
        try:
            return json.loads(s)
        except Exception:
            pass
        # Try ast literal eval
        try:
            return ast.literal_eval(s)
        except Exception:
            pass
        # Fallback: try to extract pairs using regex
        try:
            # find all ["Day", "time"] patterns
            pairs = re.findall(r"\[\s*\"(.*?)\"\s*,\s*\"(.*?)\"\s*\]", s)
            if pairs:
                return [[p[0], p[1]] for p in pairs]
        except Exception:
            pass
    return None

# Time parsing
def parse_time_to_minutes(t):
    # t like '9AM', '9:30AM', '12PM', '12:00AM'
    if t is None:
        return None
    t = t.strip().upper()
    # Remove spaces
    t = t.replace(' ', '')
    # Replace unicode en dash or em dash
    t = t.replace('\u2013', '-')
    # Handle times like '9AM' or '9:30AM'
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', t)
    if not m:
        # try to parse with colon and AM/PM at end
        # or if it's like '24hours'
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else: # PM
        if hour != 12:
            hour += 12
    return hour*60 + minute


def closing_time_minutes(time_range_str):
    # time_range_str e.g. '9:30AM–9:30PM' or 'Closed'
    if not isinstance(time_range_str, str):
        return None
    s = time_range_str.strip()
    if s.lower() == 'closed':
        return None
    # replace unicode dash with hyphen
    s = s.replace('\u2013', '-')
    s = s.replace('\u2014', '-')
    # split on - or – or — or to
    parts = re.split(r'[-–—]|to', s)
    if len(parts) < 2:
        return None
    close_part = parts[-1]
    # cleanup
    close_part = close_part.strip()
    # Sometimes times include extra text like '11AM–9:30PM (EST)'
    # Keep only the leading time token
    # Extract token matching \d{1,2}(:\d{2})?(AM|PM)
    m = re.search(r'(\d{1,2}(?::\d{2})?(?:AM|PM))', close_part, re.IGNORECASE)
    if not m:
        return None
    ttok = m.group(1).upper()
    return parse_time_to_minutes(ttok)

# Determine if a business is open after 6:00 PM on at least one weekday
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def open_after_6pm(hours_field):
    parsed = try_load_hours(hours_field)
    if not parsed:
        return False
    # parsed expected as list of [day, time]
    for entry in parsed:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0].strip()
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        if not isinstance(times, str):
            continue
        close_min = closing_time_minutes(times)
        if close_min is None:
            continue
        if close_min > 18*60:
            return True
    return False

# Apply filter
bd['open_after_6pm_weekday'] = bd['hours'].apply(lambda x: open_after_6pm(x))

# Compute average ratings per gmap_id
if not rv.empty:
    avg_ratings = rv.groupby('gmap_id', as_index=False)['rating'].mean()
    avg_ratings.rename(columns={'rating':'avg_rating'}, inplace=True)
else:
    avg_ratings = pd.DataFrame(columns=['gmap_id','avg_rating'])

# Merge
merged = bd.merge(avg_ratings, on='gmap_id', how='left')
# Only businesses open after 6pm on at least one weekday and with at least one review
filtered = merged[(merged['open_after_6pm_weekday']==True) & (~merged['avg_rating'].isna())]

# Sort by avg_rating desc, then by name
filtered_sorted = filtered.sort_values(by=['avg_rating','name'], ascending=[False, True])

# Select top 5
top5 = filtered_sorted.head(5)

# Prepare output list
out = []
for _, row in top5.iterrows():
    out.append({
        'name': row['name'],
        'hours': row['hours'],
        'average_rating': round(float(row['avg_rating']), 2)
    })

# Print result in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ENvHJNqhqjsCK9RfUlp1j2Iu': 'file_storage/call_ENvHJNqhqjsCK9RfUlp1j2Iu.json', 'var_call_339SjRX2zZOOYj64qMKxLcX1': 'file_storage/call_339SjRX2zZOOYj64qMKxLcX1.json'}

exec(code, env_args)
