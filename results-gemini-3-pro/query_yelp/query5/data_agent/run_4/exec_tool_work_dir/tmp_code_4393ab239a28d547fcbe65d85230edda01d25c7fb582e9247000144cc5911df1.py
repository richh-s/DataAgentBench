code = """import re
import json

data = locals()['var_function-call-3014868214744279977']

# If data is a string (file path), load it.
if isinstance(data, str):
    with open(data, 'r') as f:
        data = json.load(f)

wifi_businesses = []
state_counts = {}
businesses_by_state = {}

# Regex to capture state: " in City Name, ST," or " in City Name, ST "
# The description format: "Located at ... in City, ST, ..."
state_pattern = re.compile(r" in [^,]+, ([A-Z]{2})")

for entry in data:
    wifi_val = entry.get('attributes', {}).get('WiFi', 'no')
    
    # Normalize wifi_val
    # It seems to be a string repr of a python string, e.g. "u'free'"
    # We treat it as offering WiFi if it contains 'free' or 'paid'
    if wifi_val and ('free' in wifi_val.lower() or 'paid' in wifi_val.lower()):
        desc = entry.get('description', '')
        match = state_pattern.search(desc)
        if match:
            state = match.group(1)
            # Filter out false positives if any (US states are 2 uppercase letters)
            # The regex ensures 2 uppercase letters.
            
            if state not in state_counts:
                state_counts[state] = 0
                businesses_by_state[state] = []
            
            state_counts[state] += 1
            businesses_by_state[state].append(entry['business_id'])

# Find state with max businesses
if state_counts:
    top_state = max(state_counts, key=state_counts.get)
    count = state_counts[top_state]
    target_ids = businesses_by_state[top_state]
else:
    top_state = None
    count = 0
    target_ids = []

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state,
    "business_count": count,
    "business_ids": target_ids
}))"""

env_args = {'var_function-call-9757262322190042123': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3014868214744279977': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
