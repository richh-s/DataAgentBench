code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_2xoh2qOwpRh4fU6xTKNp3VVm, 'r') as f:
    business = json.load(f)
with open(var_call_FZg7woBCJ10SxtPGJEHiHShF, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bf = pd.DataFrame(business)
rf = pd.DataFrame(reviews)

# Ensure correct dtypes
if 'rating' in rf.columns:
    rf['rating'] = pd.to_numeric(rf['rating'], errors='coerce')

# Compute average rating per gmap_id
avg_r = rf.groupby('gmap_id', dropna=False)['rating'].mean().reset_index().rename(columns={'rating': 'avg_rating'})

# Merge with business data
merged = bf.merge(avg_r, on='gmap_id', how='left')

# Helper to parse time strings into minutes since midnight
def parse_time_to_minutes(t):
    if t is None:
        return None
    t = t.strip()
    if t.lower() == 'closed':
        return None
    # Regex to capture hour, optional minute, am/pm
    m = re.search(r'(\d{1,2})(?::(\d{2}))?\s*([APap][Mm])', t)
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

# Weekdays list
weekdays = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

def opens_after_6pm(hours_field):
    if hours_field is None:
        return False
    if isinstance(hours_field, str) and hours_field.strip().lower() in ('none', 'null', ''):
        return False
    # hours_field is expected to be a JSON string representing a list of [day, times]
    try:
        hrs = json.loads(hours_field)
    except Exception:
        return False
    for entry in hrs:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(times, str):
            continue
        if 'Closed' in times or times.strip().lower() == 'closed':
            continue
        # split start and end by various dashes
        parts = re.split(r'\s*[–—-]\s*', times)
        if len(parts) < 2:
            continue
        end_time = parts[-1]
        end_minutes = parse_time_to_minutes(end_time)
        if end_minutes is None:
            continue
        if end_minutes > 18 * 60:  # after 6:00 PM
            return True
    return False

# Apply function
merged['open_after_6pm_weekday'] = merged['hours'].apply(opens_after_6pm)

# Filter businesses that are open after 6pm on at least one weekday
filtered = merged[merged['open_after_6pm_weekday'] == True].copy()

# Drop those without avg_rating
filtered = filtered[filtered['avg_rating'].notna()]

# Sort by avg_rating desc
filtered_sorted = filtered.sort_values(by='avg_rating', ascending=False)

# Take top 5
top5 = filtered_sorted.head(5)

# Prepare output
output = []
for _, row in top5.iterrows():
    output.append({
        'name': row.get('name'),
        'hours': row.get('hours'),
        'average_rating': round(float(row.get('avg_rating')), 2)
    })

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_SBXPJjiNV7jumUGUADFCIYzo': ['business_description'], 'var_call_2xoh2qOwpRh4fU6xTKNp3VVm': 'file_storage/call_2xoh2qOwpRh4fU6xTKNp3VVm.json', 'var_call_FZg7woBCJ10SxtPGJEHiHShF': 'file_storage/call_FZg7woBCJ10SxtPGJEHiHShF.json'}

exec(code, env_args)
