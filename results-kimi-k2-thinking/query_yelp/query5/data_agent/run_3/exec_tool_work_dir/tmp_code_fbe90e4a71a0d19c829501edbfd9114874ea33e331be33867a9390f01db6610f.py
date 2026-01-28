code = """import json
import re

# Load the business data from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    businesses = json.load(f)

print(f"Total businesses retrieved: {len(businesses)}")

# Process businesses to extract state and WiFi information
wifi_businesses = []
state_pattern = r'in ([A-Z]{2})'

for business in businesses:
    # Check if WiFi is offered (not 'no')
    wifi_attr = business.get('attributes', {}).get('WiFi', '')
    if wifi_attr and "no" not in wifi_attr.lower():
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

print(f"Businesses with WiFi: {len(wifi_businesses)}")
print(f"Sample: {wifi_businesses[:5]}")

# Count by state
from collections import Counter
state_counts = Counter([b['state'] for b in wifi_businesses])
top_states = state_counts.most_common(10)
print(f"Top states by WiFi business count: {top_states}")

# Prepare result for next step
result = {
    'wifi_businesses': wifi_businesses,
    'state_counts': dict(state_counts),
    'top_state': top_states[0] if top_states else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
