code = """import json, ast
# load the business query result from storage
with open(var_call_E7BHvPuTsK4uxmlT2A8tJwGF, 'r') as f:
    data = json.load(f)

# helper to parse time strings like '9:30AM-10PM' or '9AM-5PM' or 'Closed'
from datetime import datetime

def parse_time_str(t):
    t = t.replace('\u2013', '-')
    t = t.replace('\u2014', '-')
    if t.strip().lower() == 'closed':
        return None, None
    parts = t.split('-')
    if len(parts) != 2:
        return None, None
    def to_minutes(x):
        x = x.strip().upper()
        # ensure there is AM/PM
        if x.endswith('AM') or x.endswith('PM'):
            pass
        else:
            return None
        # parse hour and optional minute
        try:
            if ':' in x:
                hh, mm_ampm = x.split(':')
                mm = mm_ampm[:-2]
                ampm = mm_ampm[-2:]
                hour = int(hh)
                minute = int(mm)
            else:
                hour = int(x[:-2])
                minute = 0
                ampm = x[-2:]
        except:
            return None
        if ampm == 'AM':
            if hour == 12:
                hour = 0
        else: # PM
            if hour != 12:
                hour += 12
        return hour*60 + minute
    start = to_minutes(parts[0])
    end = to_minutes(parts[1])
    return start, end

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

candidates = []
for rec in data:
    hours_str = rec.get('hours')
    if not hours_str:
        continue
    # convert string representation to Python list
    try:
        hrs = ast.literal_eval(hours_str)
    except Exception:
        # try replacing en dash and then eval
        try:
            hrs = ast.literal_eval(hours_str.replace('\u2013', '-'))
        except Exception:
            continue
    qualifies = False
    for day, times in hrs:
        if day in weekdays:
            if isinstance(times, str) and times.strip().lower() != 'closed':
                start,end = parse_time_str(times)
                if end is not None and end > 18*60:
                    qualifies = True
                    break
    if qualifies:
        candidates.append({'gmap_id': rec.get('gmap_id'), 'name': rec.get('name'), 'hours': hours_str})

# print results as JSON string
result = json.dumps(candidates)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Vme3bfilwLQFECZw36MdKjKI': ['review'], 'var_call_kgWScFfZGcFoDd20ucwVndlP': ['business_description'], 'var_call_E7BHvPuTsK4uxmlT2A8tJwGF': 'file_storage/call_E7BHvPuTsK4uxmlT2A8tJwGF.json'}

exec(code, env_args)
