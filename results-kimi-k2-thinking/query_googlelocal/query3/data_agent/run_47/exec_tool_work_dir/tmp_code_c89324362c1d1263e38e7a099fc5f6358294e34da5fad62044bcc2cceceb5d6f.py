code = """import json

# Load the data from the file
file_path = var_functions.query_db:4
print('File path:', file_path)
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = var_functions.query_db:4

print(f"Loaded {len(data)} records")

# Function to parse hours and check if open after 6pm on weekdays
def check_open_late(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # The hours field contains a string representation of a list
        hours_list = eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                if hours == 'Open 24 hours':
                    return True
                # Check for dash in time range
                if '–' in hours:
                    parts = hours.split('–')
                elif '-' in hours:
                    parts = hours.split('-')
                else:
                    continue
                if len(parts) >= 2:
                    close = parts[1].strip()
                    if 'PM' in close:
                        # Extract hour
                        hour_str = close.replace('PM', '').strip()
                        if ':' in hour_str:
                            h = int(hour_str.split(':')[0])
                        else:
                            h = int(hour_str)
                        if h != 12:
                            h += 12
                        if h >= 18:  # 6 PM or later
                            return True
    except:
        pass
    return False

# Filter businesses
open_late = []
for item in data:
    if check_open_late(item['hours']):
        open_late.append({'gmap_id': item['gmap_id'], 'name': item['name'], 'hours': item['hours']})

print(f"Found {len(open_late)} businesses open after 6 PM")

# Get list of gmap_ids
gmap_ids = [b['gmap_id'] for b in open_late]

result = {'businesses': open_late, 'gmap_ids': gmap_ids, 'count': len(open_late)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
