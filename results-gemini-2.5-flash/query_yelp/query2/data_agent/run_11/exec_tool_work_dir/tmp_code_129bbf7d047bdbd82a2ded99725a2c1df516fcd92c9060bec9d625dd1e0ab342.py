code = """import json
import re

business_data = locals()['var_function-call-8038848346409518787']['results']

state_review_counts = {}
business_id_to_state = {}

for business in business_data:
    description = business.get('description', '')
    review_count = int(business.get('review_count', 0)) if business.get('review_count') else 0
    business_id = business.get('business_id')

    # Extract state abbreviation (e.g., CA, MO, ID, FL, IN) from the description
    match = re.search(r', ([A-Z]{2}),', description)
    if match:
        state = match.group(1)
        state_review_counts[state] = state_review_counts.get(state, 0) + review_count
        business_id_to_state[business_id] = state

if state_review_counts:
    highest_review_state = max(state_review_counts, key=state_review_counts.get)
    highest_review_count = state_review_counts[highest_review_state]
else:
    highest_review_state = None
    highest_review_count = 0

result = {
    'highest_review_state': highest_review_state,
    'highest_review_count': highest_review_count,
    'business_id_to_state': business_id_to_state
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-8038848346409518787': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
