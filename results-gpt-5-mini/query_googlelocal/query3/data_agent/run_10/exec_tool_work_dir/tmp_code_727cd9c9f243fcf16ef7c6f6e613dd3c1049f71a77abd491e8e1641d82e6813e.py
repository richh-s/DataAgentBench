code = """import json
import ast
from datetime import datetime

def parse_time(t):
    # t like '9:30AM', '6PM', possibly with spaces
    t = t.strip().upper().replace(' ', '')
    try:
        return datetime.strptime(t, '%I:%M%p').time()
    except Exception:
        try:
            return datetime.strptime(t, '%I%p').time()
        except Exception:
            return None


def time_to_minutes(t):
    return t.hour*60 + t.minute

# load data from storage-provided file paths
with open(var_call_rLSBdlFWPgCED8v5CZiTJ1t8, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_rM12nRDmbF4o8QHKvnLbQLm4, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Build ratings dict: avg rating per gmap_id
from collections import defaultdict
ratings = defaultdict(list)
for r in reviews:
    gid = r.get('gmap_id')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings[gid].append(rating)

avg_ratings = {gid: (sum(vals)/len(vals) if len(vals)>0 else None, len(vals)) for gid, vals in ratings.items()}

# Weekday set
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

qualified = []
for b in businesses:
    gid = b.get('gmap_id')
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw in ['None', None]:
        continue
    # hours_raw is a string representation of list; try to literal_eval
    try:
        hours_list = ast.literal_eval(hours_raw)
    except Exception:
        # if it's already a list
        hours_list = hours_raw
    # Ensure hours_list is iterable of pairs
    try:
        # build dict day->time_range
        day_to_times = {entry[0]: entry[1] for entry in hours_list}
    except Exception:
        continue
    stays_open_after_6 = False
    for day in weekdays:
        if day in day_to_times:
            tr = day_to_times[day]
            if not tr or 'Closed' in tr or 'closed' in tr:
                continue
            # split on dash or en-dash
            if '\u2013' in tr:
                parts = tr.split('\u2013')
            elif '\u2014' in tr:
                parts = tr.split('\u2014')
            elif '–' in tr:
                parts = tr.split('–')
            elif '-' in tr:
                parts = tr.split('-')
            else:
                # unknown format
                continue
            if len(parts) < 2:
                continue
            close_str = parts[-1]
            # Sometimes close_str contains text like '9:30PM' or '9:30PM '
            close_time = parse_time(close_str)
            if close_time is None:
                continue
            if time_to_minutes(close_time) > 18*60:
                stays_open_after_6 = True
                break
    if stays_open_after_6:
        avg, count = avg_ratings.get(gid, (None, 0))
        if avg is None:
            continue
        qualified.append({
            'name': b.get('name'),
            'gmap_id': gid,
            'hours': hours_raw,
            'average_rating': round(avg, 2),
            'num_ratings': count
        })

# Sort by average_rating desc, then by num_ratings desc
qualified_sorted = sorted(qualified, key=lambda x: (-x['average_rating'], -x['num_ratings']))
top5 = qualified_sorted[:5]

# Prepare output list with required fields
output = [{'name': t['name'], 'hours': t['hours'], 'average_rating': t['average_rating']} for t in top5]

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ms6dpanF85ltDZhQeMMD5fya': ['business_description'], 'var_call_rLSBdlFWPgCED8v5CZiTJ1t8': 'file_storage/call_rLSBdlFWPgCED8v5CZiTJ1t8.json', 'var_call_UTVkROTFZ8yRvWG6hHcUHlCY': ['review'], 'var_call_rM12nRDmbF4o8QHKvnLbQLm4': 'file_storage/call_rM12nRDmbF4o8QHKvnLbQLm4.json'}

exec(code, env_args)
