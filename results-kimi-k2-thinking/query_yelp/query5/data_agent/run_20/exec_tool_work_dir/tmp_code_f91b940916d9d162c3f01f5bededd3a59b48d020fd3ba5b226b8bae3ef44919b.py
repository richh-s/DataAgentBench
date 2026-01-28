code = """import json
import re

# Read the business data again to get PA businesses with WiFi
business_file_path = locals()['var_functions.query_db:10']
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Find PA businesses with WiFi (not 'no')
pa_wifi_business_ids = []
us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
             'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
             'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
             'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
             'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for business in business_data:
    if 'attributes' in business and business['attributes'] is not None:
        if isinstance(business['attributes'], dict) and 'WiFi' in business['attributes']:
            wifi_value = business['attributes']['WiFi']
            if wifi_value and 'no' not in str(wifi_value).lower():
                description = business.get('description', '')
                if description:
                    state_match = re.search(r'[A-Z]{2}', description)
                    if state_match:
                        state = state_match.group()
                        if state == 'PA' and state in us_states:
                            pa_wifi_business_ids.append(business['business_id'])

print('__RESULT__:')
print(json.dumps({
    'pa_wifi_business_ids': pa_wifi_business_ids,
    'count': len(pa_wifi_business_ids)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'top_state': 'PA', 'top_state_count': 8, 'total_wifi_businesses': 21, 'state_counts': {'PA': 8, 'FL': 5, 'IN': 2, 'MO': 2, 'IL': 1, 'LA': 1, 'NV': 1, 'ID': 1}}}

exec(code, env_args)
