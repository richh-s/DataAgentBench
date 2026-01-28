code = """import json
import re

file_path = var_functions.query_db:4
print('Loading data from:', file_path)

if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        hours_data = json.load(f)
else:
    hours_data = var_functions.query_db:4

print('Loaded', len(hours_data), 'records')

# Function to check if open after 6pm
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        hours_list = eval(hours_str)
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                if hours == 'Open 24 hours':
                    return True
                dash = '–' if '–' in hours else '-'
                if dash in hours:
                    parts = hours.split(dash)
                    if len(parts) >= 2:
                        close_time = parts[1].strip()
                        if 'PM' in close_time:
                            hour_part = close_time.replace('PM', '').replace(' ', '')
                            if ':' in hour_part:
                                hour = int(hour_part.split(':')[0])
                            else:
                                hour = int(hour_part)
                            if hour != 12:
                                hour += 12
                            if hour >= 18:
                                return True
    except:
        return False
    return False

# Filter businesses
open_late = []
for business in hours_data:
    if is_open_after_6pm(business['hours']):
        open_late.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print('Found', len(open_late), 'businesses open after 6 PM')

# Get gmap_ids
gmap_ids = [b['gmap_id'] for b in open_late]

result = {'businesses': open_late, 'gmap_ids': gmap_ids, 'count': len(open_late)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
