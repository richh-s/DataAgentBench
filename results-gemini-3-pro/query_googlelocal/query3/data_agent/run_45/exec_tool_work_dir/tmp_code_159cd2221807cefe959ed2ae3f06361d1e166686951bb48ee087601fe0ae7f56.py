code = """import json
import ast

def parse_time(t_str):
    # Returns 24h hour as float, e.g. 18.5 for 6:30PM
    t_str = t_str.strip()
    if t_str == 'Open 24 hours':
        return 24.0
    
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
        
    if is_pm:
        if h != 12:
            h += 12
    elif is_am:
        if h == 12:
            h = 0 # 12AM is 00:00
            
    # If no AM/PM, it's ambiguous, but usually not the case in this dataset's end times.
    # However, sometimes ranges like "3-8PM" -> 3 is 3PM. But we only care about end time.
    # In "3-8PM", end time "8PM" has PM.
    
    return h + m/60.0

def is_late_open(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        hours_list = json.loads(hours_str)
    except:
        # Fallback if json.loads fails (e.g., single quotes)
        try:
            hours_list = ast.literal_eval(hours_str)
        except:
            return False
            
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_item in hours_list:
        if len(day_item) != 2:
            continue
        day, time_range = day_item
        
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            if time_range == 'Closed':
                continue
                
            # Split by en-dash or hyphen
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) < 2:
                continue
                
            end_time_str = parts[1]
            try:
                # Check for special cases
                # If end time is AM and small hour (e.g. 1AM), it is effectively next day 25h, so > 18h.
                # If end time is PM and > 6PM (18h).
                # If end time is 12AM (Midnight), it is > 18h.
                
                # Let's use the parse logic
                # We need to handle the case where AM/PM is missing but implied?
                # Usually end time has it.
                
                # Check directly
                is_pm = 'PM' in end_time_str
                is_am = 'AM' in end_time_str
                
                if not is_pm and not is_am:
                    # Maybe it's like 18:00? Unlikely in this dataset.
                    continue
                
                # Parse
                t_val = parse_time(end_time_str)
                
                # Logic for "after 6:00 PM"
                # If it's PM: must be > 18.0
                if is_pm:
                    if t_val > 18.0:
                        return True
                # If it's AM:
                # 12AM = 0.0 (midnight). This is > 6PM (previous day).
                # 1AM, 2AM... = early morning next day. This is > 6PM.
                # 6AM...11AM = morning. This is NOT open AFTER 6PM (it closes before evening).
                # So if AM:
                if is_am:
                    if t_val < 12.0: # 0.0 (12AM) to 11.59 (11:59AM)
                        # If t_val is 0.0 (12AM) -> Good.
                        # If t_val is 1.0 (1AM) -> Good.
                        # If t_val is 6.0 (6AM) -> Bad?
                        # Assume businesses don't stay open past 6AM from previous day unless 24h.
                        # If a bar closes at 2AM, it matches.
                        # If a breakfast place closes at 11AM, it doesn't.
                        # Cutoff: Let's say if closes before 6AM, it's a late night spot.
                        if t_val < 6.0: 
                             return True
                        # 12AM case: t_val = 0.0. < 6.0. True.
                        
            except Exception as e:
                continue
                
    return False

# Load data
with open('var_function-call-9505002775633145034.json', 'r') as f:
    businesses = json.load(f)

filtered_businesses = []
for b in businesses:
    if is_late_open(b['hours']):
        filtered_businesses.append(b)

filtered_gmap_ids = [b['gmap_id'] for b in filtered_businesses]
print("__RESULT__:")
print(json.dumps(filtered_gmap_ids))"""

env_args = {'var_function-call-16930252738869414104': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-13480375080291303633': [{'count': '79'}], 'var_function-call-9505002775633145034': 'file_storage/function-call-9505002775633145034.json'}

exec(code, env_args)
