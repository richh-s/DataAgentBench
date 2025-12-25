code = """import json
import re

# Load business data
file_path = locals()['var_function-call-1853476984234461660']
with open(file_path, 'r') as f:
    businesses = json.load(f)

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # hours_str is a string representation of a list of lists, usually valid JSON if we fix quotes
        # But looking at the output: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # It seems to be a JSON string.
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                return True
            
            # Parse time range like "6:30AM–6PM" or "11AM–9:30PM"
            # Split by dash. Note the dash might be unicode \u2013
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                end_time_str = parts[1].strip()
                
                # Check for AM/PM
                if 'PM' in end_time_str:
                    time_val = end_time_str.replace('PM', '').strip()
                    if ':' in time_val:
                        h, m = map(int, time_val.split(':'))
                    else:
                        h = int(time_val)
                        m = 0
                    
                    # 12 PM is noon, 1 PM is 13:00.
                    # Logic: 
                    # If it is 12 PM, that is 12:00. Not after 6 PM.
                    # If it is 1 PM to 11 PM, we convert to 24h?
                    # Actually, simple logic:
                    # If it's PM:
                    # 12 PM = 12:00 (No)
                    # 1 PM - 5 PM (No)
                    # 6 PM (No, needs to be *after* 6 PM? "remains open after 6:00 PM")
                    # Prompt says "remains open after 6:00 PM".
                    # Does 6:00 PM count? "After 6:00 PM" usually means closing time > 18:00. 
                    # Or does it mean it is open at 6:01 PM? 
                    # Usually "open after 6 PM" means the business is operational during the evening.
                    # If it closes at 6 PM, it is not open *after* 6 PM.
                    # If it closes at 6:30 PM, it is open after 6 PM.
                    
                    # Let's assume strict inequality: Closing Time > 6:00 PM.
                    
                    # 12 PM is noon (12). 
                    # 1..11 PM.
                    if h == 12:
                        pass # Noon.
                    else:
                        # h is 1..11
                        # If h >= 6 (i.e., 6, 7, 8, 9, 10, 11)
                        # But wait, if h=6 and m=0, that is 6:00 PM. Is it open *after* 6 PM? 
                        # If it closes at 6:00 PM, it's not open after 6 PM.
                        # If it closes at 6:30 PM, yes.
                        # So: if h > 6 or (h == 6 and m > 0): return True
                        if h > 6 or (h == 6 and m > 0):
                            return True
                            
                elif 'AM' in end_time_str:
                    # Could be "12AM" (midnight) or "1AM" (late night).
                    # 12 AM is midnight. 1 AM is 1 hour after midnight.
                    # These are definitely after 6 PM.
                    # What about "11AM"? No.
                    # We need to distinguish "early morning end" vs "late night end".
                    # Usually "9AM-5PM". End is 5PM.
                    # "5PM-2AM". End is 2AM.
                    # If the shift wraps around, it's open after 6 PM.
                    # Typically, if end time is AM and start time is AM/PM, and it's a business,
                    # small AM numbers (12, 1, 2, 3, 4) imply late night.
                    # 10 AM, 11 AM imply morning closing.
                    
                    time_val = end_time_str.replace('AM', '').strip()
                    if ':' in time_val:
                        h, m = map(int, time_val.split(':'))
                    else:
                        h = int(time_val)
                        m = 0
                    
                    if h == 12 or h <= 4: # Assuming late night / early morning closing
                         return True
                         
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b.get('hours')):
        filtered_businesses.append({
            'gmap_id': b['gmap_id'],
            'name': b['name'],
            'hours': b['hours']
        })

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-393867038646183298': ['business_description'], 'var_function-call-13412543316668570683': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-11148055321928147633': [{'count': '79'}], 'var_function-call-1853476984234461660': 'file_storage/function-call-1853476984234461660.json'}

exec(code, env_args)
