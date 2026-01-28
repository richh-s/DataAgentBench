code = """import json
import pandas as pd
import re

# Read the business data from storage
business_data = var_functions.query_db:5

# Filter businesses with WiFi attribute
wifi_businesses = []
for business in business_data:
    if business.get('attributes') and business['attributes'] != 'None':
        if isinstance(business['attributes'], dict) and 'WiFi' in business['attributes']:
            wifi_status = business['attributes']['WiFi']
            if wifi_status and wifi_status != "u'no'":
                wifi_businesses.append(business)

# Extract state from description
for business in wifi_businesses:
    desc = business.get('description', '')
    state_match = re.search(r',\s*([A-Z]{2})\s*', desc)
    if state_match:
        business['state'] = state_match.group(1)
    else:
        business['state'] = None

# Count businesses per state with WiFi
state_counts = {}
for business in wifi_businesses:
    state = business['state']
    if state:
        state_counts[state] = state_counts.get(state, 0) + 1

# Sort by count to find the state with highest number
sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)

# Extract business_ids for the top state to fetch their ratings
if sorted_states:
    top_state = sorted_states[0][0]
    top_state_business_ids = []
    for business in wifi_businesses:
        if business['state'] == top_state:
            # Convert businessid_ prefix to businessref_ prefix
            bus_id = business['business_id'].replace('businessid_', '')
            top_state_business_ids.append(f'businessref_{bus_id}')
else:
    top_state = None
    top_state_business_ids = []

# Prepare result
result = {
    'state_counts': sorted_states,
    'wifi_businesses_count': len(wifi_businesses),
    'top_state': top_state,
    'top_state_business_ids': top_state_business_ids[:10]  # Sample for query
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
