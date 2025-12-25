code = """import json
import re

# Load businesses
with open(locals()['var_function-call-3011920856549817441'], 'r') as f:
    businesses = json.load(f)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = json.loads(hours_str)
    except:
        return False

    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Split time range. En-dash or hyphen
            # Replace en-dash with hyphen just in case
            time_range = time_range.replace('–', '-')
            if '-' not in time_range:
                continue
            
            parts = time_range.split('-')
            if len(parts) != 2:
                continue
            
            close_time_str = parts[1].strip() # e.g., "6PM", "9:30PM", "2AM"
            
            # Parse close_time_str
            # Simple parser
            # Check for AM/PM
            is_pm = 'PM' in close_time_str
            is_am = 'AM' in close_time_str
            
            time_str = close_time_str.replace('PM', '').replace('AM', '').strip()
            if ':' in time_str:
                h, m = map(int, time_str.split(':'))
            else:
                h = int(time_str)
                m = 0
            
            # Convert to 24-hour equivalent for comparison
            # 12AM is 0 (or 24), 1AM is 1, ..., 12PM is 12, 1PM is 13...
            # But for "closing after 6PM", we treat late night (e.g. 1AM) as open after 6PM
            
            # Let's standardise to 24h format 0-23
            if is_pm and h != 12:
                h += 12
            if is_am and h == 12:
                h = 0
            
            # If h is 0, 1, 2... (early morning), it means it closed next day, so it was open after 6PM.
            # If h > 18 (6PM), it is open after 6PM.
            # If h == 18 and m > 0, it is open after 6PM.
            
            # Handling the case where close time is early morning (e.g. 2AM)
            # This implies it spans across midnight.
            # Logic: If close time is AM (and not 12PM which is noon), it's likely next day.
            # Only exception: 12AM is midnight.
            
            if is_am:
                # e.g., 1AM. Definitely open after 6PM previous day.
                # However, need to be careful with things closing at, say, 11AM.
                # But usually hours are like "9AM-5PM".
                # If "5PM-2AM", then close is 2AM.
                # If "9AM-11AM", close is 11AM. Not after 6PM.
                
                # Heuristic: if open time is PM and close is AM, or if close is very early AM (0-5), it's late night.
                # But I only have close time here.
                # Let's look at the hour.
                # If closing at 12AM, 1AM, 2AM, 3AM, 4AM, 5AM... -> assume late night -> Open after 6PM.
                # If closing at 6AM, 7AM... 11AM -> Morning shift -> Not after 6PM (unless open 24h, handled).
                if h < 12: # 0 to 11
                    if h <= 5: # 12AM to 5AM
                         return True
                    else:
                         pass # 6AM to 11AM, not after 6PM
            
            if is_pm:
                # PM times. 12PM (Noon) to 11PM.
                # We want > 18:00.
                if h > 18:
                    return True
                if h == 18 and m > 0:
                    return True

    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-2487918565202048850': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-13806744480525354643': [{'count': '79'}], 'var_function-call-3011920856549817441': 'file_storage/function-call-3011920856549817441.json'}

exec(code, env_args)
