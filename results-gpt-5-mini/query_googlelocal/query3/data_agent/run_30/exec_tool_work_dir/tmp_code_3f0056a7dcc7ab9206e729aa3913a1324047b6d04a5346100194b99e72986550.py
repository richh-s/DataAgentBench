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
    if not isinstance(t, str):
        return None
    s = t.strip().upper().replace(' ', '')
    if s.endswith('AM') or s.endswith('PM'):
        ampm = s[-2:]
        body = s[:-2]
    else:
        return None
    if ':' in body:
        try:
            h, m = body.split(':')
        except:
            return None
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
    else:
        if h != 12:
            h += 12
    return h * 60 + m

WEEKDAYS = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

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
    if not isinstance(hours_list, list):
        return False
    for entry in hours_list:
        if not entry or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        if not times or not isinstance(times, str):
            continue
        # Normalize dashes
        times = times.replace('–', '-').replace('—', '-')
        if 'closed' in times.lower():
            continue
        ranges = [r.strip() for r in times.split(',') if r.strip()]
        for r in ranges:
            if '-' not in r:
                continue
            parts = r.split('-')
            close_part = parts[-1]
            ct = parse_time(close_part)
            if ct is None:
                continue
            if ct > 18*60:
                return True
    return False

results = []
for b in businesses:
    gid = b.get('gmap_id')
    if gid not in avg_rating:
        continue
    avg = avg_rating[gid]
    hours_field = b.get('hours')
    if open_after_6pm(hours_field):
        try:
            num_rev = int(b.get('num_of_reviews') or 0)
        except:
            num_rev = 0
        results.append({'name': b.get('name'), 'gmap_id': gid, 'hours': hours_field, 'avg_rating': round(avg, 2), 'num_of_reviews': num_rev})

results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], -x['num_of_reviews'], x['name'] or ''))

top5 = results_sorted[:5]

if not top5:
    final_text = 'No businesses found that are open after 6:00 PM on a weekday.'
else:
    lines = []
    for i, r in enumerate(top5, start=1):
        lines.append(str(i) + '. ' + (r.get('name') or '') + ' | Hours: ' + (str(r.get('hours')) or '') + ' | Average rating: ' + str(r.get('avg_rating')))
    final_text = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_XRKoqv0Eam6Wif5LPsj3iIR4': 'file_storage/call_XRKoqv0Eam6Wif5LPsj3iIR4.json', 'var_call_Rnt3UxB4mF55SHQqnLl8lCE7': 'file_storage/call_Rnt3UxB4mF55SHQqnLl8lCE7.json'}

exec(code, env_args)
