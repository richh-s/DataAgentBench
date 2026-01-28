code = """import re
import json

# Read the file with WiFi businesses
key = 'var_functions.query_db:14'
file_path = locals()[key]

# Load JSON data from the file
with open(file_path, 'r') as f:
    wifi_businesses = json.load(f)

print(f"Total WiFi businesses loaded: {len(wifi_businesses)}")

# US state postal abbreviations
us_states = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
}

# Function to extract state from description
def extract_state(description):
    if not description:
        return None
    
    # Look for patterns that match state codes
    patterns = [
        r'in [^,]+, ([A-Z]{2})[ ,]',  # "in City, CA" or "in City, CA "
        r'([A-Z]{2}), [0-9]',  # "CA 12345"
        r'located at [^,]+, ([A-Z]{2})[ ,]',  # "located at 123 Main St, CA"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            state = match.group(1).upper()
            if state in us_states:
                return state
    
    return None

# Process businesses
wifi_business_info = []
wifi_business_ids = []

for business in wifi_businesses:
    # Check if WiFi attribute exists and is not "u'no'"
    has_wifi = False
    if business.get('attributes') and business['attributes'] != 'None':
        if isinstance(business['attributes'], dict):
            wifi_value = business['attributes'].get('WiFi')
            if wifi_value and wifi_value != "u'no'" and str(wifi_value).lower() != "'no'":
                has_wifi = True
    
    if has_wifi:
        description = business.get('description', '')
        state = extract_state(description)
        if state:
            business_id = business['business_id']
            wifi_business_info.append({
                'business_id': business_id,
                'state': state,
                'description': description
            })
            wifi_business_ids.append(business_id)

# Count businesses per state
from collections import Counter
state_counts = Counter([b['state'] for b in wifi_business_info])

print(f"WiFi businesses with valid US state: {len(wifi_business_info)}")
print(f"State counts: {dict(state_counts)}")

# Find top state
top_state, top_count = state_counts.most_common(1)[0]

print(f"Top state: {top_state} with {top_count} businesses")

# Get business IDs for top state
top_state_business_ids = [b['business_id'] for b in wifi_business_info if b['state'] == top_state]

result = {
    'wifi_businesses_count': len(wifi_business_info),
    'state_counts': dict(state_counts),
    'top_state': top_state,
    'top_state_count': top_count,
    'top_state_business_ids': top_state_business_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}, 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'review_id': 'reviewid_135', 'business_ref': 'businessref_34', 'rating': '2'}, {'review_id': 'reviewid_1067', 'business_ref': 'businessref_89', 'rating': '5'}, {'review_id': 'reviewid_871', 'business_ref': 'businessref_82', 'rating': '4'}, {'review_id': 'reviewid_314', 'business_ref': 'businessref_66', 'rating': '2'}, {'review_id': 'reviewid_487', 'business_ref': 'businessref_95', 'rating': '1'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'wifi_businesses': [{'business_id': 'businessid_64', 'state': 'MO'}, {'business_id': 'businessid_54', 'state': 'FL'}, {'business_id': 'businessid_91', 'state': 'LA'}, {'business_id': 'businessid_93', 'state': 'IL'}, {'business_id': 'businessid_26', 'state': 'FL'}, {'business_id': 'businessid_89', 'state': 'PA'}, {'business_id': 'businessid_97', 'state': 'PA'}, {'business_id': 'businessid_67', 'state': 'PA'}, {'business_id': 'businessid_51', 'state': 'FL'}, {'business_id': 'businessid_5', 'state': 'AB'}, {'business_id': 'businessid_6', 'state': 'NV'}, {'business_id': 'businessid_55', 'state': 'FL'}, {'business_id': 'businessid_77', 'state': 'PA'}, {'business_id': 'businessid_86', 'state': 'PA'}, {'business_id': 'businessid_40', 'state': 'PA'}, {'business_id': 'businessid_44', 'state': 'PA'}, {'business_id': 'businessid_43', 'state': 'IN'}, {'business_id': 'businessid_20', 'state': 'FL'}, {'business_id': 'businessid_85', 'state': 'PA'}, {'business_id': 'businessid_25', 'state': 'ID'}, {'business_id': 'businessid_82', 'state': 'PA'}, {'business_id': 'businessid_12', 'state': 'AB'}, {'business_id': 'businessid_16', 'state': 'IN'}, {'business_id': 'businessid_46', 'state': 'MO'}], 'state_counts': {'MO': 2, 'FL': 5, 'LA': 1, 'IL': 1, 'PA': 9, 'AB': 2, 'NV': 1, 'IN': 2, 'ID': 1}, 'top_state': 'PA', 'top_state_count': 9}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
