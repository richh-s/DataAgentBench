code = """import json
import pandas as pd
import ast
import re

# Load data from previous tool calls (file paths)
with open(var_call_d9mAcES9urkQX8Tok78ugQiE, 'r', encoding='utf-8') as f:
    biz = json.load(f)
with open(var_call_8rRKygM9Kz5TiWISPpQTnoAE, 'r', encoding='utf-8') as f:
    rev = json.load(f)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# Ensure ratings numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Compute average rating per gmap_id
avg_rating = rev_df.groupby('gmap_id', dropna=True)['rating'].mean().reset_index()
avg_rating.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Merge with business info
merged = pd.merge(biz_df, avg_rating, on='gmap_id', how='inner')

# Helper to parse time like '6:30PM' or '6PM'
def parse_time(t):
    t = t.strip()
    # remove any spaces before AM/PM
    t = re.sub(r"\s+([AP]M)$", r"\1", t, flags=re.IGNORECASE)
    m = re.match(r'(?i)^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$', t)
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

# Check if closing time > 18:00 (1080 minutes)
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def closes_after_6pm(hours_field):
    if not hours_field or hours_field == 'None':
        return False
    # hours_field is a string representation of a list; try to literal_eval
    try:
        hlist = ast.literal_eval(hours_field)
    except Exception:
        return False
    for entry in hlist:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        if not times or 'Closed' in times or 'closed' in times:
            continue
        # split on dash or en-dash
        parts = re.split(r'[\-\u2013\u2014–—]', times)
        if len(parts) < 2:
            continue
        closing = parts[1].strip()
        # Sometimes closing contains extra text like '9:30PM"' – strip non print
        closing = re.sub(r'[^0-9APMapm:\.]', '', closing)
        # Ensure AM/PM present; if not, assume same as start? skip if missing
        if not re.search(r'[APap][Mm]$', closing):
            # try to find AM/PM elsewhere in the string
            if re.search(r'[APap][Mm]', times):
                # extract last AM/PM occurrence
                ampm = re.findall(r'[APap][Mm]', times)[-1]
                closing = closing + ampm
            else:
                continue
        mins = parse_time(closing)
        if mins is None:
            continue
        if mins > 18*60:
            return True
    return False

# Apply filter
merged['opens_after_6pm_weekday'] = merged['hours'].apply(closes_after_6pm)
filtered = merged[merged['opens_after_6pm_weekday'] == True].copy()

# Sort by avg_rating desc
filtered['avg_rating'] = filtered['avg_rating'].astype(float)
filtered_sorted = filtered.sort_values(by=['avg_rating','name'], ascending=[False, True])

# Take top 5
top5 = filtered_sorted.head(5)

# Prepare output
output = []
for _, row in top5.iterrows():
    output.append({
        'name': row['name'],
        'hours': row['hours'],
        'average_rating': round(float(row['avg_rating']), 2)
    })

result_str = json.dumps(output)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_PDGF1kFBtlFSAf4bIcUXVaNW': ['business_description'], 'var_call_d9mAcES9urkQX8Tok78ugQiE': 'file_storage/call_d9mAcES9urkQX8Tok78ugQiE.json', 'var_call_5hJm4r28HYMUGawoGHmV67Wx': ['review'], 'var_call_8rRKygM9Kz5TiWISPpQTnoAE': 'file_storage/call_8rRKygM9Kz5TiWISPpQTnoAE.json'}

exec(code, env_args)
