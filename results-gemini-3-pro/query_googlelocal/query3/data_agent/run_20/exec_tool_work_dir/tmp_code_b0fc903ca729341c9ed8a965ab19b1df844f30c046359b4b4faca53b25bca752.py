code = """import json
import ast
import re

# Load businesses
with open(locals()['var_function-call-15796407158225419449'], 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # Returns minutes from midnight
    # t_str e.g. "6PM", "6:30PM", "12AM", "12:30PM"
    if t_str == "Open 24 hours":
        return 24 * 60 + 1 # Special value
    
    match = re.match(r"(\d+)(?::(\d+))?\s*(AM|PM)", t_str, re.IGNORECASE)
    if not match:
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    period = match.group(3).upper()
    
    if period == "PM" and h != 12:
        h += 12
    if period == "AM" and h == 12:
        h = 0
        
    return h * 60 + m

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

valid_businesses = []

for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == "None":
        continue
    
    try:
        # It seems the string is JSON format based on the preview (double quotes)
        # But let's use ast.literal_eval to be safe if it's mixed
        hours_list = json.loads(hours_str)
    except:
        try:
            hours_list = ast.literal_eval(hours_str)
        except:
            continue
            
    is_open_late = False
    
    for day_hours in hours_list:
        day, time_range = day_hours
        if day in weekdays:
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                is_open_late = True
                break
                
            # Split time range
            # Expected "Start–End" or "Start-End"
            # Note: The preview shows \u2013 (en-dash)
            parts = re.split(r"[\u2013-]", time_range)
            if len(parts) == 2:
                start_str, end_str = parts
                end_minutes = parse_time(end_str)
                start_minutes = parse_time(start_str)
                
                if end_minutes is not None:
                    # 6:00 PM is 18 * 60 = 1080 minutes
                    if end_minutes > 1080:
                        is_open_late = True
                        break
                    # Handle crossing midnight (e.g. 5PM - 2AM)
                    # If end_minutes < start_minutes (and not 24h), it assumes next day
                    # If end_minutes is AM (e.g. 1 AM = 60), it is < 1080.
                    # But it means it stays open past midnight, so definitely open after 6PM.
                    if end_minutes < start_minutes:
                         is_open_late = True
                         break
                         
    if is_open_late:
        valid_businesses.append(b)

print("__RESULT__:")
print(json.dumps(valid_businesses))"""

env_args = {'var_function-call-14090496036911441590': ['business_description'], 'var_function-call-17092706083038356233': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-6287908053654957115': [{'count': '79'}], 'var_function-call-15796407158225419449': 'file_storage/function-call-15796407158225419449.json'}

exec(code, env_args)
