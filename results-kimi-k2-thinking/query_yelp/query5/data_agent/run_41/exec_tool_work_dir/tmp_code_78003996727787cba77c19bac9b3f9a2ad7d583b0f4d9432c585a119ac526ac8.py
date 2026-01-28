code = """import json
import re

businesses_file = var_functions.query_db:14
with open(businesses_file, 'r') as f:
    businesses = json.load(f)

# Filter businesses that offer WiFi (not "no")
wifi_businesses = []
for business in businesses:
    wifi_attr = business.get('attributes', {}).get('WiFi', '')
    if wifi_attr and 'no' not in wifi_attr.lower():
        wifi_businesses.append(business)

print(f"Total businesses: {len(businesses)}")
print(f"WiFi businesses: {len(wifi_businesses)}")

# Extract state from description
state_pattern = r'in [^,]+, ([A-Z]{2})'
state_counts = {}
state_business_ids = {}

for business in wifi_businesses:
    description = business.get('description', '')
    match = re.search(state_pattern, description)
    if match:
        state = match.group(1)
        state_counts[state] = state_counts.get(state, 0) + 1
        if state not in state_business_ids:
            state_business_ids[state] = []
        state_business_ids[state].append(business['business_id'])

if state_counts:
    top_state = max(state_counts.items(), key=lambda x: x[1])
    print(f"Top state: {top_state[0]} with {top_state[1]} businesses")
    print(f"Total states: {len(state_counts)}")
else:
    top_state = None
    print("No states found")

result = {
    'wifi_businesses': wifi_businesses,
    'state_counts': state_counts,
    'top_state': top_state,
    'state_business_ids': state_business_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'business_ref': 'businessref_47'}, {'business_ref': 'businessref_16'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_1'}, {'business_ref': 'businessref_55'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_38'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
