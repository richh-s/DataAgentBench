code = """import json
import pandas as pd
import re

# Load data from the stored JSON files
with open(var_call_K0EBeo056FX1Yiepy0Ql6JiX, 'r', encoding='utf-8') as f:
    business_records = json.load(f)
with open(var_call_b8Mm5kLQ1RYE1B7OQwXYsu8m, 'r', encoding='utf-8') as f:
    review_records = json.load(f)

# DataFrames
bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

# Ensure rating is numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Compute average rating per gmap_id
avg_ratings = rdf.groupby('gmap_id', dropna=False)['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Helper to parse hours string and determine if business stays open after 6:00 PM on a weekday
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time_to_minutes(t):
    t = t.strip()
    # Handle missing or closed
    if t.lower() in ('closed', 'none', ''):
        return None
    # Normalize dash types
    t = t.replace('\u2013', '-')
    t = t.replace('\u2014', '-')
    t = t.replace('\u2010', '-')
    t = t.replace('\u2212', '-')
    # Regex to extract hour, minute, am/pm
    m = re.match(r'(?i)^(\d{1,2})(?::(\d{2}))?\s*(AM|PM|am|pm)?$', t)
    if not m:
        # Sometimes there's trailing/leading spaces or missing AM/PM; try to salvage
        # If ends with AM/PM without space
        m2 = re.search(r'(?i)(\d{1,2})(?::(\d{2}))?\s*(AM|PM|am|pm)$', t)
        if not m2:
            return None
        m = m2
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if ampm:
        ampm = ampm.upper()
    else:
        # If no AM/PM assume 24-hour? We'll assume None -> can't parse reliably
        return None
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    elif ampm == 'PM':
        if hour != 12:
            hour += 12
    return hour * 60 + minute


def opens_after_6pm(hours_field):
    if not hours_field or hours_field in (None, 'None'):
        return False
    try:
        parsed = json.loads(hours_field)
    except Exception:
        # If it's not valid JSON, try to eval-like parse by replacing single quotes
        try:
            parsed = eval(hours_field)
        except Exception:
            return False
    # parsed expected to be list of [day, time_range]
    for entry in parsed:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        if day not in WEEKDAYS:
            continue
        time_range = entry[1]
        if not time_range or time_range.lower() == 'closed':
            continue
        # normalize dash and split
        time_range_norm = re.sub('[\u2013\u2014\u2010\u2212–—]', '-', time_range)
        parts = time_range_norm.split('-')
        if len(parts) < 2:
            continue
        start_s = parts[0].strip()
        end_s = parts[1].strip()
        end_minutes = parse_time_to_minutes(end_s)
        if end_minutes is None:
            continue
        # Check strictly greater than 6:00 PM (18:00 -> 1080 minutes)
        if end_minutes > 18 * 60:
            return True
    return False

# Apply on business df
bdf['opens_after_6pm_weekday'] = bdf['hours'].apply(opens_after_6pm)

# Merge with average ratings
merged = pd.merge(bdf, avg_ratings, on='gmap_id', how='left')

# Filter businesses that remain open after 6pm on at least one weekday and have avg_rating
filtered = merged[merged['opens_after_6pm_weekday'] & merged['avg_rating'].notna()].copy()

# Sort by avg_rating desc, if tie sort by name
filtered.sort_values(['avg_rating','name'], ascending=[False, True], inplace=True)

# Take top 5
top5 = filtered.head(5)

# Prepare output list
result = []
for _, row in top5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'average_rating': round(float(row['avg_rating']), 2)
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rpWZKTqBWBwzJpIbeU2qEYt1': ['business_description'], 'var_call_K0EBeo056FX1Yiepy0Ql6JiX': 'file_storage/call_K0EBeo056FX1Yiepy0Ql6JiX.json', 'var_call_b8Mm5kLQ1RYE1B7OQwXYsu8m': 'file_storage/call_b8Mm5kLQ1RYE1B7OQwXYsu8m.json'}

exec(code, env_args)
