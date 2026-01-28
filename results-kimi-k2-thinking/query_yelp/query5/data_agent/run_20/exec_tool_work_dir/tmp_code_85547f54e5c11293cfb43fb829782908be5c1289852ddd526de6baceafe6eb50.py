code = """import json
import pandas as pd
import re

# Read the business data from the JSON file
business_file_path = locals()['var_functions.query_db:10']
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Filter businesses that have WiFi attribute
wifi_businesses = []

for business in business_data:
    # Check if attributes field exists and contains WiFi
    if 'attributes' in business and business['attributes'] is not None:
        if isinstance(business['attributes'], dict) and 'WiFi' in business['attributes']:
            wifi_value = business['attributes']['WiFi']
            # Check if WiFi is enabled (free, paid, etc., but not 'no')
            if wifi_value and 'no' not in str(wifi_value).lower():
                # Extract state from description
                description = business.get('description', '')
                if description:
                    # Look for state pattern (e.g., "CA", "PA", "FL")
                    # Pattern: Look for 2-letter state codes at the end of location or before zip
                    state_match = re.search(r'[A-Z]{2}', description)
                    if state_match:
                        state = state_match.group()
                        # Verify it's a US state (basic check)
                        us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                                   'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                                   'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                                   'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                                   'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
                        if state in us_states:
                            wifi_businesses.append({
                                'business_id': business['business_id'],
                                'state': state,
                                'wifi': wifi_value,
                                'name': business.get('name', '')
                            })

# Create DataFrame and count by state
df_wifi = pd.DataFrame(wifi_businesses)
if not df_wifi.empty:
    state_counts = df_wifi['state'].value_counts()
    top_state = state_counts.index[0]
    top_state_count = state_counts.iloc[0]
    
    print('__RESULT__:')
    print(json.dumps({
        'top_state': top_state,
        'top_state_count': int(top_state_count),
        'total_wifi_businesses': int(len(wifi_businesses)),
        'state_counts': state_counts.to_dict()
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'error': 'No WiFi businesses found',
        'total_processed': len(business_data)
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
