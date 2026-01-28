code = """import json
import re

# Load data from storage variables
# var_call_GXW9sSUulZrKreEV0ivD6wu6 and var_call_dv6eCZ4frc9xhaeh0lLhEZhP are provided by tool results

def load_var(v):
    if isinstance(v, str):
        # Assume it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_data = load_var(var_call_GXW9sSUulZrKreEV0ivD6wu6)
review_data = load_var(var_call_dv6eCZ4frc9xhaeh0lLhEZhP)

# Helper to parse times
def parse_time(t):
    t = t.strip().upper()
    if t in ("CLOSED", ""):
        return None
    if '24' in t:
        # assume open 24 hours
        return 24*60-1
    # regex to extract hour, minute, AM/PM
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$", t)
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

# Helper to get closing time from a time range like '6:30AM–6PM'
def get_closing_minutes(range_str):
    if not range_str or 'CLOSED' in range_str.upper():
        return None
    # split on dash/en-dash/em-dash
    parts = re.split(r'[\u2013\u2014\-\u2012]', range_str)
    if len(parts) < 2:
        return None
    end = parts[-1].strip()
    return parse_time(end)

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

# Build average ratings per gmap_id
from collections import defaultdict
ratings = defaultdict(list)
for r in review_data:
    gid = r.get('gmap_id')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings[gid].append(rating)

avg_ratings = {gid: (sum(vals)/len(vals)) for gid, vals in ratings.items() if len(vals)>0}

# For each business, check hours
candidates = []
for b in business_data:
    gid = b.get('gmap_id')
    hours_field = b.get('hours')
    name = b.get('name')
    if not hours_field or hours_field == 'None':
        continue
    # hours_field is a string representation of a list
    try:
        hours_list = json.loads(hours_field)
    except Exception:
        # if not JSON, skip
        continue
    # find entries for weekdays
    open_after_6 = False
    for day, timestr in hours_list:
        if day in weekdays:
            if not timestr or 'Closed' in timestr or timestr.strip()=='' :
                continue
            close_min = get_closing_minutes(timestr)
            if close_min is None:
                continue
            if close_min > 18*60:
                open_after_6 = True
                break
    if open_after_6 and gid in avg_ratings:
        candidates.append({
            'gmap_id': gid,
            'name': name,
            'hours': hours_field,
            'average_rating': round(avg_ratings[gid], 2)
        })

# Sort by average_rating desc
candidates_sorted = sorted(candidates, key=lambda x: x['average_rating'], reverse=True)
# Take top 5
top5 = candidates_sorted[:5]

# Prepare JSON string
result_str = json.dumps(top5, ensure_ascii=False)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_GXW9sSUulZrKreEV0ivD6wu6': 'file_storage/call_GXW9sSUulZrKreEV0ivD6wu6.json', 'var_call_dv6eCZ4frc9xhaeh0lLhEZhP': 'file_storage/call_dv6eCZ4frc9xhaeh0lLhEZhP.json'}

exec(code, env_args)
