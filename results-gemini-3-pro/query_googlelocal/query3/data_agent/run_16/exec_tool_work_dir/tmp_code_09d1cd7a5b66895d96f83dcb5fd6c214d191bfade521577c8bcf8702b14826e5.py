code = """import json
import pandas as pd

# Load the business data from the file provided in the previous step
# The key is 'var_function-call-13370844062312160176'
with open(locals()['var_function-call-13370844062312160176'], 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # Parses time string like "6:30AM", "6PM", "9:30PM" to minutes from midnight
    # Returns None if invalid
    if not t_str: return None
    t_str = t_str.strip()
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    # Remove AM/PM
    t_clean = t_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t_clean:
        parts = t_clean.split(':')
        h = int(parts[0])
        m = int(parts[1])
    else:
        h = int(t_clean)
        m = 0
        
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    target_time_min = 18 * 60 # 6:00 PM in minutes
    
    for day_info in hours_list:
        if len(day_info) != 2: continue
        day, time_range = day_info
        
        if day not in weekdays:
            continue
            
        if time_range == 'Closed':
            continue
        if time_range == 'Open 24 hours':
            return True
            
        # Split time range "Start–End"
        # The separator seems to be \u2013 (en-dash)
        if '\u2013' in time_range:
            parts = time_range.split('\u2013')
        elif '-' in time_range: # fallback
            parts = time_range.split('-')
        else:
            continue
            
        if len(parts) != 2: continue
        
        end_time_str = parts[1]
        
        # Check if end time extends past 6 PM.
        # Cases: 
        # "5PM" -> 17:00 (No)
        # "6PM" -> 18:00 (No, must be *after*)
        # "6:30PM" -> 18:30 (Yes)
        # "9PM" -> 21:00 (Yes)
        # "12AM" -> 00:00 (Yes, next day)
        # "2AM" -> 02:00 (Yes, next day)
        
        try:
            end_min = parse_time(end_time_str)
            
            # If end time is small (e.g. 1 AM = 60 min), it's definitely after 6 PM (1080 min) because it wrapped around.
            # Assuming typical business hours where "opening" is in morning and "closing" is later.
            # But we just need to know if the closing time is > 18:00 OR if it's early morning (implying late night close).
            
            # A simple heuristic: 
            # If closing time >= 0 and < 6:00 AM (360 min), it's late night / next day. -> Yes
            # If closing time > 18:00 (1080 min). -> Yes
            
            if end_min is not None:
                if end_min > target_time_min: # Strictly after 6 PM
                    return True
                if end_min < 360: # Up to 6 AM next day
                    return True
        except:
            continue

    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

# Extract gmap_ids for next query
gmap_ids = [b['gmap_id'] for b in filtered_businesses]

print("__RESULT__:")
print(json.dumps({
    "filtered_gmap_ids": gmap_ids,
    "filtered_businesses": filtered_businesses
}))"""

env_args = {'var_function-call-9448307054440205137': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-11630857833362404501': [{'count': '79'}], 'var_function-call-13370844062312160176': 'file_storage/function-call-13370844062312160176.json'}

exec(code, env_args)
