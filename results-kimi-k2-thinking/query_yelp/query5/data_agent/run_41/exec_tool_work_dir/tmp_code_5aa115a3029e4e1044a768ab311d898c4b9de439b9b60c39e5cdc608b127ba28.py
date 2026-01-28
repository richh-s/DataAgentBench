code = """import json
import re

# Get businesses data
businesses_file = var_functions.query_db:8
with open(businesses_file, 'r') as f:
    businesses = json.load(f)

# Filter businesses that offer WiFi (not "no")
wifi_businesses = []
for business in businesses:
    wifi_attr = business.get('attributes', {}).get('WiFi', '')
    if wifi_attr and 'no' not in wifi_attr.lower():
        wifi_businesses.append(business)

print(f"Total businesses with WiFi data: {len(businesses)}")
print(f"Businesses that offer WiFi: {len(wifi_businesses)}")

# Parse state from description (format: "... in City, ST")
state_pattern = r'in [^,]+, ([A-Z]{2})'
state_counts = {}
businesses_by_state = {}

for business in wifi_businesses:
    description = business.get('description', '')
    match = re.search(state_pattern, description)
    if match:
        state = match.group(1)
        state_counts[state] = state_counts.get(state, 0) + 1
        if state not in businesses_by_state:
            businesses_by_state[state] = []
        businesses_by_state[state].append(business)

# Sort states by count
sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)

print(f"States found: {len(sorted_states)}")
print(f"Top 10 states by WiFi business count:")
for state, count in sorted_states[:10]:
    print(f"  {state}: {count}")

# Prepare results for export
top_state = sorted_states[0] if sorted_states else None
result = {
    'total_wifi_businesses': len(wifi_businesses),
    'state_counts': state_counts,
    'top_state': top_state,
    'businesses_by_state': businesses_by_state
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'business_ref': 'businessref_47'}, {'business_ref': 'businessref_16'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_1'}, {'business_ref': 'businessref_55'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_38'}]}

exec(code, env_args)
