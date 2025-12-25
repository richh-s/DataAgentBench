code = """import json
import re

# Load the businesses from the previous step
with open('var_function-call-11765510306618497496.json', 'r') as f:
    businesses = json.load(f)

def parse_time(time_str):
    # Parses time string like "6:30AM" or "6PM" or "12PM" (noon) or "12AM" (midnight)
    # Returns 24-hour float (e.g., 18.0, 18.5)
    # 12AM is 0.0 or 24.0 depending on context, usually 0.0 (start of day)
    # But for closing time, if it closes at 12AM, it's late.
    
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
        hours_list = json.loads(hours_json.replace("'", '"')) # Sometimes single quotes? The preview showed valid JSON double quotes.
    except:
        # Fallback if json load fails
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
            
            # Split time range. Usually "Start–End" (en-dash) or "Start-End" (hyphen)
            # The preview showed "\u2013" which is en-dash.
            times = re.split(r'\u2013|-', time_range)
            if len(times) == 2:
                end_time_str = times[1].strip()
                end_time = parse_time(end_time_str)
                
                # Check if > 18:00
                # Note: 12AM (midnight) should be considered late (effectively next day)
                # If closing time is 0.0 (12AM) or 1.0 (1AM), it is late.
                # However, usually we compare > 18.0.
                # If end_time is e.g. 19.0, it is > 18.0.
                # If end_time is 0.0 (midnight), technically 0 < 18, but it means late night.
                # Let's assume if it closes in the PM, it must be > 6PM.
                # If it closes in the AM (e.g. 1AM), it is definitely after 6PM (previous day).
                
                if end_time is not None:
                    # Logic: if end_time > 18.0 OR end_time < 4.0 (assuming very late night/early morning close means open past 6PM)
                    # Safe bet: if end_time > 18.0
                    if end_time > 18.0:
                        return True
                    # If closing time is 0 (midnight) or small AM hours, it's also "after 6 PM".
                    # Let's say anything between 0.0 and 6.0 is "late".
                    if 0.0 <= end_time < 9.0: # e.g. closes at 2AM.
                         # Wait, if it closes at 6AM? "6:30AM-6PM". 
                         # If it closes at 2AM, it opened earlier. 
                         # Usually standard business hours.
                         # Let's stick to: if closing time corresponds to a time after 18:00.
                         # 12 AM = 0.0. In 24h, 19, 20... 23, 24 (represented as 0 of next day).
                         # If it's AM and small (e.g. 1AM), it implies it stayed open past 6PM.
                         if end_time < 12.0: # AM hours
                             # But check start time? "6:30AM-6PM". 6PM is 18.0. Not after.
                             # If "5PM-2AM", close 2AM.
                             pass
                             
                    # Refined logic:
                    # Convert 12AM (midnight) to 24.0 for comparison if needed, or just handle cases.
                    # PM hours: must be > 6 (i.e. > 18.0) or 12 (noon) which is < 18.
                    # AM hours: usually means next day early morning -> definitely open after 6PM.
                    # EXCEPT if it's a morning shift e.g. 6AM-10AM. Then close is 10AM (not late).
                    # So, if PM and > 6PM.
                    # OR if AM (0.0 to say 5.0) -> likely late night close.
                    
                    is_pm = 'PM' in end_time_str.upper()
                    is_am = 'AM' in end_time_str.upper()
                    
                    if is_pm:
                         # 12 PM is noon (12.0). 1 PM is 13.0 ... 6 PM is 18.0.
                         # We need > 18.0
                         if end_time > 18.001: # allow slight float diff, strictly after 6PM
                             return True
                    elif is_am:
                         # 12 AM is midnight. 1 AM ...
                         # If closing is 12AM, 1AM, 2AM... it's late.
                         # If closing is 10AM, 11AM... it's early.
                         # Let's say if closing is <= 4AM it is late.
                         if end_time == 0.0 or end_time <= 4.0:
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
