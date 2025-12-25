code = """import json
import ast

# Get the file path from the storage
file_path = locals()['var_function-call-4466573628404652358']

businesses = []
with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(time_str):
    if not time_str:
        return None
    time_str = time_str.strip()
    # Handle "12PM" -> 12.0, "12AM" -> 0.0
    # "6:30AM" -> 6.5
    
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    # Strip AM/PM
    t_clean = time_str.replace('PM', '').replace('AM', '').strip()
    
    try:
        if ':' in t_clean:
            parts = t_clean.split(':')
            hour = int(parts[0])
            minute = int(parts[1])
        else:
            hour = int(t_clean)
            minute = 0
            
        if is_pm and hour != 12:
            hour += 12
        if is_am and hour == 12:
            hour = 0
            
        return hour + minute / 60.0
    except:
        return None

filtered_businesses = []

for b in businesses:
    hours_data = b.get('hours')
    if not hours_data or hours_data == 'None':
        continue
    
    try:
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
                parts = hours_str.split('\u2013')
                if len(parts) == 2:
                    open_time_str = parts[0]
                    close_time_str = parts[1]
                    
                    open_time = parse_time(open_time_str)
                    close_time = parse_time(close_time_str)
                    
                    if open_time is not None and close_time is not None:
                        # Case 1: Crosses midnight (e.g. 5PM - 2AM)
                        if close_time < open_time:
                            is_open_after_6pm = True
                        # Case 2: Same day, closes after 18:00
                        elif close_time > 18.0:
                            is_open_after_6pm = True
            
            if is_open_after_6pm:
                break

    if is_open_after_6pm:
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-8219845975773706916': ['business_description'], 'var_function-call-6225709022825431152': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-8426357324127209070': [{'count': '79'}], 'var_function-call-4466573628404652358': 'file_storage/function-call-4466573628404652358.json'}

exec(code, env_args)
