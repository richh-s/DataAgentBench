code = """import json
import ast
from datetime import datetime

# Get the file path from the variable
file_path = locals()['var_function-call-4041812981108132417']

with open(file_path, 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # formats: "6:30AM", "6PM", "12PM", "12AM", "9:30PM"
    return datetime.strptime(t_str, "%I:%M%p" if ":" in t_str else "%I%p")

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Closed':
                continue
            if time_range == 'Open 24 hours':
                return True
            
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) == 2:
                end_time_str = parts[1].strip()
                try:
                    end_dt = parse_time(end_time_str)
                    target = datetime.strptime("6:00PM", "%I:%M%p").time()
                    check = end_dt.time()
                    
                    is_am = end_time_str.endswith('AM')
                    is_pm = end_time_str.endswith('PM')
                    
                    if is_pm:
                         if check > target:
                             return True
                    elif is_am:
                        # 12AM is 00:00. 1AM is 01:00.
                        # Anything AM (00:00-11:59) that is a closing time usually implies next day if it's "night".
                        # If closing at 11AM, it's not "open after 6PM" (it closed way before).
                        # If closing at 12AM, 1AM, 2AM... it's after 6PM.
                        # Let's assume late night closing is < 9AM.
                        if check.hour < 9: 
                            return True
                        
                except Exception as e:
                    pass
    return False

valid_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        valid_businesses.append(b)

print("__RESULT__:")
print(json.dumps(valid_businesses))"""

env_args = {'var_function-call-11274278717337983726': ['business_description'], 'var_function-call-5679228863261529158': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-10625289044817991517': [{'count': '79'}], 'var_function-call-4041812981108132417': 'file_storage/function-call-4041812981108132417.json'}

exec(code, env_args)
