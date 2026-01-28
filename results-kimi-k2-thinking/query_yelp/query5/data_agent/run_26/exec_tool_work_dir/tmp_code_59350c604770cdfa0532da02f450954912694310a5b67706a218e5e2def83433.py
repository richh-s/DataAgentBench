code = """import json
import re

# Read the file path from storage
file_path = locals()['var_functions.query_db:14']
print('File path:', file_path)

# Read the business data
all_business_data = json.load(open(file_path, 'r'))
print('Loaded', len(all_business_data), 'businesses')

# Extract WiFi businesses and their states
wifi_businesses = []

for business in all_business_data:
    business_id = business['business_id']
    name = business['name']
    description = business.get('description', '')
    attributes = business.get('attributes', {})
    
    # Extract state (two-letter code after city)
    state_match = re.search(r',\s*([A-Z]{2})\s*,', description)
    if not state_match:
        state_match = re.search(r',\s*([A-Z]{2})\s*$', description)
    
    state = state_match.group(1) if state_match else None
    
    # Check if business offers WiFi
    has_wifi = False
    if isinstance(attributes, dict) and 'WiFi' in attributes:
        wifi_value = str(attributes['WiFi']).lower()
        if 'free' in wifi_value or 'paid' in wifi_value:
            has_wifi = True
    
    if state and has_wifi:
        wifi_businesses.append({
            'business_id': business_id,
            'business_ref': business_id.replace('businessid_', 'businessref_'),
            'name': name,
            'state': state,
            'wifi_value': str(attributes.get('WiFi', ''))
        })

print('Found', len(wifi_businesses), 'WiFi businesses')

# Count by state
state_counts = {}
for biz in wifi_businesses:
    state = biz['state']
    state_counts[state] = state_counts.get(state, 0) + 1

# Find top state
top_state = max(state_counts, key=state_counts.get) if state_counts else None
top_count = state_counts.get(top_state, 0) if top_state else 0

print('Top state:', top_state, 'with', top_count, 'WiFi businesses')
print('State counts (top 10):')
sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
for state, count in sorted_states[:10]:
    print(f'  {state}: {count}')

result = {
    'total_wifi_businesses': len(wifi_businesses),
    'wifi_businesses': wifi_businesses,
    'state_counts': state_counts,
    'top_state': top_state,
    'top_state_count': top_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}, 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'test': 'success', 'file_key': 'var_functions.query_db:2'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'review_id': 'reviewid_135', 'business_ref': 'businessref_34', 'rating': '2'}, {'review_id': 'reviewid_1067', 'business_ref': 'businessref_89', 'rating': '5'}, {'review_id': 'reviewid_871', 'business_ref': 'businessref_82', 'rating': '4'}, {'review_id': 'reviewid_314', 'business_ref': 'businessref_66', 'rating': '2'}, {'review_id': 'reviewid_487', 'business_ref': 'businessref_95', 'rating': '1'}, {'review_id': 'reviewid_1031', 'business_ref': 'businessref_24', 'rating': '4'}, {'review_id': 'reviewid_441', 'business_ref': 'businessref_40', 'rating': '4'}, {'review_id': 'reviewid_40', 'business_ref': 'businessref_47', 'rating': '5'}, {'review_id': 'reviewid_1807', 'business_ref': 'businessref_16', 'rating': '3'}, {'review_id': 'reviewid_1741', 'business_ref': 'businessref_96', 'rating': '5'}]}

exec(code, env_args)
