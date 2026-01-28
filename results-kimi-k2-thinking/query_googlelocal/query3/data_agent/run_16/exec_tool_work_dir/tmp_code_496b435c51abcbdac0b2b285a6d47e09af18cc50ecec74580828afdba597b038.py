code = """import json
import re
import ast

# The storage key is var_functions.query_db:10
# Access it differently 
businesses_data = locals()['var_functions.query_db:10']

# Now parse the hours to find businesses open after 6PM
def parse_hours(hours_str):
    if not hours_str or hours_str == 'None':
        return []
    try:
        return ast.literal_eval(hours_str)
    except:
        return []

def is_open_after_6pm(hours_list):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            
            # Extract closing time
            if '–' in time_range:
                parts = time_range.split('–')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) < 2:
                continue
                
            closing = parts[1].strip()
            
            # Parse time
            if 'PM' in closing:
                closing = closing.replace('PM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    hour = int(hour_part) if hour_part.isdigit() else 0
                    if hour != 12:
                        hour += 12
                else:
                    hour = int(closing) if closing.isdigit() else 0
                    if hour != 12:
                        hour += 12
                if hour >= 18:
                    return True
            elif 'AM' in closing:
                closing = closing.replace('AM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    hour = int(hour_part) if hour_part.isdigit() else 0
                else:
                    hour = int(closing) if closing.isdigit() else 0
                if hour == 12:
                    hour = 0
                if hour >= 18:
                    return True
    
    return False

# Find businesses open after 6PM
open_after_6 = []
for business in businesses_data:
    hours_list = parse_hours(business.get('hours', ''))
    if is_open_after_6pm(hours_list):
        open_after_6.append({
            'gmap_id': business.get('gmap_id'),
            'name': business.get('name'),
            'state': business.get('state', ''),
            'hours': business.get('hours', '')
        })

print(f'Found {len(open_after_6)} businesses open after 6PM')

# Get ratings for these businesses
print('__RESULT__:')
print(json.dumps(open_after_6))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:5': ['business_description'], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'count': 39}}

exec(code, env_args)
