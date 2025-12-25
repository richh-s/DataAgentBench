code = """import json
import re
import pandas as pd

# Load business data
businesses = locals()['var_function-call-5300744252068254687']

# Load review data
with open(locals()['var_function-call-9204549464474788302'], 'r') as f:
    reviews = json.load(f)

# Helper to check WiFi
def has_wifi(attrs):
    if not attrs or attrs == 'None':
        return False
    # attrs is a dict or string 'None' (but we handled 'None')
    # Wait, in the preview it showed "attributes": "None" (string) and "attributes": {...} (dict)
    # The tool output showed "attributes": "None" for one case.
    if isinstance(attrs, str):
        # If it's a string that is not "None", it might be malformed or something else. 
        # But based on preview, "None" means null.
        return False
    
    wifi = attrs.get('WiFi')
    if not wifi:
        return False
    
    # wifi is a string like "u'no'", "u'free'", "'free'", "None"
    wifi_lower = wifi.lower()
    if 'free' in wifi_lower or 'paid' in wifi_lower:
        return True
    return False

# Helper to extract state
def get_state(desc):
    # Pattern: " in City, ST, this"
    # Regex look for ", [A-Z]{2}, this"
    match = re.search(r",\s([A-Z]{2}),\sthis", desc)
    if match:
        return match.group(1)
    return None

# Process businesses
# We need to map business_id to state, ONLY for wifi businesses
wifi_biz_state = {} # suffix -> state

for b in businesses:
    if has_wifi(b.get('attributes')):
        bid = b.get('business_id')
        # Extract suffix. id format: "businessid_X"
        if bid.startswith('businessid_'):
            suffix = bid.split('_')[1]
            state = get_state(b.get('description', ''))
            if state:
                wifi_biz_state[suffix] = state

# Count businesses per state
state_counts = {}
for suffix, state in wifi_biz_state.items():
    state_counts[state] = state_counts.get(state, 0) + 1

# Find top state
if not state_counts:
    print("__RESULT__:")
    print(json.dumps("No businesses with WiFi found"))
    exit()

top_state = max(state_counts, key=state_counts.get)
top_count = state_counts[top_state]

# Filter reviews for businesses in the top state
# We need to calculate average rating for these businesses
# First, group ratings by business
biz_ratings = {} # suffix -> [ratings]

for r in reviews:
    bref = r.get('business_ref')
    # format: "businessref_X"
    if bref and bref.startswith('businessref_'):
        suffix = bref.split('_')[1]
        
        # Only care if this business is in the top state and has wifi
        if suffix in wifi_biz_state and wifi_biz_state[suffix] == top_state:
            if suffix not in biz_ratings:
                biz_ratings[suffix] = []
            biz_ratings[suffix].append(float(r['rating']))

# Calculate average rating for each business, then average of that
avg_ratings = []
for suffix in biz_ratings:
    ratings = biz_ratings[suffix]
    if ratings:
        avg_ratings.append(sum(ratings) / len(ratings))

final_avg_rating = 0
if avg_ratings:
    final_avg_rating = sum(avg_ratings) / len(avg_ratings)

result = {
    "top_state": top_state,
    "business_count": top_count,
    "average_rating": final_avg_rating
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1384464540767786372': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5300744252068254687': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9204549464474788302': 'file_storage/function-call-9204549464474788302.json'}

exec(code, env_args)
