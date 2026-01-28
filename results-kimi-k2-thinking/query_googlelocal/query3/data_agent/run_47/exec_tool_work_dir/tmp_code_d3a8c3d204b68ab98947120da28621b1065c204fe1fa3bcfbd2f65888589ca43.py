code = """import json

# Get the variable name with the data
var_name = 'var_functions.query_db:4'
print('Variable name:', var_name)

# Access via locals() dictionary to handle the colon in the name
data_var = locals().get(var_name)
print('Data variable loaded:', data_var is not None)

hours_data = []
if data_var is not None:
    if isinstance(data_var, str) and data_var.endswith('.json'):
        with open(data_var, 'r') as f:
            hours_data = json.load(f)
    else:
        hours_data = data_var

print('Loaded', len(hours_data), 'business records')

# Function to check if open after 6PM on weekdays
def check_hours(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # This is a string representation of a Python list
        hours_list = eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                if hours == 'Open 24 hours':
                    return True
                
                # Parse the closing time
                time_range = hours
                if '–' in time_range:
                    parts = time_range.split('–')
                elif '-' in time_range:
                    parts = time_range.split('-')
                else:
                    continue
                
                if len(parts) >= 2:
                    close_time = parts[1].strip()
                    if 'PM' in close_time:
                        # Extract hour
                        hour_part = close_time.replace('PM', '').replace(' ', '')
                        if ':' in hour_part:
                            hour = int(hour_part.split(':')[0])
                        else:
                            hour = int(hour_part)
                        
                        if hour != 12:
                            hour += 12
                        
                        if hour >= 18:  # 6 PM or later
                            return True
    except:
        return False
    
    return False

# Filter businesses
open_late = []
for business in hours_data:
    if check_hours(business['hours']):
        open_late.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print('Found', len(open_late), 'businesses open after 6 PM on weekdays')

# Get gmap_ids
gmap_ids = [b['gmap_id'] for b in open_late]

result = {
    'businesses': open_late,
    'gmap_ids': gmap_ids,
    'count': len(open_late)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
