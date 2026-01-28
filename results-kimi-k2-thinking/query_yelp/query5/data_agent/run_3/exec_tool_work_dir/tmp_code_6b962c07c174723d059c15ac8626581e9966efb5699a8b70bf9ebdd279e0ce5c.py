code = """import json
import re

# Load the business data from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print(f"Total businesses retrieved: {len(businesses)}")

# Process businesses to extract state and WiFi information
wifi_businesses = []
state_pattern = r'in ([A-Z]{2})'

for business in businesses:
    # Check if WiFi attribute exists and has a value
    wifi_attr = business.get('attributes', {}).get('WiFi', None)
    if wifi_attr is not None:
        # Check if it's offered (not 'no')
        if isinstance(wifi_attr, str) and 'no' not in wifi_attr.lower():
            # Extract state from description
            description = business.get('description', '')
            state_match = re.search(state_pattern, description)
            if state_match:
                state = state_match.group(1)
                wifi_businesses.append({
                    'business_id': business['business_id'],
                    'state': state,
                    'name': business.get('name', ''),
                    'wifi': wifi_attr
                })

print(f"Businesses with WiFi (not 'no'): {len(wifi_businesses)}")

# Count by state
from collections import Counter
state_counts = Counter([b['state'] for b in wifi_businesses])
top_states = state_counts.most_common(10)
print(f"Top states by WiFi business count: {top_states}")

# Get top state
top_state = None
business_ids_top_state = []
if top_states:
    top_state = top_states[0][0]
    business_ids_top_state = [b['business_id'] for b in wifi_businesses if b['state'] == top_state]
    print(f"Top state: {top_state} with {len(business_ids_top_state)} WiFi businesses")
    print(f"Sample business IDs: {business_ids_top_state[:5]}")

result = {
    'top_state': top_state,
    'business_count': len(business_ids_top_state),
    'business_ids': business_ids_top_state[:1000],  # Limit for next query
    'all_state_counts': dict(state_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'error': 'No WiFi businesses found'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
