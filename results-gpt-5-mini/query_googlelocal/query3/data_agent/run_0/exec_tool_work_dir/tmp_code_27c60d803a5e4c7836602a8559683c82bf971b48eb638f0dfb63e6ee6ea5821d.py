code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_LHKVYAQtPH9FPOHT5hBUMOQ7, 'r', encoding='utf-8') as f:
    business_records = json.load(f)
with open(var_call_gZ8YjyQnNztrv8WEFjJKcFRk, 'r', encoding='utf-8') as f:
    review_records = json.load(f)

# Create DataFrames
df_bus = pd.DataFrame(business_records)
df_rev = pd.DataFrame(review_records)

# Clean review ratings
if not df_rev.empty:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
    avg_ratings = df_rev.groupby('gmap_id', dropna=False)['rating'].mean().reset_index()
    avg_ratings.columns = ['gmap_id', 'avg_rating']
else:
    avg_ratings = pd.DataFrame(columns=['gmap_id', 'avg_rating'])

# Helper to parse time strings like '9:30PM' or '11AM'
import re

def parse_time(tstr):
    tstr = tstr.strip()
    # handle cases like 'Closed' or empty
    if not tstr or 'Closed' in tstr:
        return None
    # Remove spaces
    tstr = tstr.replace(' ', '')
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?(AM|PM|am|pm)$", tstr)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3).upper()
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return hour * 60 + minute

# Function to determine if business stays open after 6:00 PM (18:00) on at least one weekday
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def opens_after_6pm(hours_field):
    if not hours_field or hours_field == 'None':
        return False
    try:
        parsed = json.loads(hours_field)
    except Exception:
        return False
    # parsed expected as list of [day, "start–end"]
    for entry in parsed:
        if not isinstance(entry, list) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        # some times may be like '9AM\u20139:30PM' with en-dash
        if not times or 'Closed' in times:
            continue
        # split on dash-like characters
        parts = re.split(r"[\u2013\u2014\-–—]", times)
        if len(parts) < 2:
            continue
        close_str = parts[-1]
        ct = parse_time(close_str)
        if ct is None:
            continue
        if ct > 18*60:
            return True
    return False

# Apply function to businesses
df_bus['stays_after_6pm_weekday'] = df_bus['hours'].apply(opens_after_6pm)

# Merge with avg ratings
df_merged = pd.merge(df_bus, avg_ratings, on='gmap_id', how='left')
# Drop businesses without ratings (NaN avg_rating)
df_merged = df_merged[~df_merged['avg_rating'].isna()].copy()

# Filter businesses that stay open after 6pm on at least one weekday
df_filtered = df_merged[df_merged['stays_after_6pm_weekday']]

# Sort by avg_rating descending and take top 5
df_sorted = df_filtered.sort_values(by='avg_rating', ascending=False)
result_df = df_sorted[['gmap_id', 'name', 'hours', 'avg_rating']].head(5).copy()
# Round avg_rating to 2 decimals
result_df['avg_rating'] = result_df['avg_rating'].round(2)

# Convert to list of dicts
result = result_df.to_dict(orient='records')

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LHKVYAQtPH9FPOHT5hBUMOQ7': 'file_storage/call_LHKVYAQtPH9FPOHT5hBUMOQ7.json', 'var_call_gZ8YjyQnNztrv8WEFjJKcFRk': 'file_storage/call_gZ8YjyQnNztrv8WEFjJKcFRk.json'}

exec(code, env_args)
