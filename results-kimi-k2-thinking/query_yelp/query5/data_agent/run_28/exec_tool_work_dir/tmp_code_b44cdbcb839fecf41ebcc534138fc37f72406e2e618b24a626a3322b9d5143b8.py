code = """import json
import re

# Access the stored result using the correct variable name
wifi_result = locals()['var_functions.query_db:12']

# Load the data from file if it's a file path
if isinstance(wifi_result, str) and wifi_result.endswith('.json'):
    with open(wifi_result, 'r') as f:
        wifi_businesses_raw = json.load(f)
    print(f"Loaded from file: {wifi_result}")
else:
    wifi_businesses_raw = wifi_result
    print(f"Using direct data, type: {type(wifi_result)}")

print(f"Total records loaded: {len(wifi_businesses_raw)}")

# Process businesses
wifi_businesses = []
us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

# Debug: Check WiFi values
wifi_values = set()
for b in wifi_businesses_raw[:20]:  # Sample first 20
    if isinstance(b.get('attributes'), dict) and b['attributes'].get('WiFi'):
        wifi_values.add(str(b['attributes']['WiFi']))

print(f"Sample WiFi values: {wifi_values}")

# Extract state for each business
for b in wifi_businesses_raw:
    if isinstance(b.get('attributes'), dict) and b['attributes'].get('WiFi'):
        wifi_value = str(b['attributes']['WiFi']).lower()
        # Only include if WiFi is available (not 'no')
        if 'no' not in wifi_value:
            desc = b.get('description', '')
            # Try to find state code
            match = re.search(r'\bin\s+[A-Za-z\s,]+\b([A-Z]{2})\b', desc)
            if match:
                state = match.group(1)
                if state in us_states:
                    wifi_businesses.append({
                        'business_id': b['business_id'],
                        'name': b['name'],
                        'state': state,
                        'wifi_value': b['attributes']['WiFi']
                    })

print(f"WiFi businesses with valid states: {len(wifi_businesses)}")

if wifi_businesses:
    from collections import Counter
    state_counts = Counter([b['state'] for b in wifi_businesses])
    top_states = state_counts.most_common(10)
    print(f"Top 10 states: {top_states}")
    
    # Get top state info
    if top_states:
        top_state = top_states[0]
        print(f"Top state: {top_state[0]} with {top_state[1]} businesses")
        
        # Get business refs for top state (convert businessid_ to businessref_)
        top_state_business_ids = []
        for b in wifi_businesses:
            if b['state'] == top_state[0]:
                # Convert: businessid_X -> businessref_X
                bid = b['business_id'].replace('businessid_', 'businessref_')
                top_state_business_ids.append(bid)
        
        print(f"Converted business IDs for reviews: {len(top_state_business_ids)}")
        
        result = {
            'wifi_businesses': wifi_businesses,
            'state_counts': dict(state_counts),
            'top_state_code': top_state[0],
            'top_state_business_refs': top_state_business_ids
        }
    else:
        result = {'error': 'No states found'}
else:
    result = {'error': 'No WiFi businesses with valid states'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['review', 'tip', 'user'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
