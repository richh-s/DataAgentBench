code = """import json

# Read the file from the storage
file_path = var_functions.query_db:2

with open(file_path, 'r') as f:
    businesses = json.load(f)

# Let's examine the structure and find businesses with WiFi
wifi_businesses = []
for business in businesses:
    attributes = business.get('attributes', {})
    if attributes and isinstance(attributes, dict):
        wifi = attributes.get('WiFi')
        if wifi and 'free' in str(wifi).lower():
            wifi_businesses.append(business)

print('__RESULT__:')
print(json.dumps({
    'total_businesses': len(businesses),
    'wifi_businesses_count': len(wifi_businesses),
    'sample_wifi': wifi_businesses[:3]
}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
