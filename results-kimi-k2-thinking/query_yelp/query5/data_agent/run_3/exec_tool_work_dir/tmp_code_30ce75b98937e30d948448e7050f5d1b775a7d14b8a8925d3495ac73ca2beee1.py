code = """import json
import re

# Load the business data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses: ' + str(len(businesses)))

# First, let's just count all businesses by state to verify state extraction works
all_states = []
state_pattern = r'in ([A-Z]{2})'

for business in businesses[:1000]:  # Sample first 1000
    desc = business.get('description', '')
    state_match = re.search(state_pattern, desc)
    if state_match:
        state = state_match.group(1)
        all_states.append(state)

from collections import Counter
state_counts_all = Counter(all_states)
print('Top states (all businesses): ' + str(state_counts_all.most_common(10)))

# Now find WiFi businesses
wifi_businesses = []
wifi_values = set()

for business in businesses:
    wifi = business.get('attributes', {}).get('WiFi')
    if wifi is not None:
        wifi_str = str(wifi)
        wifi_values.add(wifi_str)
        # Exclude only 'no', include everything else
        if 'no' not in wifi_str.lower():
            desc = business.get('description', '')
            state_match = re.search(state_pattern, desc)
            if state_match:
                state = state_match.group(1)
                wifi_businesses.append({
                    'business_id': business['business_id'],
                    'state': state
                })

print('Unique WiFi values: ' + str(wifi_values))
print('WiFi businesses found: ' + str(len(wifi_businesses)))

if wifi_businesses:
    state_counts_wifi = Counter([b['state'] for b in wifi_businesses])
    top_state = state_counts_wifi.most_common(1)[0]
    print('Top state: ' + top_state[0] + ' with ' + str(top_state[1]) + ' WiFi businesses')
    
    top_state_code = top_state[0]
    business_ids = [b['business_id'] for b in wifi_businesses if b['state'] == top_state_code]
    
    result = {
        'top_state': top_state_code,
        'business_count': len(business_ids),
        'business_ids': business_ids[:2000]  # Limit for querying
    }
else:
    result = {'error': 'No WiFi businesses found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'error': 'No WiFi businesses found'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'top_state': None, 'business_count': 0, 'business_ids': [], 'all_state_counts': {}}, 'var_functions.execute_python:16': {'error': 'No WiFi businesses found'}, 'var_functions.execute_python:18': {'error': 'No WiFi businesses found'}}

exec(code, env_args)
