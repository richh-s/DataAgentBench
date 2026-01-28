code = """import json
import re

# Read the full data
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    businesses = json.load(f)

print(f"Total businesses queried: {len(businesses)}")

# Filter for businesses that offer WiFi (not "no")
wifi_businesses = []
for business in businesses:
    wifi_attr = business.get('attributes', {}).get('WiFi', '')
    # Parse the WiFi attribute value
    if wifi_attr and 'no' not in wifi_attr.lower():
        wifi_businesses.append(business)

print(f"Businesses with WiFi: {len(wifi_businesses)}")

# Parse state from description
state_pattern = r'\b([A-Z]{2})\b'
state_counts = {}

for business in wifi_businesses:
    description = business.get('description', '')
    match = re.search(state_pattern, description)
    if match:
        state = match.group(1)
        state_counts[state] = state_counts.get(state, 0) + 1

# Sort states by count
sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
print(f"States with WiFi businesses: {len(sorted_states)}")
print(f"Top states: {sorted_states[:10]}")

# Now get business IDs to query reviews
wifi_business_ids = [b['business_id'] for b in wifi_businesses]

# Save results for next steps
result = {
    'wifi_businesses': wifi_businesses,
    'state_counts': state_counts,
    'top_state': sorted_states[0] if sorted_states else None,
    'wifi_business_ids': wifi_business_ids
}

import json as js
print('__RESULT__:')
print(js.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
