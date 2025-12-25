code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-3389794052004706370']

# Load the business data
with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def is_open_after_6pm(time_str):
    if not time_str or time_str == "Closed":
        return False
    if time_str == "Open 24 hours":
        return True
    
    # Split by the separator (en-dash or similar)
    parts = re.split(r'[\u2013\-\u2014]', time_str)
    if len(parts) < 2:
        return False
    
    end_time_str = parts[-1].strip()
    
    # Parse end time
    match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', end_time_str, re.IGNORECASE)
    if not match:
        return False
    
    hour = int(match.group(1))
    minute = int(match.group(2) or 0)
    period = match.group(3).upper()
    
    if period == "PM":
        if hour != 12:
            hour += 12
    elif period == "AM":
        if hour == 12:
            hour = 0
            
    # Check if strictly after 18:00
    if hour > 18:
        return True
    if hour == 18 and minute > 0:
        return True
    # If it closes early morning (next day), it means it was open past 6PM
    if 0 <= hour < 6:
        return True
        
    return False

filtered_businesses = []
for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        hours_list = json.loads(hours_str)
    except:
        continue
        
    open_late = False
    for day_info in hours_list:
        if len(day_info) != 2:
            continue
        day, time_range = day_info
        if day in weekdays:
            if is_open_after_6pm(time_range):
                open_late = True
                break
    
    if open_late:
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-641724158129676975': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-18196666654569981474': [{'count': '79'}], 'var_function-call-3389794052004706370': 'file_storage/function-call-3389794052004706370.json'}

exec(code, env_args)
