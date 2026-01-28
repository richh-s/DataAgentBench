code = """import json
import pandas as pd
from datetime import datetime

# Load data from previous tool results
with open(var_call_vjrjbt3i4YlD1HbBrNy0JlLP, 'r') as f:
    businesses = json.load(f)
with open(var_call_eAcgFTI4lzy3Kbvy1ZnHbKMt, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
biz_df = pd.DataFrame(businesses)
rev_df = pd.DataFrame(reviews)

# Normalize review ratings to numeric
if not rev_df.empty:
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
else:
    rev_df['rating'] = pd.Series(dtype=float)

# Compute average rating per gmap_id
avg_ratings = rev_df.groupby('gmap_id', dropna=True)['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Helper to parse closing time and check > 6:00 PM
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time(t):
    t = t.strip().upper()
    # Remove spaces before AM/PM if any
    t = t.replace(' ', '')
    for fmt in ('%I:%M%p','%I%p'):
        try:
            return datetime.strptime(t, fmt).time()
        except Exception:
            pass
    return None


def closes_after_6pm(hours_field):
    if not hours_field or hours_field in (None, 'None'):
        return False
    try:
        # hours_field is a JSON string like [["Thursday", "6:30AM–6PM"], ...]
        hours_list = json.loads(hours_field)
    except Exception:
        return False
    for entry in hours_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        timestr = entry[1]
        if day not in weekdays:
            continue
        if not timestr or (isinstance(timestr, str) and timestr.strip().lower() == 'closed'):
            continue
        # Normalize dash characters
        timestr_norm = timestr.replace('\u2013', '-').replace('\u2014','-').replace('–','-').replace('—','-')
        parts = timestr_norm.split('-')
        if len(parts) < 2:
            continue
        close_part = parts[-1].strip()
        close_time = parse_time(close_part)
        if close_time is None:
            continue
        # Check strictly greater than 18:00
        minutes = close_time.hour * 60 + close_time.minute
        if minutes > 18*60:
            return True
    return False

# Apply to businesses
biz_df['open_after_6pm_weekday'] = biz_df['hours'].apply(closes_after_6pm)

# Merge with avg ratings
merged = pd.merge(biz_df, avg_ratings, on='gmap_id', how='left')
# Exclude those without average ratings
merged = merged[merged['average_rating'].notna()]
# Filter open after 6pm on at least one weekday
filtered = merged[merged['open_after_6pm_weekday']]

# Sort by average_rating desc and take top 5
top5 = filtered.sort_values(by='average_rating', ascending=False).head(5)

# Prepare result
result = []
for _, row in top5.iterrows():
    result.append({
        'name': row.get('name'),
        'hours': row.get('hours'),
        'average_rating': round(float(row.get('average_rating')), 2)
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zWYkKq9kaLlMDaKvrNU5QeC5': ['business_description'], 'var_call_aCb1tI0lttoavdiMhmj84xXz': ['review'], 'var_call_vjrjbt3i4YlD1HbBrNy0JlLP': 'file_storage/call_vjrjbt3i4YlD1HbBrNy0JlLP.json', 'var_call_eAcgFTI4lzy3Kbvy1ZnHbKMt': 'file_storage/call_eAcgFTI4lzy3Kbvy1ZnHbKMt.json'}

exec(code, env_args)
