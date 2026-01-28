code = """import json
import re

# Get business data from storage
biz_result = locals()['var_functions.query_db:8']

# Load JSON data from file if it's a file path
if isinstance(biz_result, str) and biz_result.endswith('.json'):
    with open(biz_result, 'r') as f:
        businesses = json.load(f)
else:
    businesses = biz_result

print('Processing businesses count:', len(businesses))

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def get_closing_hour(time_str):
    if not time_str or '-' not in time_str:
        return None
    
    parts = time_str.split('-')
    if len(parts) < 2:
        return None
    
    closing = parts[1].strip().upper()
    
    if '12PM' in closing:
        return 12
    if '12AM' in closing:
        return 0
    
    match = re.search(r'(\d+)(?::\d+)?(AM|PM)', closing)
    if not match:
        return None
    
    hour = int(match.group(1))
    period = match.group(2)
    
    if period == 'PM' and hour != 12:
        hour = hour + 12
    
    return hour

def check_open_late(hours_data):
    if hours_data == 'None' or not hours_data:
        return False
    
    try:
        if isinstance(hours_data, str):
            hours_list = eval(hours_data)
        else:
            hours_list = hours_data
    except:
        return False
    
    if not isinstance(hours_list, list):
        return False
    
    for entry in hours_list:
        if len(entry) < 2:
            continue
        
        day = entry[0]
        hours_range = entry[1]
        
        if day in weekdays and hours_range != 'Closed':
            close_hour = get_closing_hour(hours_range)
            if close_hour and close_hour > 18:
                return True
    
    return False

late_businesses = []
for biz in businesses:
    if check_open_late(biz.get('hours', 'None')):
        late_businesses.append({
            'gmap_id': biz['gmap_id'],
            'name': biz['name'],
            'hours': biz['hours']
        })

result = {'count': len(late_businesses), 'businesses': late_businesses[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}]}

exec(code, env_args)
