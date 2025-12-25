code = """import json
import re

# Load the business data
with open(locals()['var_function-call-2744922478340649244'], 'r') as f:
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
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                return True
            
            # Parse time range, e.g., "6:30AM–6PM", "11AM–9:30PM", "3–8PM"
            # Split by en-dash or hyphen
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                close_time_str = parts[1].strip() # e.g., "6PM", "9:30PM", "12AM" (next day)
                
                # Convert close_time_str to 24-hour format minutes
                # Helper to parse time string
                def parse_time(t_str):
                    t_str = t_str.upper()
                    is_pm = 'PM' in t_str
                    is_am = 'AM' in t_str
                    # Remove AM/PM
                    clean_t = t_str.replace('PM', '').replace('AM', '').strip()
                    
                    if ':' in clean_t:
                        h, m = map(int, clean_t.split(':'))
                    else:
                        h = int(clean_t)
                        m = 0
                        
                    if is_pm and h != 12:
                        h += 12
                    if is_am and h == 12:
                        h = 0
                    # Handle "12AM" usually implies next day, effectively very late. 
                    # But if it closes at 12AM, it is open after 6 PM.
                    if t_str == '12AM': # Special case for midnight closing
                         return 24 * 60
                    
                    return h * 60 + m

                try:
                    close_mins = parse_time(close_time_str)
                    target_mins = 18 * 60 # 6:00 PM
                    
                    # If closing time is 0 (midnight next day) or small (early morning next day), 
                    # it means it's open past midnight, so definitely open after 6 PM.
                    # e.g., closes at 2 AM.
                    # Logic check:
                    # If close_time is 18:00 (1080), it's not *after* 6 PM.
                    # If close_time is > 1080, it is.
                    # If close_time is < opening time (overnight), it is.
                    # But simpler check: if it closes at PM >= 6 or AM (next day), it's good.
                    
                    # Let's rely on standard PM conversion.
                    # 6PM -> 18:00 (1080)
                    # 5PM -> 17:00 (1020)
                    # 6:30PM -> 18:30 (1110)
                    # 12AM -> 0:00 (or 24:00)
                    # 2AM -> 2:00
                    
                    # If 'PM' is in string:
                    if 'PM' in close_time_str:
                         if close_mins > target_mins:
                             return True
                    elif 'AM' in close_time_str:
                        # If it closes in AM, it likely spills over to next day, 
                        # meaning it was open through the evening.
                        return True
                        
                except Exception as e:
                    # print(f"Error parsing time {close_time_str}: {e}")
                    pass
                    
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-4816253827118263871': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-11659200861465779444': [{'count': '66'}], 'var_function-call-15186731001370988029': [{'count': '79'}], 'var_function-call-2744922478340649244': 'file_storage/function-call-2744922478340649244.json'}

exec(code, env_args)
