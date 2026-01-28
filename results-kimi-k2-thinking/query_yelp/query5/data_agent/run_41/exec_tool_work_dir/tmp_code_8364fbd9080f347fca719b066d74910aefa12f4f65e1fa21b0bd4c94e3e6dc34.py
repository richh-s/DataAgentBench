code = """import json
import re

businesses_file = var_functions.query_db:14
with open(businesses_file, 'r') as f:
    businesses = json.load(f)

wifi_businesses = []
for business in businesses:
    wifi_attr = business.get('attributes', {}).get('WiFi', '')
    if wifi_attr and 'no' not in wifi_attr.lower():
        wifi_businesses.append(business)

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

wifi_count = len(wifi_businesses)
total_count = len(businesses)

result = {
    'wifi_count': wifi_count,
    'total_count': total_count,
    'state_counts': state_counts,
    'state_business_ids': state_business_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'business_ref': 'businessref_47'}, {'business_ref': 'businessref_16'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_1'}, {'business_ref': 'businessref_55'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_38'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
