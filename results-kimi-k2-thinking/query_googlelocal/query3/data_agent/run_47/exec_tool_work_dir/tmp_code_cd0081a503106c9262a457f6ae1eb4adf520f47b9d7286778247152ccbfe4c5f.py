code = """import json
import os

# Debug: print available variables
available_vars = list(locals().keys())
print('Available variables:', available_vars[:10])

# Find the data - check if it's a file path or direct data
hours_data = None
for var_name in available_vars:
    if 'query_db' in var_name:
        print('Found variable:', var_name)
        value = locals()[var_name]
        print('Type:', type(value))
        print('Content preview:', str(value)[:200])
        
        if isinstance(value, str) and value.endswith('.json'):
            print('Loading from JSON file')
            with open(value, 'r') as f:
                hours_data = json.load(f)
        elif isinstance(value, list):
            print('Direct data list')
            hours_data = value
        break

if hours_data is None:
    print('Could not find hours data')
    hours_data = []

print('Total records loaded:', len(hours_data))
print('First record sample:', hours_data[0] if hours_data else 'No data')"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
