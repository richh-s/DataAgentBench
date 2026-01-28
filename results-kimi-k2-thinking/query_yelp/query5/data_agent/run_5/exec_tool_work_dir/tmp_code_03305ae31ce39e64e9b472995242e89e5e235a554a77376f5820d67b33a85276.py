code = """import json
import re

# Read the businesses data
businesses = locals()['var_functions.query_db:18']

# Check if it's a file path string
if isinstance(businesses, str):
    with open(businesses, 'r') as f:
        businesses = json.load(f)

print(f"Total businesses loaded: {len(businesses)}")

# Process businesses to find WiFi-enabled ones and extract states
wifi_businesses = []
state_wifi_counts = {}

for business in businesses:
    business_id = business.get('business_id', '')
    attributes = business.get('attributes', {})
    description = business.get('description', '')
    
    # Skip if attributes is None or "None" string
    if not attributes or attributes == "None":
        continue
    
    # Check if WiFi attribute exists and is not 'no'
    if isinstance(attributes, dict):
        wifi_value = attributes.get('WiFi')
        if wifi_value and isinstance(wifi_value, str):
            # Clean up the WiFi value
            wifi_clean = wifi_value.replace("u'", "").replace("'", "").strip()
            
            # Only count businesses that actually offer WiFi (not 'no')
            if wifi_clean != 'no':
                # Extract state from description
                state = None
                if description:
                    # Try different patterns to extract state
                    patterns = [
                        r',\s*([A-Z]{2})\s+\d{5}',  # ", ST 12345"
                        r'\bin\s+([A-Z]{2})\b',  # "in ST"
                        r',\s*([A-Z]{2})\s*,',  # ", ST,"
                        r'Located\s+at\s+.*?\bin\s+([A-Za-z]+)',  # "in City"
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, description)
                        if match:
                            state = match.group(1)
                            # Convert full state name to abbreviation if needed
                            state_abbrev_map = {
                                'California': 'CA', 'Florida': 'FL', 'Texas': 'TX', 
                                'New York': 'NY', 'Pennsylvania': 'PA', 'Illinois': 'IL',
                                'Ohio': 'OH', 'Georgia': 'GA', 'North Carolina': 'NC',
                                'Michigan': 'MI', 'New Jersey': 'NJ', 'Virginia': 'VA',
                                'Washington': 'WA', 'Arizona': 'AZ', 'Massachusetts': 'MA',
                                'Tennessee': 'TN', 'Indiana': 'IN', 'Missouri': 'MO',
                                'Maryland': 'MD', 'Wisconsin': 'WI', 'Minnesota': 'MN',
                                'Colorado': 'CO', 'Alabama': 'AL', 'South Carolina': 'SC',
                                'Louisiana': 'LA', 'Kentucky': 'KY', 'Oregon': 'OR',
                                'Oklahoma': 'OK', 'Connecticut': 'CT', 'Utah': 'UT',
                                'Iowa': 'IA', 'Nevada': 'NV', 'Arkansas': 'AR',
                                'Mississippi': 'MS', 'Kansas': 'KS', 'New Mexico': 'NM',
                                'Nebraska': 'NE', 'West Virginia': 'WV', 'Idaho': 'ID',
                                'Hawaii': 'HI', 'New Hampshire': 'NH', 'Maine': 'ME',
                                'Montana': 'MT', 'Rhode Island': 'RI', 'Delaware': 'DE',
                                'South Dakota': 'SD', 'North Dakota': 'ND', 'Alaska': 'AK',
                                'Vermont': 'VT', 'Wyoming': 'WY'
                            }
                            if state in state_abbrev_map:
                                state = state_abbrev_map[state]
                            break
                
                wifi_businesses.append({
                    'business_id': business_id,
                    'wifi': wifi_clean,
                    'state': state,
                    'description': description
                })
                
                if state:
                    state_wifi_counts[state] = state_wifi_counts.get(state, 0) + 1

# Sort states by WiFi business count
sorted_states = sorted(state_wifi_counts.items(), key=lambda x: x[1], reverse=True)

print(f"Total WiFi-enabled businesses: {len(wifi_businesses)}")
print(f"Top states by WiFi business count: {sorted_states[:10]}")

print("__RESULT__:")
print(json.dumps({
    'total_wifi_businesses': len(wifi_businesses),
    'state_wifi_counts': sorted_states,
    'wifi_businesses': wifi_businesses
}))"""

env_args = {'var_functions.query_db:0': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:4': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_wifi_businesses': 35, 'top_states': [['PA', 12], ['FL', 5], ['MO', 4], ['IN', 4], ['LA', 2], ['NV', 2], ['ID', 2], ['AB', 2], ['CA', 1], ['IL', 1]], 'business_list': [{'business_id': 'businessid_49', 'wifi': "u'no'", 'state': 'CA'}, {'business_id': 'businessid_92', 'wifi': "u'no'", 'state': 'PA'}, {'business_id': 'businessid_64', 'wifi': "u'free'", 'state': 'MO'}, {'business_id': 'businessid_54', 'wifi': "u'free'", 'state': 'FL'}, {'business_id': 'businessid_91', 'wifi': "u'free'", 'state': 'LA'}, {'business_id': 'businessid_93', 'wifi': "u'free'", 'state': 'IL'}, {'business_id': 'businessid_24', 'wifi': "u'no'", 'state': 'MO'}, {'business_id': 'businessid_26', 'wifi': "u'free'", 'state': 'FL'}, {'business_id': 'businessid_89', 'wifi': "u'free'", 'state': 'PA'}, {'business_id': 'businessid_32', 'wifi': "u'no'", 'state': 'LA'}, {'business_id': 'businessid_97', 'wifi': "u'free'", 'state': 'PA'}, {'business_id': 'businessid_27', 'wifi': "u'no'", 'state': 'NV'}, {'business_id': 'businessid_67', 'wifi': "u'free'", 'state': 'PA'}, {'business_id': 'businessid_7', 'wifi': "u'no'", 'state': 'ID'}, {'business_id': 'businessid_51', 'wifi': "u'free'", 'state': 'FL'}, {'business_id': 'businessid_5', 'wifi': "'no'", 'state': 'AB'}, {'business_id': 'businessid_6', 'wifi': "'free'", 'state': 'NV'}, {'business_id': 'businessid_87', 'wifi': "u'no'", 'state': 'IN'}, {'business_id': 'businessid_55', 'wifi': "u'free'", 'state': 'FL'}, {'business_id': 'businessid_96', 'wifi': "u'no'", 'state': 'MO'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:16': {'total_wifi_businesses': 1, 'state_counts': [['CA', 1]], 'sample_businesses': [{'business_id': 'businessid_49', 'wifi': "u'no", 'state': 'CA'}]}, 'var_functions.query_db:18': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
