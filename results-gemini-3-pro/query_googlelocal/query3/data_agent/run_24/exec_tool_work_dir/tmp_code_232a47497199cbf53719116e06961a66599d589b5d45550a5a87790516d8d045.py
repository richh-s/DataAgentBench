code = """import json
import re

# Load businesses
file_path = locals()['var_function-call-4692712977986487479']
with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def to_24h(time_str):
    # time_str examples: "6PM", "6:30AM", "12PM", "12:30AM", "3", "9.30"
    # The format in the sample is "6:30AM", "6PM", "9:30PM", "12PM"
    # "3" usually implies the same meridian as the other part if missing? 
    # Actually, in "3-8PM", 3 is 3PM. 
    # But let's assume standard format like "Number(:Number)?(AM|PM)".
    # Sometimes it might be just "3".
    
    time_str = time_str.strip()
    if time_str == "Open 24 hours":
        return 2400
    
    # regex for time
    match = re.match(r"(\d+)(?::(\d+))?\s*(AM|PM)?", time_str, re.IGNORECASE)
    if not match:
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    meridian = match.group(3)
    
    # If meridian is missing, it's tricky. But usually in "Start-End", the end has it.
    # The start might miss it. But we only care about End time to check if it's > 6PM.
    # End time usually has AM/PM.
    
    if meridian:
        meridian = meridian.upper()
        if meridian == "PM" and h != 12:
            h += 12
        elif meridian == "AM" and h == 12:
            h = 0
    
    return h * 100 + m

def is_open_late(hours_list):
    # hours_list is like [['Thursday', '6:30AM–6PM'], ...]
    # check if any weekday has end time > 1800 (6:00 PM)
    
    # We need to parse the JSON string of hours
    try:
        hours_data = json.loads(hours_list)
    except:
        return False
        
    for day, time_range in hours_data:
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Split by en-dash or hyphen
            # The sample uses \u2013 (en-dash)
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                start, end = parts
                end_val = to_24h(end)
                if end_val is not None:
                    # 6:00 PM is 1800. We want "after 6:00 PM"
                    # If it closes exactly at 6:00 PM (1800), does it "remain open after"?
                    # Usually "remains open after 6:00 PM" means strictly > 1800.
                    # Or it means it is open at 6:01 PM.
                    # "Open after 6:00 PM" -> Closing time > 18:00.
                    if end_val > 1800: # 18:00
                        return True
                    # If end_val < start_val (e.g. 11AM - 2AM), it means next day, so it is open late.
                    start_val = to_24h(start)
                    if start_val is not None and end_val < start_val:
                         # Crosses midnight
                         return True
            elif "24 hours" in time_range:
                return True
                
    return False

filtered_businesses = []
for b in businesses:
    if is_open_late(b['hours']):
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-5476439852656715722': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-7625765129633426110': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}], 'var_function-call-13316723503650301114': [{'count': '66'}], 'var_function-call-4692712977986487479': 'file_storage/function-call-4692712977986487479.json'}

exec(code, env_args)
