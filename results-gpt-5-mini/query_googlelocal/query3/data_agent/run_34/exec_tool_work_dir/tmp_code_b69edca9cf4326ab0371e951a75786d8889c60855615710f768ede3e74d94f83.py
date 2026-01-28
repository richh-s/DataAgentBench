code = """import json
import ast
import re

# Load data from previous tool calls
with open(var_call_5r1HG9AjipYAXr3BLW4VXr0Y, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_B06qUxga9Rf4uoypk4mpw9uo, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Build ratings by gmap_id
from collections import defaultdict
ratings = defaultdict(list)
for r in reviews:
    gid = r.get('gmap_id')
    rating = r.get('rating')
    try:
        rating_val = int(rating)
    except Exception:
        try:
            rating_val = int(float(rating))
        except Exception:
            continue
    ratings[gid].append(rating_val)

# Helper to parse end time into minutes since midnight
ampm_re = re.compile(r"(\d{1,2})(?::(\d{1,2}))?\s*([APap][Mm])")

def parse_time_to_minutes(tstr):
    if not tstr or tstr.strip().lower() in ('closed','none'):
        return None
    s = tstr.strip().replace('.', '')
    m = ampm_re.search(s)
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

# Weekdays set
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def hours_str_to_list(hstr):
    if not hstr or hstr.strip() in ('None', 'None'):
        return None
    try:
        # Some strings use unicode en-dash; literal_eval should handle
        parsed = ast.literal_eval(hstr)
        return parsed
    except Exception:
        # Try simple replacements and parsing
        try:
            s = hstr.replace('\u2013', '-')
            parsed = ast.literal_eval(s)
            return parsed
        except Exception:
            return None

# Identify businesses open after 6:00 PM on at least one weekday
qualifying = []
for b in businesses:
    gid = b.get('gmap_id')
    hstr = b.get('hours')
    parsed = hours_str_to_list(hstr)
    opens_after_6pm = False
    if parsed:
        for entry in parsed:
            try:
                day = entry[0]
                times = entry[1]
            except Exception:
                continue
            if day not in weekdays:
                continue
            if not times or 'Closed' in times or 'closed' in times:
                continue
            # normalize dashes
            times_norm = times.replace('\u2013','-').replace('\u2014','-').replace('–','-')
            if '-' not in times_norm:
                continue
            parts = times_norm.split('-')
            if len(parts) < 2:
                continue
            end = parts[-1].strip()
            end_min = parse_time_to_minutes(end)
            if end_min is None:
                continue
            if end_min > 18*60:
                opens_after_6pm = True
                break
    if opens_after_6pm and gid in ratings and len(ratings[gid])>0:
        avg = sum(ratings[gid]) / len(ratings[gid])
        qualifying.append({
            'name': b.get('name'),
            'gmap_id': gid,
            'hours': hstr,
            'average_rating': round(avg, 2),
            'num_reviews': len(ratings[gid])
        })

# Sort by average_rating desc, then num_reviews desc
qualifying_sorted = sorted(qualifying, key=lambda x: (-x['average_rating'], -x['num_reviews'], x['name']))

top5 = qualifying_sorted[:5]

# Prepare output (include only requested fields: names, operating hours, average ratings)
output = []
for item in top5:
    output.append({
        'name': item['name'],
        'hours': item['hours'],
        'average_rating': item['average_rating']
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Bedr9gwUOoIRbgBM5uHY8JFS': ['business_description'], 'var_call_5r1HG9AjipYAXr3BLW4VXr0Y': 'file_storage/call_5r1HG9AjipYAXr3BLW4VXr0Y.json', 'var_call_gKtPEzr5We7WC3El6VW75kFU': ['review'], 'var_call_B06qUxga9Rf4uoypk4mpw9uo': 'file_storage/call_B06qUxga9Rf4uoypk4mpw9uo.json'}

exec(code, env_args)
