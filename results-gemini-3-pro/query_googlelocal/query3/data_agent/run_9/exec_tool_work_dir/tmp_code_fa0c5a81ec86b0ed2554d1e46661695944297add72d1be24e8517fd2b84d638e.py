code = """import json
import re
import os

# Get the file path from the previous result variable
file_path = locals()['var_function-call-11765510306618497496']

with open(file_path, 'r') as f:
    businesses = json.load(f)

def parse_time(time_str):
    if not time_str:
        return None
    match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', time_str, re.IGNORECASE)
    if not match:
        return None
    hour = int(match.group(1))
    minute = int(match.group(2) or 0)
    period = match.group(3).upper()
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    return hour + minute / 60.0

def is_open_late(hours_json):
    if not hours_json or hours_json == 'None':
        return False
    try:
        hours_list = json.loads(hours_json.replace("'", '"')) # Simple fix for quotes if any
    except:
        return False
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        if day in weekdays:
            if 'Open 24 hours' in time_range:
                return True
            if 'Closed' in time_range:
                continue
            
            # Handle en-dash or hyphen
            times = re.split(r'\u2013|-', time_range)
            if len(times) == 2:
                end_time_str = times[1].strip()
                end_time = parse_time(end_time_str)
                if end_time is not None:
                    # PM hours: > 18.0
                    is_pm = 'PM' in end_time_str.upper()
                    is_am = 'AM' in end_time_str.upper()
                    if is_pm:
                         if end_time > 18.001: 
                             return True
                    elif is_am:
                         # Closing in AM usually means late night (after midnight)
                         # Unless it's a morning shift (e.g., 10 AM).
                         # Assuming < 5 AM is late night.
                         if end_time == 0.0 or end_time <= 5.0:
                             return True
    return False

late_businesses = []
for b in businesses:
    if is_open_late(b['hours']):
        late_businesses.append(b)

print("__RESULT__:")
print(json.dumps(late_businesses))"""

env_args = {'var_function-call-17526194597046591921': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-12219215353860809743': [{'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}], 'var_function-call-8631971219953678902': [{'count': '66'}], 'var_function-call-11765510306618497496': 'file_storage/function-call-11765510306618497496.json'}

exec(code, env_args)
