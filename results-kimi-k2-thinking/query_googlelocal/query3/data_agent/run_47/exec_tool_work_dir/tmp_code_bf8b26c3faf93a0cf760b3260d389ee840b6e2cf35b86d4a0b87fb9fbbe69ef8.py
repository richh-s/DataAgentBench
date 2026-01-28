code = """import json

# Load the data file
hours_data = []

# Use the variable that's provided - check if it's a file path
data_file = var_functions.query_db:4

if isinstance(data_file, str) and data_file.endswith('.json'):
    with open(data_file, 'r') as file:
        hours_data = json.load(file)
else:
    hours_data = var_functions.query_db:4

print(f"Loaded {len(hours_data)} business records")

# Simple function to check if a business closes at 6PM or later on weekdays
def is_open_late(hours_str):
    if not hours_str or hours_str == "None":
        return False
    
    # Check for 24 hours
    if "24 hours" in hours_str:
        return True
    
    # Check for PM closing times
    # Extract PM times and check if hour >= 6
    import re
    pm_times = re.findall(r'(\d{1,2})(?::\d{2})?\s*PM', hours_str)
    
    for time in pm_times:
        hour = int(time)
        if hour >= 6:  # 6 PM or later
            return True
    
    return False

# Filter businesses that are open late
late_businesses = []
for business in hours_data:
    if is_open_late(business['hours']):
        late_businesses.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

late_gmap_ids = [b['gmap_id'] for b in late_businesses]

result = {
    'late_businesses': late_businesses,
    'late_gmap_ids': late_gmap_ids,
    'count': len(late_businesses)
}

print('OUTPUT:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
