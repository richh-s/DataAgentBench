code = """import json
import re

# Load the business data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses: ' + str(len(businesses)))

# Debug: Check first 10 businesses for WiFi and state format
wifi_values = set()
states_found = []

for i, business in enumerate(businesses[:20]):
    wifi = business.get('attributes', {}).get('WiFi')
    if wifi:
        wifi_values.add(str(wifi))
    
    desc = business.get('description', '')
    # Try different patterns
    patterns = [
        r'in ([A-Z]{2})',  # Original
        r'in ([A-Z][A-Z])',  # More explicit
        r'([A-Z]{2}),',  # State followed by comma
        r'\b([A-Z]{2})\b'  # Any 2-letter uppercase word
    ]
    
    for pattern in patterns:
        match = re.search(pattern, desc)
        if match:
            state = match.group(1)
            if i < 10:
                print(f'Business {i}: WiFi={wifi}, State={state}, Desc={desc[:80]}')
            states_found.append(state)
            break

print('Unique WiFi values: ' + str(wifi_values))
print('States found in sample: ' + str(set(states_found)))

# Now process all businesses
wifi_businesses = []

for business in businesses:
    wifi = business.get('attributes', {}).get('WiFi')
    if wifi:
        # Check if WiFi is offered (not 'no')
        wifi_str = str(wifi)
        # Look for actual WiFi offerings
        if 'free' in wifi_str.lower() or 'paid' in wifi_str.lower():
            desc = business.get('description', '')
            # Try to extract state
            state_match = re.search(r'in ([A-Z]{2})', desc)
            if state_match:
                state = state_match.group(1)
                wifi_businesses.append({
                    'business_id': business['business_id'],
                    'state': state
                })

print('WiFi businesses found: ' + str(len(wifi_businesses)))

if wifi_businesses:
    from collections import Counter
    state_counts = Counter([b['state'] for b in wifi_businesses])
    top_state = state_counts.most_common(1)[0]
    print('Top state: ' + top_state[0] + ' with ' + str(top_state[1]) + ' businesses')
    
    top_state_code = top_state[0]
    business_ids = [b['business_id'] for b in wifi_businesses if b['state'] == top_state_code]
    
    result = {
        'top_state': top_state_code,
        'business_count': len(business_ids),
        'business_ids': business_ids
    }
else:
    result = {'error': 'No WiFi businesses found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'error': 'No WiFi businesses found'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'top_state': None, 'business_count': 0, 'business_ids': [], 'all_state_counts': {}}, 'var_functions.execute_python:16': {'error': 'No WiFi businesses found'}}

exec(code, env_args)
