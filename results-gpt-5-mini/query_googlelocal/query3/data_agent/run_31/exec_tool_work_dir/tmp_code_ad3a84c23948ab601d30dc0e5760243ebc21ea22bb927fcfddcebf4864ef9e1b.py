code = """import json
import pandas as pd
import re
from statistics import mean

# Load data from storage files
business_path = var_call_ENRXLjOTPJ7NhURLnfJtNpaQ
reviews_path = var_call_7R5Ovpv8svuZg4pZhhTbXgal

with open(business_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize ratings
if not df_r.empty:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.Series(dtype=float)

# Compute average rating per gmap_id
avg = df_r.groupby('gmap_id')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Merge
df = pd.merge(df_b, avg, on='gmap_id', how='left')

# Helper to parse hours
weekdays = set(["Monday","Tuesday","Wednesday","Thursday","Friday"]) 

def parse_hours_field(hours_field):
    if hours_field is None:
        return []
    hs = hours_field
    if isinstance(hs, str):
        if hs.strip().lower() in ('none',''):
            return []
        # try json loads
        try:
            parsed = json.loads(hs)
        except Exception:
            try:
                # fallback to literal eval
                import ast
                parsed = ast.literal_eval(hs)
            except Exception:
                return []
    else:
        parsed = hs
    # Expect parsed to be list of [day, timestr]
    result = []
    for item in parsed:
        if not item or len(item) < 2:
            continue
        day = item[0]
        timestr = item[1]
        result.append((day, timestr))
    return result

# helper to convert time like '9:30PM' to minutes
def time_to_minutes(t):
    t = t.strip().upper()
    # handle variants
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$", t)
    if not m:
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
    return hour*60 + minute

# function to check if any weekday has closing time after 6:00 PM

def closes_after_6pm(hours_field):
    parsed = parse_hours_field(hours_field)
    for day, times in parsed:
        if day not in weekdays:
            continue
        if not isinstance(times, str):
            continue
        t = times.strip()
        if t.lower() == 'closed':
            continue
        # split on dash or en dash
        parts = re.split(r"[-–—\u2013]+", t)
        if len(parts) < 2:
            continue
        end = parts[-1].strip()
        # Some entries like '11AM' or '9:30PM' should match
        end_min = time_to_minutes(end)
        if end_min is None:
            # try to extract with regex
            m = re.search(r"(\d{1,2}(?::\d{2})?\s*(AM|PM))", end)
            if m:
                end_min = time_to_minutes(m.group(1))
        if end_min is None:
            continue
        if end_min > 18*60:
            return True
    return False

# Filter businesses that meet criteria and have avg_rating
filtered = []
for _, row in df.iterrows():
    hours_field = row.get('hours')
    if closes_after_6pm(hours_field):
        avg_rating = row.get('avg_rating')
        if pd.isna(avg_rating):
            continue
        filtered.append({'name': row.get('name'), 'hours': hours_field, 'avg_rating': round(float(avg_rating),2)})

# Sort by avg_rating desc and take top 5
filtered_sorted = sorted(filtered, key=lambda x: (-x['avg_rating'], x['name']))[:5]

# Prepare output
result = filtered_sorted

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_52sOoPTZhAxKDtv7rOCkf6ew': ['business_description'], 'var_call_ENRXLjOTPJ7NhURLnfJtNpaQ': 'file_storage/call_ENRXLjOTPJ7NhURLnfJtNpaQ.json', 'var_call_btdaWZYl2ZzZNKwOWeJhqbeJ': ['review'], 'var_call_7R5Ovpv8svuZg4pZhhTbXgal': 'file_storage/call_7R5Ovpv8svuZg4pZhhTbXgal.json'}

exec(code, env_args)
