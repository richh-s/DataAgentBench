code = """import json
import re

# Correctly access the results list from the storage
raw_db_output_list = locals()['var_function-call-8038848346409518787']['query_db_response']['results']

business_data = []

if raw_db_output_list and isinstance(raw_db_output_list[0], str):
    full_output_string = raw_db_output_list[0]

    # The actual JSON array is embedded in a larger string. Extract it.
    match = re.search(r'\[\{.*\}\]', full_output_string, re.DOTALL)
    if match:
        json_array_str = match.group(0)
        try:
            business_data = json.loads(json_array_str)
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e} for extracted string part: {json_array_str[:200]}")
    else:
        print("No JSON array found in the raw output string.")
else:
    print("Raw DB output is not in the expected format.")

state_review_counts = {}
business_id_to_state = {}

for business in business_data:
    description = business.get('description', '')
    review_count_str = business.get('review_count', '0')
    review_count = int(review_count_str) if isinstance(review_count_str, str) and review_count_str.isdigit() else 0
    business_id = business.get('business_id')

    match = re.search(r', ([A-Z]{2}),', description)
    if match:
        state = match.group(1)
        state_review_counts[state] = state_review_counts.get(state, 0) + review_count
        business_id_to_state[business_id] = state

highest_review_state = None
highest_review_count = 0

if state_review_counts:
    highest_review_state = max(state_review_counts, key=state_review_counts.get)
    highest_review_count = state_review_counts[highest_review_state]

business_refs_in_highest_review_state = []
for business_id, state in business_id_to_state.items():
    if state == highest_review_state:
        business_refs_in_highest_review_state.append(business_id.replace("businessid_", "businessref_"))

result = {
    'highest_review_state': highest_review_state,
    'highest_review_count': highest_review_count,
    'business_refs_in_highest_review_state': business_refs_in_highest_review_state
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-8038848346409518787': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
