code = """import json, ast
from statistics import mean
with open(var_call_XRKoqv0Eam6Wif5LPsj3iIR4, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_Rnt3UxB4mF55SHQqnLl8lCE7, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
ratings = {}
for r in reviews:
    gid = r.get('gmap_id')
    try:
        val = float(r.get('rating'))
    except:
        continue
    ratings.setdefault(gid, []).append(val)
avg = {k: mean(v) for k, v in ratings.items()}
WEEK = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

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
        if len(parts)!=2:
            return None
        h = parts[0]; m = parts[1]
    else:
        h = body; m = '0'
    try:
        h = int(h); m = int(m)
    except:
        return None
    if ampm == 'AM':
        if h==12: h = 0
    else:
        if h!=12: h += 12
    return h*60 + m

import math

def open_after_6(hours_field):
    if hours_field is None: return False
    if isinstance(hours_field, str):
        if hours_field.strip().lower()=='none': return False
        try:
            hrs = ast.literal_eval(hours_field)
        except:
            return False
    else:
        hrs = hours_field
    if not isinstance(hrs, list): return False
    for entry in hrs:
        if not entry or len(entry)<2: continue
        day = entry[0]
        times = entry[1]
        if day not in WEEK: continue
        if not isinstance(times, str): continue
        times = times.replace('\u2013','-').replace('\u2014','-').replace('–','-').replace('—','-')
        if 'closed' in times.lower(): continue
        parts = [p.strip() for p in times.split(',') if p.strip()]
        for p in parts:
            if '-' not in p: continue
            cp = p.split('-')[-1]
            ct = parse_time(cp)
            if ct is None: continue
            if ct > 18*60:
                return True
    return False

out = []
for b in businesses:
    gid = b.get('gmap_id')
    if gid not in avg: continue
    if open_after_6(b.get('hours')):
        try:
            nr = int(b.get('num_of_reviews') or 0)
        except:
            nr = 0
        out.append({'name': b.get('name'), 'hours': b.get('hours'), 'avg_rating': round(avg[gid],2), 'num_of_reviews': nr})

out = sorted(out, key=lambda x: (-x['avg_rating'], -x['num_of_reviews'], x['name'] or ''))[:5]
if not out:
    result_text = 'No businesses found that are open after 6:00 PM on a weekday.'
else:
    lines = []
    i = 1
    for r in out:
        lines.append(f"{i}. {r['name']} | Hours: {r['hours']} | Average rating: {r['avg_rating']}")
        i += 1
    result_text = '\n'.join(lines)
print('__RESULT__:')
print(json.dumps(result_text))"""

env_args = {'var_call_XRKoqv0Eam6Wif5LPsj3iIR4': 'file_storage/call_XRKoqv0Eam6Wif5LPsj3iIR4.json', 'var_call_Rnt3UxB4mF55SHQqnLl8lCE7': 'file_storage/call_Rnt3UxB4mF55SHQqnLl8lCE7.json'}

exec(code, env_args)
