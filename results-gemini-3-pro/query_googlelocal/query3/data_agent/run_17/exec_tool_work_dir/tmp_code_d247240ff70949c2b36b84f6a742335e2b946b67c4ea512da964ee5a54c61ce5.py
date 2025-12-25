code = """import json
import ast
from datetime import datetime

# Load businesses
with open('var_function-call-3043783580466555497.json', 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False, None
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False, None
        
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True, hours_str
            if time_range == 'Closed':
                continue
            
            # Parse time range, e.g., "6:30AM–6PM" or "11AM–9:30PM"
            # Split by '–' (en dash) or '-' (hyphen)
            if '–' in time_range:
                parts = time_range.split('–')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) == 2:
                end_time_str = parts[1].strip()
                # Parse end time
                # Formats: "6PM", "6:30PM", "12AM", etc.
                try:
                    # Normalize time string for parsing
                    # Python datetime strptime %I%p or %I:%M%p
                    dt = None
                    if ':' in end_time_str:
                         dt = datetime.strptime(end_time_str, "%I:%M%p")
                    else:
                         dt = datetime.strptime(end_time_str, "%I%p")
                    
                    # Check if > 6:00 PM (18:00)
                    # 12 PM is noon (12:00), 12 AM is midnight (00:00)
                    
                    # Convert to 24hr integer for comparison
                    hour = dt.hour
                    minute = dt.minute
                    
                    # 6 PM is 18
                    # If hour > 18, yes.
                    # If hour == 18 and minute > 0, yes.
                    # Special case: closing at 12AM or later (e.g. 1AM, 2AM) which is next day morning.
                    # But usually represented as AM.
                    # If it closes at 12AM, 1AM, etc., it is definitely open after 6PM.
                    # In 24h: 0, 1, 2...
                    # If closing time is AM (and not 12PM), it implies it's open late night (or early morning next day).
                    # Wait, if it closes at 10AM, it's not open after 6PM.
                    # So we need to distinguish "closes at 1AM (next day)" vs "closes at 10AM (same day)".
                    # Assuming standard business hours, if it closes in AM (0-11), 
                    # usually businesses open in AM and close in PM.
                    # If it closes in AM (e.g. 2AM), it likely opened previous day.
                    # However, simple logic: is the closing time > 6PM?
                    # 6:01 PM to 11:59 PM range.
                    
                    if 18 < hour < 24:
                        return True, hours_str
                    if hour == 18 and minute > 0:
                        return True, hours_str
                    
                    # Handle "late night" closings?
                    # If a place closes at 1 AM, it is open after 6 PM.
                    # But if a breakfast place closes at 11 AM, it is not.
                    # Context: "Start–End".
                    # Let's parse Start time too to be sure? 
                    # Usually "open after 6PM" means it is open at some point after 6PM.
                    # If it closes at 1AM, it was open at 6PM (presumably).
                    # If it closes at 5PM, it's not open after 6PM.
                    
                    # Let's look at AM/PM.
                    # If end_time is PM: needs to be > 6PM.
                    # If end_time is AM:
                    #   If it's 12AM (midnight), yes.
                    #   If it's small AM (1, 2, 3), yes (open late).
                    #   If it's late morning (10, 11), probably no (breakfast place).
                    #   Let's check start time.
                    
                    start_time_str = parts[0].strip()
                    start_dt = None
                    if ':' in start_time_str:
                         start_dt = datetime.strptime(start_time_str, "%I:%M%p")
                    else:
                         start_dt = datetime.strptime(start_time_str, "%I%p")
                    
                    # If start is PM (e.g. 5PM) and end is AM (e.g. 2AM), yes.
                    # If start is AM (e.g. 8AM) and end is AM (e.g. 2AM), yes.
                    # If start is AM (e.g. 6AM) and end is AM (e.g. 11AM), no.
                    
                    start_h = start_dt.hour
                    end_h = dt.hour
                    
                    # Logic: 
                    # If end_h is 0-5 (12AM-5AM), it's late. YES.
                    # If end_h >= 18 (6PM+), YES (unless exactly 18:00, then NO per "after 6:00 PM").
                    # User says "remain open after 6:00 PM". 
                    # If it closes AT 6:00 PM, does it remain open AFTER? Strictly, no. It closes at 6:00.
                    # So strict inequality > 18:00.
                    
                    if 0 <= end_h <= 5: # Closes after midnight
                        return True, hours_str
                    
                    if end_h > 18:
                        return True, hours_str
                    if end_h == 18 and minute > 0:
                        return True, hours_str
                    
                except ValueError:
                    pass

    return False, None

filtered_businesses = []
for b in businesses:
    is_open, hours_val = is_open_after_6pm(b['hours'])
    if is_open:
        b['hours'] = hours_val # keep the string
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-4784077454714328516': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-12420282615059275630': [{'count': '79'}], 'var_function-call-3043783580466555497': 'file_storage/function-call-3043783580466555497.json'}

exec(code, env_args)
