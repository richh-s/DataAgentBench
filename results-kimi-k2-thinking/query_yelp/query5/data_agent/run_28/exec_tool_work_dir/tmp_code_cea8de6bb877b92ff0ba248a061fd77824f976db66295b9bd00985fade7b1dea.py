code = """import json
import re

# Get the WiFi businesses data
wifi_result = locals()['var_functions.query_db:12']

# Load from file if needed
if isinstance(wifi_result, str) and wifi_result.endswith('.json'):
    with open(wifi_result, 'r') as f:
        wifi_businesses_raw = json.load(f)
else:
    wifi_businesses_raw = wifi_result

print(f"Total records: {len(wifi_businesses_raw)}")

# Examine first few records with WiFi
wifi_samples = []
for i, b in enumerate(wifi_businesses_raw[:10]):
    if isinstance(b.get('attributes'), dict) and b['attributes'].get('WiFi'):
        sample = {
            'index': i,
            'name': b.get('name'),
            'wifi': b['attributes']['WiFi'],
            'description': b.get('description', '')[:100]
        }
        wifi_samples.append(sample)

print(f"WiFi samples: {json.dumps(wifi_samples, indent=2)}")

# Now let's try a different approach - parse description more carefully
wifi_businesses = []
us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

print("\nTrying to extract states...")
for b in wifi_businesses_raw[:20]:  # Just check first 20
    if isinstance(b.get('attributes'), dict) and b['attributes'].get('WiFi'):
        wifi_value = str(b['attributes']['WiFi']).lower()
        # Check if WiFi is available (not 'no')
        has_wifi = 'no' not in wifi_value
        
        desc = b.get('description', '')
        # Try multiple patterns to find state
        patterns = [
            r'\bin\s+[A-Za-z\s,]+\b([A-Z]{2})\b',  # after 'in'
            r'\b([A-Z]{2})\b',  # any 2-letter code
            r'\b([A-Z]{2})\b[^.]*$',  # at end of text
        ]
        
        state_found = None
        for pattern in patterns:
            match = re.search(pattern, desc)
            if match:
                state = match.group(1)
                if state in us_states:
                    state_found = state
                    break
        
        if has_wifi and state_found:
            print(f"FOUND: {b['name']} - State: {state_found}, WiFi: {b['attributes']['WiFi']}")
        elif has_wifi:
            print(f"NO STATE: {b['name']} - WiFi: {b['attributes']['WiFi']}, Desc: {desc[:80]}")

print('__RESULT__:')
print(json.dumps({'status': 'debug complete'}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['review', 'tip', 'user'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:22': {'error': 'No WiFi businesses with valid states'}}

exec(code, env_args)
