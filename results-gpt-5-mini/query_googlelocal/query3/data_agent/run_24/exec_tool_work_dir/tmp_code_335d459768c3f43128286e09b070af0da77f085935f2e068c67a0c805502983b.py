code = """import json, ast, re
path = var_call_NcRqDh2BgzigD8PzoEqDbVy0
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

weekdays = set(["Monday","Tuesday","Wednesday","Thursday","Friday"])

def parse_time_to_minutes(t):
    # t expected like '6:30PM' or '6PM' possibly with spaces
    t = t.strip()
    # find hour, minute, meridiem
    m = re.search(r"(\d{1,2})(?::(\d{2}))?\s*([AaPp][Mm])?", t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    mer = m.group(3)
    if mer:
        mer = mer.upper()
        if mer == 'AM':
            if hour == 12:
                hour24 = 0
            else:
                hour24 = hour
        else: # PM
            if hour == 12:
                hour24 = 12
            else:
                hour24 = hour + 12
    else:
        # assume no meridiem -> ambiguous; return None
        return None
    return hour24*60 + minute

matches = []
for r in rows:
    hours_str = r.get('hours')
    if not hours_str:
        continue
    # normalize dashes
    s = hours_str.replace('\u2013','-').replace('\u2014','-')
    try:
        hours_list = ast.literal_eval(s)
    except Exception:
        # fallback: try to extract pairs via regex
        continue
    open_after_6 = False
    for pair in hours_list:
        if not isinstance(pair, (list, tuple)) or len(pair) < 2:
            continue
        day = pair[0]
        times = pair[1]
        if day not in weekdays:
            continue
        if not times or 'Closed' in times or 'closed' in times:
            continue
        # split start-end
        parts = re.split(r"[-–—]", times)
        if len(parts) < 2:
            continue
        end = parts[1]
        end_min = parse_time_to_minutes(end)
        if end_min is None:
            continue
        if end_min > 18*60:
            open_after_6 = True
            break
    if open_after_6:
        matches.append({
            'gmap_id': r.get('gmap_id'),
            'name': r.get('name'),
            'hours': r.get('hours')
        })

import json
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_pD6QWRPutNwWraf0FlIDLErF': ['business_description'], 'var_call_NcRqDh2BgzigD8PzoEqDbVy0': 'file_storage/call_NcRqDh2BgzigD8PzoEqDbVy0.json'}

exec(code, env_args)
