code = """import json
import re

# Load the business data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses: ' + str(len(businesses)))

# Debug: Check all unique WiFi values and count them
wifi_values = {}
for business in businesses:
    wifi = business.get('attributes', {}).get('WiFi')
    if wifi is not None:
        wifi_str = str(wifi)
        wifi_values[wifi_str] = wifi_values.get(wifi_str, 0) + 1

print('All WiFi values and counts: ' + str(wifi_values))

# Now find WiFi businesses (excluding 'no')
wifi_businesses = []
state_pattern = r'in ([A-Z]{2})'

for business in businesses:
    wifi = business.get('attributes', {}).get('WiFi')
    if wifi is not None:
        wifi_str = str(wifi)
        # Check if it's not 'no'
        if 'no' not in wifi_str.lower():
            desc = business.get('description', '')
            state_match = re.search(state_pattern, desc)
            if state_match:
                state = state_match.group(1)
                wifi_businesses.append({
                    'business_id': business['business_id'],
                    'state': state,
                    'wifi': wifi_str
                })

print('WiFi businesses (excluding no): ' + str(len(wifi_businesses)))

if wifi_businesses:
    from collections import Counter
    state_counts = Counter([b['state'] for b in wifi_businesses])
    top_states = state_counts.most_common(10)
    print('Top states: ' + str(top_states))
    
    if top_states:
        top_state = top_states[0]
        print('Top state: ' + top_state[0] + ' with ' + str(top_state[1]) + ' businesses')
        
        # Get all business IDs for top state
        top_state_code = top_state[0]
        business_ids = [b['business_id'] for b in wifi_businesses if b['state'] == top_state_code]
        
        result = {
            'top_state': top_state_code,
            'business_count': len(business_ids),
            'business_ids': business_ids
        }
    else:
        result = {'error': 'No top state found'}
else:
    result = {'error': 'No WiFi businesses found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'error': 'No WiFi businesses found'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'top_state': None, 'business_count': 0, 'business_ids': [], 'all_state_counts': {}}, 'var_functions.execute_python:16': {'error': 'No WiFi businesses found'}, 'var_functions.execute_python:18': {'error': 'No WiFi businesses found'}, 'var_functions.execute_python:20': {'error': 'No WiFi businesses found'}}

exec(code, env_args)
