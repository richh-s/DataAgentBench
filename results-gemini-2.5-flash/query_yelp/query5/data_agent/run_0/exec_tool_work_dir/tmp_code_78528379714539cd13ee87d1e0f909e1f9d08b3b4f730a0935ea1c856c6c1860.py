code = """import re
import json

# Directly access the dictionary output from the previous tool call.
# This dictionary has keys like 'query_db_response'.
output_from_query_db = locals()['var_function-call-16548434304143759753']

# The relevant data is nested under 'query_db_response' and then 'results'.
# The 'results' field is a list, and the actual JSON data we need is the first element,
# which is a string containing the JSON array along with some descriptive text.
raw_json_string_with_noise = output_from_query_db['query_db_response']['results'][0]

# Extract the pure JSON array string using regular expression.
# We're looking for content that starts with '[' and ends with ']',
# spanning multiple lines if necessary (re.DOTALL flag).
# This regex is robust to leading/trailing text.
match = re.search(r'\[.*\]', raw_json_string_with_noise, re.DOTALL)

clean_json_array_str = "[]" # Default to an empty JSON array string if no match is found
if match:
    clean_json_array_str = match.group(0)

# Parse the extracted JSON array string into a Python list of dictionaries
businesses_with_wifi = json.loads(clean_json_array_str)

state_counts = {}
business_ids_by_state = {}

for business in businesses_with_wifi:
    description = business.get('description', '')
    # Use regex to find a two-letter U.S. state abbreviation (e.g., CA, NY, FL).
    # It looks for a comma, optional space, then two uppercase letters for the state,
    # followed by a space, period, comma, or end of the string.
    state_match = re.search(r',\s*([A-Z]{2})(?:\s|\.|,|$)', description)
    if state_match:
        state = state_match.group(1)
        if state in state_counts:
            state_counts[state] += 1
            business_ids_by_state[state].append(business['business_id'])
        else:
            state_counts[state] = 1
            business_ids_by_state[state] = [business['business_id']]

most_common_state = None
if state_counts:
    most_common_state = max(state_counts, key=state_counts.get)

result_data = {
    "most_common_state": most_common_state,
    "business_ids_in_state": business_ids_by_state.get(most_common_state, []) if most_common_state else []
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_function-call-16548434304143759753': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
