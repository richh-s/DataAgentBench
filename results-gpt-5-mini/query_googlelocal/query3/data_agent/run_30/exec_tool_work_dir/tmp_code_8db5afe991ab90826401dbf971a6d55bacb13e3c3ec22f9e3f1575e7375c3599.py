code = """import json, re
from statistics import mean

# Load filtered businesses and reviews
with open(var_call_Pohj0i9rMou8ZjhzB4KWAXWC, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_Rnt3UxB4mF55SHQqnLl8lCE7, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# compute average ratings
ratings = {}
for r in reviews:
    gid = r.get('gmap_id')
    try:
        val = float(r.get('rating'))
    except Exception:
        continue
    ratings.setdefault(gid, []).append(val)
avg = {k: mean(v) for k, v in ratings.items()}

# parse time to minutes since midnight
def parse_time(s):
    if not isinstance(s, str):
        return None
    s2 = s.strip().upper().replace(' ', '')
    if s2.endswith('AM') or s2.endswith('PM'):
        ampm = s2[-2:]
        body = s2[:-2]
    else:
        return None
    if ':' in body:
        parts = body.split(':')
        if len(parts) != 2:
            return None
        try:
            h = int(parts[0]); m = int(parts[1])
        except Exception:
            return None
    else:
        try:
            h = int(body); m = 0
        except Exception:
            return None
    if ampm == 'AM':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return h*60 + m

WEEK = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def open_after_6pm(hours_field):
    if not hours_field or not isinstance(hours_field, str):
        return False
    try:
        hours_list = json.loads(hours_field)
    except Exception:
        # fallback to eval-like parsing
        try:
            import ast
            hours_list = ast.literal_eval(hours_field)
        except Exception:
            return False
    if not isinstance(hours_list, list):
        return False
    for entry in hours_list:
        if not entry or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in WEEK:
            continue
        if not isinstance(times, str):
            continue
        if 'closed' in times.lower():
            continue
        # split on commas for multiple ranges
        ranges = [p.strip() for p in times.split(',') if p.strip()]
        for r in ranges:
            # split on dash or unicode dash characters
            parts = re.split('[-–—]', r)
            if len(parts) < 2:
                continue
            close_part = parts[-1]
            ct = parse_time(close_part)
            if ct is None:
                continue
            if ct > 18*60:
                return True
    return False

candidates = []
for b in businesses:
    gid = b.get('gmap_id')
    if gid not in avg:
        continue
    if open_after_6pm(b.get('hours')):
        try:
            nr = int(b.get('num_of_reviews') or 0)
        except Exception:
            nr = 0
        candidates.append({'name': b.get('name'), 'hours': b.get('hours'), 'avg_rating': round(avg[gid],2), 'num_of_reviews': nr})

candidates.sort(key=lambda x: (-x['avg_rating'], -x['num_of_reviews'], x['name'] or ''))
top5 = candidates[:5]

if not top5:
    out_text = 'No businesses found that are open after 6:00 PM on a weekday.'
else:
    lines = []
    i = 1
    for r in top5:
        lines.append(str(i) + '. ' + (r.get('name') or '') + ' | Hours: ' + str(r.get('hours')) + ' | Average rating: ' + str(r.get('avg_rating')))
        i += 1
    out_text = '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(out_text))"""

env_args = {'var_call_XRKoqv0Eam6Wif5LPsj3iIR4': 'file_storage/call_XRKoqv0Eam6Wif5LPsj3iIR4.json', 'var_call_Rnt3UxB4mF55SHQqnLl8lCE7': 'file_storage/call_Rnt3UxB4mF55SHQqnLl8lCE7.json', 'var_call_Pohj0i9rMou8ZjhzB4KWAXWC': [{'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'num_of_reviews': '18'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'num_of_reviews': '6'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'num_of_reviews': '26'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'num_of_reviews': '8'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'num_of_reviews': '8'}, {'name': 'J B Oriental Inc', 'gmap_id': 'gmap_32', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'num_of_reviews': '6'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]', 'num_of_reviews': '15'}, {'name': 'The Beauty Bar', 'gmap_id': 'gmap_30', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'num_of_reviews': '21'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53', 'hours': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]', 'num_of_reviews': '38'}, {'name': 'Excel Hair & Nails', 'gmap_id': 'gmap_65', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]', 'num_of_reviews': '52'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'num_of_reviews': '18'}, {'name': 'Beauty Divine Artistry', 'gmap_id': 'gmap_36', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'num_of_reviews': '8'}, {'name': 'White Barn Candle Co', 'gmap_id': 'gmap_12', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'num_of_reviews': '2'}, {'name': "Rossy's Beauty Salon", 'gmap_id': 'gmap_7', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'num_of_reviews': '37'}, {'name': 'TACOS LA CABANA', 'gmap_id': 'gmap_8', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'num_of_reviews': '2'}, {'name': 'Paradise tattoo', 'gmap_id': 'gmap_11', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]', 'num_of_reviews': '378'}, {'name': 'Off The Hoof', 'gmap_id': 'gmap_61', 'hours': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]', 'num_of_reviews': '3'}, {'name': 'Advanced Auto Upholstery', 'gmap_id': 'gmap_68', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]', 'num_of_reviews': '4'}, {'name': 'LuXe Organic Nails Boutique', 'gmap_id': 'gmap_67', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]', 'num_of_reviews': '31'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'hours': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'num_of_reviews': '35'}, {'name': 'The Dream Junction', 'gmap_id': 'gmap_60', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]', 'num_of_reviews': '48'}]}

exec(code, env_args)
