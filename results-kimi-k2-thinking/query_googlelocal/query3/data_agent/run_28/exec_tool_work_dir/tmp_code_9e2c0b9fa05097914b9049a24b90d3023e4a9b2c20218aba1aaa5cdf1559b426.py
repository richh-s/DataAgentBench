code = """import json
import re
from datetime import time

# Function to parse closing time from hours string
def parse_closing_time(time_str):
    try:
        if not time_str or time_str in ['Closed', 'Open 24 hours']:
            return None
        
        # Clean unicode dash
        time_str = time_str.replace('\u2013', '-')
        
        if '-' in time_str:
            parts = time_str.split('-')
            if len(parts) == 2:
                closing_part = parts[1].strip()
                
                # Parse formats like "6PM", "9:30PM", "12AM", "12:30PM"
                closing_part_lower = closing_part.lower()
                
                if ':' in closing_part:
                    match = re.match(r'(\d+):(\d+)(am|pm)', closing_part_lower)
                    if match:
                        hour = int(match.group(1))
                        minute = int(match.group(2))
                        period = match.group(3)
                        
                        if period == 'pm' and hour != 12:
                            hour += 12
                        elif period == 'am' and hour == 12:
                            hour = 0
                            
                        return time(hour, minute)
                else:
                    match = re.match(r'(\d+)(am|pm)', closing_part_lower)
                    if match:
                        hour = int(match.group(1))
                        period = match.group(2)
                        
                        if period == 'pm' and hour != 12:
                            hour += 12
                        elif period == 'am' and hour == 12:
                            hour = 0
                            
                        return time(hour, 0)
    except Exception as e:
        print(f'Error parsing time: {time_str}, error: {e}')
    return None

# Function to check if business is open after 6pm on any weekday
def is_open_after_six(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # The data is stored as a string representation of a list
        # We'll use ast.literal_eval to safely parse it
        import ast
        hours_list = ast.literal_eval(hours_str)
        
        if not isinstance(hours_list, list):
            return False
        
        weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
        
        for day_entry in hours_list:
            if not isinstance(day_entry, list) or len(day_entry) != 2:
                continue
                
            day, hours = day_entry
            if day in weekdays:
                if hours == 'Open 24 hours':
                    return True
                if hours == 'Closed':
                    continue
                
                closing_time = parse_closing_time(hours)
                if closing_time and closing_time > time(18, 0):
                    return True
        
        return False
    except Exception as e:
        print(f'Error processing hours string: {hours_str}, error: {e}')
        return False

# Load business data
business_file = locals()['var_functions.query_db:20']
with open(business_file, 'r') as f:
    businesses = json.load(f)

print(f'Loaded {len(businesses)} businesses')

# Filter businesses that are open after 6pm on weekdays
businesses_open_after_six = []
for business in businesses:
    hours = business.get('hours')
    if hours and is_open_after_six(hours):
        businesses_open_after_six.append(business)

print(f'{len(businesses_open_after_six)} businesses are open after 6pm on weekdays')

# Get business IDs for these businesses
business_ids = set([b['gmap_id'] for b in businesses_open_after_six])

print('__RESULT__:')
print(json.dumps({
    'message': 'Businesses filtered',
    'count': len(businesses_open_after_six),
    'business_ids_count': len(business_ids)
}, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'Data loaded successfully', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'Data loaded', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
