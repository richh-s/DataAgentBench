code = """import json
import re

# Load businesses
with open(locals()['var_function-call-12351195923220380137'], 'r') as f:
    businesses = json.load(f)

def parse_time_to_minutes(time_str):
    # Returns (minutes, period)
    # minutes is 0-719 for AM, 720-1439 for PM
    # period is 'AM' or 'PM'
    if not time_str: return None
    time_str = time_str.strip()
    match = re.search(r"(\d+)(?::(\d+))?\s*(AM|PM)?", time_str, re.IGNORECASE)
    if not match: return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    period = match.group(3)
    
    if period:
        period = period.upper()
    
    # We will return h, m, period to handle logic outside
    return h, m, period

qualified_businesses = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        hours_list = json.loads(hours_str)
    except:
        continue
        
    is_open_late = False
    
    for day, time_range in hours_list:
        if day in weekdays:
            if "Open 24 hours" in time_range:
                is_open_late = True
                break
            if "Closed" in time_range:
                continue
            
            # Split range
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                start_str = parts[0].strip()
                end_str = parts[1].strip()
                
                # Parse end time
                parsed_end = parse_time_to_minutes(end_str)
                if not parsed_end: continue
                
                eh, em, e_period = parsed_end
                
                # Logic to determine if e_period is PM if missing
                # In "3-8PM", end is "8PM". e_period is PM.
                # In "11AM-2PM", end is "2PM".
                # In data, end usually has suffix.
                
                if not e_period:
                    # If missing, assume PM if start had AM? Unsafe.
                    # But scanning data, usually end has suffix.
                    # If strict, skip.
                    pass
                
                # Convert to minutes from midnight (0-1439)
                minutes = 0
                if e_period == 'PM':
                    if eh != 12:
                        minutes = (eh + 12) * 60 + em
                    else:
                        minutes = 12 * 60 + em # 12PM is 720
                elif e_period == 'AM':
                    if eh == 12:
                        minutes = 0 + em # 12AM is 0
                    else:
                        minutes = eh * 60 + em
                else:
                    # No period. Assume PM if h < 12 and h != 12?
                    # "5:30" usually PM if business hours.
                    # "17:00" is 24h.
                    pass
                
                # Logic for "Remain open after 6:00 PM"
                # 6 PM = 18:00 = 1080 mins.
                
                # Cases:
                # 1. PM, minutes > 1080. (e.g. 7 PM = 1140).
                # 2. AM (early morning next day). e.g. 1 AM = 60 mins.
                #    If period is AM and minutes < 720 (noon), it's likely next day closure.
                #    Exception: 9AM - 11AM.
                #    So we need to check if it's a "late night" AM.
                #    A business closing at 11 AM usually opened at 8 AM.
                #    A business closing at 1 AM usually opened in PM.
                #    So if end is AM, check start time.
                
                # Check start time to resolve ambiguity or confirm "crossing midnight"
                parsed_start = parse_time_to_minutes(start_str)
                if parsed_start:
                    sh, sm, s_period = parsed_start
                    # Infer start period if missing
                    # "9-5PM" -> Start 9AM?
                    # "3-8PM" -> Start 3PM?
                    
                    if not s_period and e_period:
                        # Heuristic: if start hour > end hour (numerically) and end is PM, start is likely AM.
                        # e.g. 9-5PM (9 > 5). Start 9 AM.
                        # 11-2PM (11 > 2). Start 11 AM.
                        # 3-8PM (3 < 8). Start 3 PM.
                        if sh > eh and e_period == 'PM':
                            s_period = 'AM'
                        elif sh < eh and e_period == 'PM':
                            s_period = 'PM' # 3-8PM
                        # This is rough but likely accurate for business hours.
                    
                    # Calculate start minutes
                    s_minutes = 0
                    if s_period == 'PM':
                         if sh != 12: s_minutes = (sh + 12) * 60 + sm
                         else: s_minutes = 12 * 60 + sm
                    elif s_period == 'AM':
                        if sh == 12: s_minutes = 0 + sm
                        else: s_minutes = sh * 60 + sm
                    else:
                        # default?
                        s_minutes = sh * 60 + sm
                        
                    # Logic:
                    # If end_minutes < start_minutes, it crosses midnight (e.g. 10PM to 2AM).
                    # If crosses midnight, it's open after 6PM.
                    if minutes < s_minutes:
                         is_open_late = True
                         break
                
                # Standard PM check
                if e_period == 'PM':
                    if minutes > 1080: # Strictly after 18:00
                        is_open_late = True
                        break
                elif e_period == 'AM':
                    # If end is AM, and we didn't catch "crosses midnight" (maybe start parsing failed),
                    # assume 12AM-4AM is late night. 5AM-11AM is morning shift.
                    if minutes < 600: # Closes before 10 AM -> Likely late night
                         is_open_late = True
                         break

    if is_open_late:
        qualified_businesses.append(b)

print("__RESULT__:")
print(json.dumps(qualified_businesses))"""

env_args = {'var_function-call-4613583688241027152': ['business_description'], 'var_function-call-10114926834381514642': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-13529672724907323289': [{'count': '79'}], 'var_function-call-12351195923220380137': 'file_storage/function-call-12351195923220380137.json', 'var_function-call-1070840189818604655': 'file_storage/function-call-1070840189818604655.json'}

exec(code, env_args)
