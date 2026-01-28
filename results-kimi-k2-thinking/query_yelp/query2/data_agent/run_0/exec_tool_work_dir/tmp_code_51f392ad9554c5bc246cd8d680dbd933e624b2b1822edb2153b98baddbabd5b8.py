code = """import json
import re

# Read the business data from the file
business_file_path = var_functions.query_db:5
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

print(f"Loaded {len(businesses)} businesses")
print("Sample business:", businesses[0])

# Extract state information from descriptions
state_data = []
for biz in businesses:
    business_id = biz['business_id']
    review_count = int(biz['review_count'])
    description = biz['description']
    
    # Parse state from description
    # Looking for pattern like "CA," or "CA " or ", CA" or " in CA"
    state_patterns = [
        r',\s*([A-Z]{2})\b',  # comma followed by state code
        r'\bin\s+([A-Z]{2})\b',  # "in STATE"
        r'\bat\s+[^,]+,\s*([A-Z]{2})\b',  # "at address, STATE"
        r'\b([A-Z]{2})\b'  # any 2-letter uppercase combination
    ]
    
    state = None
    for pattern in state_patterns:
        match = re.search(pattern, description)
        if match:
            potential_state = match.group(1)
            # Validate it's likely a US state code (2 letters, uppercase)
            if len(potential_state) == 2 and potential_state.isupper():
                state = potential_state
                break
    
    if state:
        state_data.append({
            'business_id': business_id,
            'review_count': review_count,
            'state': state,
            'description': description
        })

print(f"Successfully extracted state for {len(state_data)} businesses")
if state_data:
    print("First few with states:", state_data[:3])

# Count total reviews per state
state_review_totals = {}
for item in state_data:
    state = item['state']
    review_count = item['review_count']
    state_review_totals[state] = state_review_totals.get(state, 0) + review_count

# Sort states by total reviews
sorted_states = sorted(state_review_totals.items(), key=lambda x: x[1], reverse=True)
print("Top states by review count:", sorted_states[:10])

# Find the top state
top_state = sorted_states[0][0]
top_state_reviews = sorted_states[0][1]

print(f"Top state: {top_state} with {top_state_reviews} reviews")

# Prepare result for next steps
result = {
    'top_state': top_state,
    'top_state_reviews': top_state_reviews,
    'businesses_in_top_state': [biz['business_id'] for biz in state_data if biz['state'] == top_state],
    'all_states_data': state_data
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
