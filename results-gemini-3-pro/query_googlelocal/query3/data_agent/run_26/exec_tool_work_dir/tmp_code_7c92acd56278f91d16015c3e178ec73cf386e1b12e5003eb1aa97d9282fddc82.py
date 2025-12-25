code = """import json
import ast

businesses = []
# Load the previous result from file
with open('var_function-call-4466573628404652358.json', 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(time_str):
    # time_str example: "6:30AM", "6PM", "12PM" (noon), "12AM" (midnight)
    # Returns 24-hour float e.g. 18.0, 6.5
    
    if not time_str:
        return None
    
    time_str = time_str.strip()
    is_pm = time_str.endswith('PM')
    is_am = time_str.endswith('AM')
    
    if not is_pm and not is_am:
        return None # unexpected format

    t = time_str[:-2]
    parts = t.split(':')
    hour = int(parts[0])
    minute = int(parts[1]) if len(parts) > 1 else 0
    
    if is_pm and hour != 12:
        hour += 12
    if is_am and hour == 12:
        hour = 0
        
    return hour + minute / 60.0

filtered_businesses = []

for b in businesses:
    hours_data = b.get('hours')
    if not hours_data or hours_data == 'None':
        continue
    
    try:
        # Use ast.literal_eval because the format looks like python list string
        hours_list = ast.literal_eval(hours_data)
    except:
        continue

    is_open_after_6pm = False
    
    for day_info in hours_list:
        if len(day_info) != 2:
            continue
            
        day_name = day_info[0]
        hours_str = day_info[1]
        
        if day_name in weekdays:
            if hours_str == 'Open 24 hours':
                is_open_after_6pm = True
                break
            elif hours_str == 'Closed':
                continue
            elif '\u2013' in hours_str: # En dash
                # Split by en dash
                parts = hours_str.split('\u2013')
                if len(parts) == 2:
                    close_time_str = parts[1]
                    # Handle cases like "Open 24 hours" if mixed or weird (unlikely based on data)
                    # Parse closing time
                    close_time = parse_time(close_time_str)
                    if close_time is not None:
                        # Check if closes after 18:00 (6 PM)
                        # We consider "after 6 PM" meaning it is still open at 6:01 PM.
                        # If it closes at 6 PM, it is not open *after* 6 PM in the sense of extended hours?
                        # "remain open after 6:00 PM" usually means closing time > 6:00 PM.
                        # However, if a business closes at 12AM (midnight) or 1AM (next day), parse_time returns 0 or 1.
                        # We need to handle late night closings.
                        # If close_time < open_time, it usually means next day.
                        # But simple check: usually "9AM-5PM".
                        # If closing is "12AM" (0.0), it is effectively 24.0 for this comparison.
                        # If closing is "1AM", it is 25.0.
                        # Let's handle the AM/PM logic carefully.
                        
                        # If closing time is AM (0-11.99) and it's not "12PM" (noon), it's likely next day if opening was AM/PM.
                        # But simpler heuristic:
                        # If close_time_str ends with AM and it is not 12AM (which is 0), it is likely next day early morning.
                        # 12AM is midnight, which is > 6 PM.
                        # 1 AM is > 6 PM.
                        # So if the parsed time is < 12 (noon) and represented as AM, add 24 to it for comparison?
                        # Actually, 6 PM is 18.0.
                        # Any time > 18.0 is good.
                        # Any time in AM (early morning next day) is also good.
                        
                        # Let's refine:
                        # If closing time > 18.0, good.
                        # If closing time < 12.0 (e.g. 1 AM, 2 AM, ... 11 AM), we need to check if it's "next day".
                        # Typically businesses don't open at 5 PM and close at 11 AM same day backwards.
                        # Most businesses opening in morning close in evening.
                        # If they close at 1 AM, it's next day.
                        # So if closing time is between 0 and say 10 (AM), and it's a PM opening or standard day, it's late.
                        
                        # Let's look at the string "AM" or "PM".
                        if close_time_str.endswith('AM'):
                             # 12AM is 0.0. 1AM is 1.0.
                             # If it closes at 10AM, it might be a morning coffee shop? No, context is "remain open after 6PM".
                             # If a place is 7AM - 10AM, it's not open after 6PM.
                             # If a place is 5PM - 2AM, it is.
                             
                             # We should look at opening time too?
                             open_time_str = parts[0]
                             open_time = parse_time(open_time_str)
                             
                             # If close_time < open_time, it crosses midnight.
                             # e.g. 5PM (17) to 2AM (2). 2 < 17. So crosses midnight.
                             # If crosses midnight, it is open at 6 PM (18) provided open_time <= 18?
                             # Or if open_time > 18, it's open after 6 PM (e.g. opens 8 PM).
                             
                             if close_time < open_time:
                                 # Crosses midnight, so likely open late.
                                 # Need to check if it covers the post-6PM period.
                                 # If it crosses midnight, it stays open until next morning.
                                 # e.g. 10PM - 2AM. Open after 6PM? Yes, 10PM is after 6PM.
                                 # e.g. 5PM - 2AM. Open after 6PM? Yes.
                                 is_open_after_6pm = True
                             else:
                                 # Same day.
                                 # e.g. 9AM - 10AM. Not open after 6PM.
                                 # e.g. 9AM - 8PM. Open after 6PM.
                                 if close_time > 18.0:
                                     is_open_after_6pm = True
                        else:
                            # PM case.
                            # e.g. 6PM is 18.0.
                            if close_time > 18.0:
                                is_open_after_6pm = True
                                
            if is_open_after_6pm:
                break

    if is_open_after_6pm:
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-8219845975773706916': ['business_description'], 'var_function-call-6225709022825431152': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-8426357324127209070': [{'count': '79'}], 'var_function-call-4466573628404652358': 'file_storage/function-call-4466573628404652358.json'}

exec(code, env_args)
