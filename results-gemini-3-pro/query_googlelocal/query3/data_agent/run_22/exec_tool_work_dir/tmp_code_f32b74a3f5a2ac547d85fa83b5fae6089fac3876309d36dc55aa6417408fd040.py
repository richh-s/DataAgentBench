code = """import json
import ast
import re

# Read the file containing business descriptions
with open(locals()['var_function-call-9478071719638559422'], 'r') as f:
    businesses = json.load(f)

weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def parse_time(t_str):
    # t_str like "6:30AM" or "6PM" or "12PM" (noon) or "12AM" (midnight)
    # returns minutes from midnight
    if not t_str: return None
    match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', t_str)
    if not match: return None
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    ampm = match.group(3)
    
    if ampm == 'PM' and h != 12:
        h += 12
    if ampm == 'AM' and h == 12:
        h = 0
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
        
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            if time_range == 'Closed':
                continue
            # "6:30AM–6PM"
            # Split by en-dash or hyphen. The data uses \u2013 (en-dash)
            # Unicode en-dash is \u2013.
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                open_time, close_time = parts
                close_minutes = parse_time(close_time)
                # 6:00 PM is 18*60 = 1080 minutes
                if close_minutes is not None and close_minutes > 1080:
                    return True
            elif '24 hours' in time_range:
                 return True
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-6152367786706215475': [{'name': 'City Textile', 'hours': 'None', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'gmap_id': 'gmap_45'}], 'var_function-call-5329146605310995410': [{'count': '79'}], 'var_function-call-9478071719638559422': 'file_storage/function-call-9478071719638559422.json'}

exec(code, env_args)
