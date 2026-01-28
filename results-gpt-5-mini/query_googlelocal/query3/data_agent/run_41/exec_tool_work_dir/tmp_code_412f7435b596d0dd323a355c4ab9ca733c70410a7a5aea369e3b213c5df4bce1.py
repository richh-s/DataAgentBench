code = """import pandas as pd
import json
import ast
import re

# Load data from storage-provided file paths
with open(var_call_guEnygnGvG3Ho8ZUHk5JIUm6, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_EtzOLGE9yFWTSuOP9jqZI03K, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# DataFrames
df_bus = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Normalize types
if 'rating' in df_rev.columns:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Compute average ratings per business
avg_ratings = df_rev.groupby('gmap_id', dropna=False)['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Helper to parse time strings into minutes since midnight
def time_to_minutes(t):
    t = t.strip()
    # handle cases like 'Closed' or empty
    if not t or t.lower() == 'closed' or t.lower() == 'none':
        return None
    # Some strings may include extra text like 'Closes 9:30PM' - extract time portion
    # Find the last occurrence of an AM/PM pattern
    m = re.search(r'([0-9]{1,2}(:[0-9]{2})?\s*[APap][Mm])', t)
    if m:
        t = m.group(1)
    # Normalize
    t = t.upper().replace(' ', '')
    # Extract AM/PM
    ampm = 'AM' if t.endswith('AM') else ('PM' if t.endswith('PM') else None)
    if not ampm:
        # try to infer if contains 'NOON' or 'MIDNIGHT'
        if 'NOON' in t:
            return 12*60
        if 'MIDNIGHT' in t:
            return 0
        return None
    num = t[:-2]
    if ':' in num:
        hr, mn = num.split(':')
    else:
        hr, mn = num, '0'
    try:
        hr = int(hr)
        mn = int(mn)
    except:
        return None
    if ampm == 'AM':
        if hr == 12:
            hr = 0
    else:  # PM
        if hr != 12:
            hr = hr + 12
    return hr*60 + mn

# Function to check if business remains open after 6:00 PM on at least one weekday
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def open_after_6_on_weekday(hours_field):
    if hours_field is None:
        return False
    # If it's not a list already, try to literal_eval
    hours = None
    if isinstance(hours_field, list):
        hours = hours_field
    else:
        s = str(hours_field).strip()
        if s in ('None',''):
            return False
        try:
            hours = ast.literal_eval(s)
        except Exception:
            # if parse fails, attempt simple checks for a time like '9AM-10PM'
            # split by day separators (comma) and analyze pieces
            hours = []
            parts = re.split(r';|,', s)
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                # try to extract day and range if present
                m = re.match(r'([A-Za-z]+)[:\s]+(.+)', p)
                if m:
                    day = m.group(1)
                    rng = m.group(2)
                    hours.append([day, rng])
    if not hours:
        return False
    # Iterate entries
    for entry in hours:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        time_range = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(time_range, str):
            continue
        tr = time_range.strip()
        if not tr or tr.lower() == 'closed' or 'closed' in tr.lower():
            continue
        # Split on dash/en-dash/em-dash
        parts = re.split(r'[-	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6	6\u2013\u2014\u2012\u2010]', tr)
        if len(parts) < 2:
            # maybe '9AM to 10PM'
            parts = re.split(r'\s+to\s+|\s+\u2013\s+|\s+-\s+', tr)
        if len(parts) >= 2:
            start_s = parts[0].strip()
            end_s = parts[1].strip()
            end_min = time_to_minutes(end_s)
            if end_min is not None and end_min > 18*60:
                return True
        else:
            # single time, maybe indicates open until late (not much we can do)
            # check if it contains PM and hour > 6
            m = re.search(r'([0-9]{1,2}(:[0-9]{2})?\s*[APap][Mm])', tr)
            if m:
                tmin = time_to_minutes(m.group(1))
                if tmin is not None and tmin > 18*60:
                    return True
    return False

# Apply to businesses
df_bus['open_after_6_weekday'] = df_bus['hours'].apply(open_after_6_on_weekday)

# Merge average ratings
df_merged = df_bus.merge(avg_ratings, on='gmap_id', how='left')

# Filter those open after 6pm on at least one weekday and have avg_rating
df_filtered = df_merged[(df_merged['open_after_6_weekday']==True) & (df_merged['avg_rating'].notna())]

# Sort by avg_rating desc
df_sorted = df_filtered.sort_values(by='avg_rating', ascending=False)

# Select top 5
top5 = df_sorted.head(5)

# Prepare output
output = []
for _, row in top5.iterrows():
    output.append({
        'name': row.get('name'),
        'gmap_id': row.get('gmap_id'),
        'hours': row.get('hours'),
        'average_rating': round(float(row.get('avg_rating')), 2) if pd.notna(row.get('avg_rating')) else None
    })

result_str = json.dumps(output)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_guEnygnGvG3Ho8ZUHk5JIUm6': 'file_storage/call_guEnygnGvG3Ho8ZUHk5JIUm6.json', 'var_call_EtzOLGE9yFWTSuOP9jqZI03K': 'file_storage/call_EtzOLGE9yFWTSuOP9jqZI03K.json'}

exec(code, env_args)
