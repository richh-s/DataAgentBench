code = """import re
import json

# Load the full business data from file
business_data_path = locals()['var_functions.query_db:8']
if isinstance(business_data_path, str) and business_data_path.endswith('.json'):
    with open(business_data_path, 'r') as f:
        businesses = json.load(f)
else:
    businesses = business_data_path

# Parse business hours to find those open after 6pm on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_closing_time(time_str):
    """Extract closing hour from time string like '10AM-8PM' or '9AM-10PM'"""
    if '-' not in time_str:
        return None
    
    closing_part = time_str.split('-')[1].strip()
    
    # Handle 12PM/12AM cases
    if '12PM' in closing_part:
        return 12
    elif '12AM' in closing_part or '12:00AM' in closing_part:
        return 0
    
    # Extract hour and AM/PM
    match = re.search(r'(\d+)(?::\d+)?(AM|PM)', closing_part, re.IGNORECASE)
    if not match:
        return None
    
    hour = int(match.group(1))
    period = match.group(2).upper()
    
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    
    return hour

def is_open_after_6pm(hours_data):
    """Check if business is open after 6pm on any weekday"""
    if hours_data == 'None' or not hours_data:
        return False
    
    try:
        if isinstance(hours_data, str):
            hours_list = json.loads(hours_data.replace('"', '\\"'))
        else:
            hours_list = hours_data
    except:
        return False
    
    for day_hours in hours_list:
        if len(day_hours) < 2:
            continue
            
        day = day_hours[0]
        time_range = day_hours[1]
        
        if day in weekdays and time_range != 'Closed':
            closing_hour = parse_closing_time(time_range)
            if closing_hour and closing_hour > 18:  # After 6pm (18:00)
                return True
    
    return False

# Filter businesses open after 6pm
open_after_6pm = []
for business in businesses:
    if is_open_after_6pm(business['hours']):
        open_after_6pm.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print(f"Found {len(open_after_6pm)} businesses open after 6pm on weekdays")
print('__RESULT__:')
print(open_after_6pm[:3])  # Return first 3 as preview"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}]}

exec(code, env_args)
