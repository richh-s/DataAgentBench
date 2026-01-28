code = """import json
import ast
from statistics import mean

# Load data from storage-provided file paths
with open(var_call_XRKoqv0Eam6Wif5LPsj3iIR4, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_Rnt3UxB4mF55SHQqnLl8lCE7, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Compute average ratings per gmap_id
ratings_by_id = {}
for r in reviews:
    gid = r.get('gmap_id')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings_by_id.setdefault(gid, []).append(rating)

avg_rating = {gid: mean(vals) for gid, vals in ratings_by_id.items()}

# Helper to parse time like '9:30AM' or '9AM'
def parse_time(t):
    t = t.strip().upper()
    # remove spaces
    t = t.replace(' ', '')
    # handle missing AM/PM
    if t.endswith('AM') or t.endswith('PM'):
        ampm = t[-2:]
        body = t[:-2]
    else:
        return None
    if ':' in body:
        h, m = body.split(':')
    else:
        h, m = body, '0'
    try:
        h = int(h)
        m = int(m)
    except:
        return None
    if ampm == 'AM':
        if h == 12:
            h = 0
    else:  # PM
        if h != 12:
            h += 12
    return h * 60 + m

# Check if closing time is after 6:00 PM (18:00 -> 1080 minutes)
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def open_after_6pm(hours_field):
    if hours_field is None:
        return False
    if isinstance(hours_field, str):
        if hours_field.strip().lower() == 'none':
            return False
        try:
            hours_list = ast.literal_eval(hours_field)
        except Exception:
            return False
    else:
        hours_list = hours_field
    # hours_list expected like [["Thursday", "6:30AM-6PM"], ...]
    for entry in hours_list:
        if not entry or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        if times is None:
            continue
        times = times.replace('\u2013','-').replace('\u2014','-')
        if 'closed' in times.lower():
            continue
        # Some entries might have multiple ranges separated by comma; check each
        ranges = [r.strip() for r in times.split(',') if r.strip()]
        for r in ranges:
            if '-' not in r:
                continue
            parts = r.split('-')
            if len(parts) < 2:
                continue
            close_part = parts[-1]
            ct = parse_time(close_part)
            if ct is None:
                continue
            if ct > 18*60:  # strictly after 6:00 PM
                return True
    return False

# Build list of businesses with avg rating and whether open after 6pm on a weekday
results = []
for b in businesses:
    gid = b.get('gmap_id')
    if gid not in avg_rating:
        continue
    avg = avg_rating[gid]
    hours_field = b.get('hours')
    if open_after_6pm(hours_field):
        results.append({'name': b.get('name'), 'gmap_id': gid, 'hours': hours_field, 'avg_rating': round(avg, 2), 'num_of_reviews': int(b.get('num_of_reviews') or 0)})

# Sort by avg_rating desc, then by num_of_reviews desc
results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], -x['num_of_reviews'], x['name']))

top5 = results_sorted[:5]

# Prepare plain-text answer
if not top5:
    final_text = 'No businesses found that are open after 6:00 PM on a weekday.'
else:
    lines = []
    for i, r in enumerate(top5, start=1):
        lines.append(f"{i}. {r['name']} | Hours: {r['hours']} | Average rating: {r['avg_rating']}")
    final_text = '\n'.join(lines)

# Print in required format as a JSON string
print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_XRKoqv0Eam6Wif5LPsj3iIR4': 'file_storage/call_XRKoqv0Eam6Wif5LPsj3iIR4.json', 'var_call_Rnt3UxB4mF55SHQqnLl8lCE7': 'file_storage/call_Rnt3UxB4mF55SHQqnLl8lCE7.json'}

exec(code, env_args)
