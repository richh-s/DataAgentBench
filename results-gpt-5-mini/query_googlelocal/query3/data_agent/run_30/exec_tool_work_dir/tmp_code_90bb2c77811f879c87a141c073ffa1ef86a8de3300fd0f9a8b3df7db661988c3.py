code = """import json, ast
from statistics import mean

# Load data
with open(var_call_XRKoqv0Eam6Wif5LPsj3iIR4, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_Rnt3UxB4mF55SHQqnLl8lCE7, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Compute average ratings per gmap_id
ratings = {}
for r in reviews:
    gid = r.get('gmap_id')
    try:
        val = float(r.get('rating'))
    except Exception:
        continue
    ratings.setdefault(gid, []).append(val)
avg_rating = {k: mean(v) for k, v in ratings.items()}

WEEKDAYS = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_time(s):
    if not isinstance(s, str):
        return None
    t = s.strip().upper().replace(' ', '')
    if t.endswith('AM') or t.endswith('PM'):
        ampm = t[-2:]
        body = t[:-2]
    else:
        return None
    if ':' in body:
        parts = body.split(':')
        if len(parts) != 2:
            return None
        h = parts[0]; m = parts[1]
    else:
        h = body; m = '0'
    try:
        h = int(h); m = int(m)
    except Exception:
        return None
    if ampm == 'AM':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return h * 60 + m

def open_after_6pm(hours_field):
    if hours_field is None:
        return False
    if isinstance(hours_field, str):
        if hours_field.strip().lower() == 'none':
            return False
        try:
            hrs = ast.literal_eval(hours_field)
        except Exception:
            return False
    else:
        hrs = hours_field
    if not isinstance(hrs, list):
        return False
    for entry in hrs:
        if not entry or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEKDAYS:
            continue
        if not isinstance(times, str):
            continue
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
            if ct > 18 * 60:
                return True
    return False

results = []
for b in businesses:
    gid = b.get('gmap_id')
    if gid not in avg_rating:
        continue
    if open_after_6pm(b.get('hours')):
        try:
            nr = int(b.get('num_of_reviews') or 0)
        except Exception:
            nr = 0
        results.append({'name': b.get('name'), 'hours': b.get('hours'), 'avg_rating': round(avg_rating[gid], 2), 'num_of_reviews': nr})

results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], -x['num_of_reviews'], x['name'] or ''))
top5 = results_sorted[:5]

if not top5:
    output = 'No businesses found that are open after 6:00 PM on a weekday.'
else:
    lines = []
    idx = 1
    for r in top5:
        line = str(idx) + '. ' + (r.get('name') or '') + ' | Hours: ' + str(r.get('hours')) + ' | Average rating: ' + str(r.get('avg_rating'))
        lines.append(line)
        idx += 1
    output = '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_XRKoqv0Eam6Wif5LPsj3iIR4': 'file_storage/call_XRKoqv0Eam6Wif5LPsj3iIR4.json', 'var_call_Rnt3UxB4mF55SHQqnLl8lCE7': 'file_storage/call_Rnt3UxB4mF55SHQqnLl8lCE7.json'}

exec(code, env_args)
