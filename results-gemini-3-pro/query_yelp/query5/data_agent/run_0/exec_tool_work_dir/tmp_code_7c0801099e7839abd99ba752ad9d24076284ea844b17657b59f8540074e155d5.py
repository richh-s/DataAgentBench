code = """import json
import re

# Load data
file_path = locals()['var_function-call-10126645596588229308']
with open(file_path, 'r') as f:
    data = json.load(f)

# US States set
us_states = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
    'DC'
}

state_counts = {}
business_ids_by_state = {}
state_pattern = re.compile(r" ([A-Z]{2}), this")

count_processed = 0
for entry in data:
    attrs = entry.get('attributes', {})
    if not attrs: continue
    
    wifi = str(attrs.get('WiFi', '')).lower()
    
    # Check for 'free' or 'paid'
    # Values seen: "u'free'", "'free'", "u'paid'", "paid"
    # "u'no'", "'no'", "none", "no"
    if 'free' in wifi or 'paid' in wifi:
        desc = entry.get('description', '')
        match = state_pattern.search(desc)
        if match:
            state = match.group(1)
            if state in us_states:
                if state not in state_counts:
                    state_counts[state] = 0
                    business_ids_by_state[state] = []
                state_counts[state] += 1
                business_ids_by_state[state].append(entry['business_id'])

if not state_counts:
    print("__RESULT__:")
    print(json.dumps({"error": "No US businesses with WiFi found"}))
else:
    top_state = max(state_counts, key=state_counts.get)
    top_count = state_counts[top_state]
    target_ids = business_ids_by_state[top_state]
    
    # Convert business_ids to business_refs
    # businessid_X -> businessref_X
    target_refs = [bid.replace("businessid_", "businessref_") for bid in target_ids]
    
    result = {
        "top_state": top_state,
        "count": top_count,
        "business_refs": target_refs
    }
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-10915411876622360088': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-13757257449374681728': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-3215486988020379641': {'top_state': 'MO', 'count': 1, 'business_ids': ['businessid_64']}, 'var_function-call-10105073347575528229': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67'}, {'_id': '6859a000fe8b31cd7362e2d5', 'business_id': 'businessid_7'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51'}, {'_id': '6859a000fe8b31cd7362e2d9', 'business_id': 'businessid_5'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36'}], 'var_function-call-10126645596588229308': 'file_storage/function-call-10126645596588229308.json'}

exec(code, env_args)
