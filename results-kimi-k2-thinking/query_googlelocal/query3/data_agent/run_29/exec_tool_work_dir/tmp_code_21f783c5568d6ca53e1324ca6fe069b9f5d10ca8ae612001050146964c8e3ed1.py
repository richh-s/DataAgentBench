code = """import json
import re
import ast

# Get business data from storage
biz_result = locals()['var_functions.query_db:20']

# Load JSON data from file if it's a file path
if isinstance(biz_result, str) and biz_result.endswith('.json'):
    with open(biz_result, 'r') as f:
        businesses = json.load(f)
else:
    businesses = biz_result

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_closing_hour(time_str):
    """Parse closing hour from time string"""
    if not time_str or '-' not in time_str or time_str == 'Closed':
        return None
    
    # Extract the closing part (after '-')
    closing = time_str.split('-')[1].strip().upper()
    
    # Handle various formats
    if '12PM' in closing or '12:00PM' in closing:
        return 12
    if '12AM' in closing or '12:00AM' in closing:
        return 24  # Midnight is 24:00 or 0:00, but we'll treat as next day
    
    # Match patterns like 9PM, 9:30PM, 10PM, etc.
    match = re.search(r'(\d{1,2})(?::\d{2})?(AM|PM)', closing)
    if not match:
        return None
    
    hour = int(match.group(1))
    period = match.group(2)
    
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    
    return hour

def is_open_after_6pm(hours_data):
    """Check if business is open after 6pm on any weekday"""
    if not hours_data or hours_data == 'None':
        return False
    
    try:
        # Parse the hours string safely
        if isinstance(hours_data, str):
            # Handle unicode dash character
            hours_str = hours_data.replace('\u2013', '-')
            hours_list = ast.literal_eval(hours_str)
        else:
            hours_list = hours_data
    except Exception as e:
        return False
    
    if not isinstance(hours_list, list):
        return False
    
    for day_entry in hours_list:
        if len(day_entry) < 2:
            continue
        
        day = day_entry[0]
        time_range = day_entry[1]
        
        if day in weekdays and time_range != 'Closed':
            closing_hour = parse_closing_hour(time_range)
            if closing_hour and closing_hour > 18:  # After 6pm = hour 18
                return True
    
    return False

# Filter businesses open after 6pm on weekdays
late_businesses = []
for biz in businesses:
    if is_open_after_6pm(biz.get('hours')):
        late_businesses.append({
            'gmap_id': biz['gmap_id'],
            'name': biz['name'],
            'hours': biz['hours']
        })

print(f"Found {len(late_businesses)} businesses open after 6pm\n")
print('Sample businesses:')
for b in late_businesses[:5]:
    print(f"  {b['name']}: {b['hours']}")

print('__RESULT__:')
print(json.dumps({
    'count': len(late_businesses),
    'businesses': late_businesses
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.execute_python:16': {'count': 0, 'businesses': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
