code = """import json, pandas as pd
path = var_call_b3E3FB3HeNXlGKzo8SntTkh2
with open(path, 'r') as f:
    data = json.load(f)

def parse_time(t):
    t = t.strip()
    if t == 'Open 24 hours':
        return 24*60
    import re
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', t)
    if not m:
        return None
    h = int(m.group(1))
    mnt = int(m.group(2) or 0)
    ampm = m.group(3)
    if h == 12:
        h = 0
    if ampm == 'PM':
        h += 12
    return h*60 + mnt

eligible = []
weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}
for row in data:
    hrs = json.loads(row['hours']) if isinstance(row['hours'], str) else row['hours']
    open_late = False
    for day, span in hrs:
        if day not in weekdays:
            continue
        if span == 'Closed':
            continue
        if span == 'Open 24 hours':
            open_late = True
            break
        parts = span.split('') if '\u2013' not in span else span.split('')
        parts = span.split('')
        parts = span.split('')
        # correct dash
        parts = span.split('\u2013')
        if len(parts) != 2:
            continue
        close_t = parse_time(parts[1])
        if close_t is None:
            continue
        if close_t > 18*60:
            open_late = True
            break
    if open_late:
        eligible.append({'name': row['name'], 'gmap_id': row['gmap_id'], 'hours': hrs})

result = json.dumps(eligible)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_b3E3FB3HeNXlGKzo8SntTkh2': 'file_storage/call_b3E3FB3HeNXlGKzo8SntTkh2.json'}

exec(code, env_args)
