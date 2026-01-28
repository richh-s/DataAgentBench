code = """import json
import re

# Load the business data from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print(f"Total businesses retrieved: {len(businesses)}")

# First, let's just extract all states from descriptions to see the format
all_states = []
state_pattern = r'in ([A-Z]{2})'

for business in businesses[:50]:  # Check first 50
    description = business.get('description', '')
    state_match = re.search(state_pattern, description)
    if state_match:
        state = state_match.group(1)
        all_states.append(state)
    else:
        # Print descriptions without matches to debug
        if 'in ' in description:
            print('No match in: ' + description[:100])

print('States found in first 50: ' + str(all_states))

# Now process all businesses for WiFi
wifi_businesses = []
for i, business in enumerate(businesses):
    wifi_attr = business.get('attributes', {}).get('WiFi', None)
    if wifi_attr is not None:
        description = business.get('description', '')
        state_match = re.search(state_pattern, description)
        if state_match:
            state = state_match.group(1)
            wifi_businesses.append({
                'business_id': business['business_id'],
                'state': state,
                'wifi': str(wifi_attr)
            })
        elif i < 5:
            print('Debug - No state match for: ' + description[:100])

print('\nBusinesses with WiFi attribute: ' + str(len(wifi_businesses)))
if wifi_businesses:
    print('Sample: ' + str(wifi_businesses[:3]))
    
    # Count by state
    from collections import Counter
    state_counts = Counter([b['state'] for b in wifi_businesses])
    top_states = state_counts.most_common(5)
    print('Top states: ' + str(top_states))
    
    result = {
        'total_wifi_businesses': len(wifi_businesses),
        'top_states': top_states,
        'business_ids_sample': [b['business_id'] for b in wifi_businesses[:10]]
    }
else:
    result = {'error': 'No WiFi businesses found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'error': 'No WiFi businesses found'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'top_state': None, 'business_count': 0, 'business_ids': [], 'all_state_counts': {}}}

exec(code, env_args)
