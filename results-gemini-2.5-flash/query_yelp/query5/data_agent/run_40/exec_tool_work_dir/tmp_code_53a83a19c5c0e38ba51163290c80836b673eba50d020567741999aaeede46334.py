code = """import re
import json

# Get the full string output from the query_db tool
full_output_string = locals()['var_function-call-16565482839893785034']['query_db_response']['results'][0]

# Find the JSON array part of the string using regex
json_array_match = re.search(r'\[.*?\]', full_output_string, re.DOTALL)

data = []
if json_array_match:
    json_array_str = json_array_match.group(0)
    data = json.loads(json_array_str)

business_states = {}
business_id_to_state = {}

for business in data:
    description = business.get('description', '')
    match = re.search(r',\s*([A-Z]{2})(?:\s|[A-Z])', description)
    if match:
        state = match.group(1)
        business_states[state] = business_states.get(state, 0) + 1
        business_id_to_state[business['business_id']] = state

if not business_states:
    highest_state = None
    filtered_business_ids = []
    business_count = 0
else:
    highest_state = max(business_states, key=business_states.get)
    filtered_business_ids = [k.replace('businessid_', 'businessref_') for k, v in business_id_to_state.items() if v == highest_state]
    business_count = business_states[highest_state]

result = {
    'highest_state': highest_state,
    'filtered_business_ids': filtered_business_ids,
    'business_count': business_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16565482839893785034': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
