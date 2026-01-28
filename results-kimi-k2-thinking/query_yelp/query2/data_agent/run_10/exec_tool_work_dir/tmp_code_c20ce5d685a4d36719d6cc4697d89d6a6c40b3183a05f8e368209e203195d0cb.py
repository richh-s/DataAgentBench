code = """import json
import re

# Load all business data from file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Function to extract state from description
def extract_state(description):
    pattern = r'in [^,]+, ([A-Z]{2})[,.]'
    match = re.search(pattern, description, re.I)
    if match:
        return match.group(1).upper()
    return None

# Calculate total review counts by state
total_reviews_by_state = {}
business_state = {}

for rec in business_data:
    desc = rec.get('description', '')
    state = extract_state(desc)
    
    if state is None:
        # Skip businesses where we can't parse the state
        continue
    
    business_id = rec.get('business_id')
    review_count_str = rec.get('review_count', '0')
    
    # Store mapping: business_id -> state for later use
    business_state[business_id] = state
    
    # Add review count to state's total
    review_count = int(review_count_str) if review_count_str and review_count_str.isdigit() else 0
    
    if state not in total_reviews_by_state:
        total_reviews_by_state[state] = 0
    total_reviews_by_state[state] += review_count

# Find state with highest total reviews
if total_reviews_by_state:
    top_state = max(total_reviews_by_state, key=total_reviews_by_state.get)
    top_state_total_reviews = total_reviews_by_state[top_state]
else:
    top_state = None
    top_state_total_reviews = 0

# Count businesses in top state
businesses_in_top_state = []
if top_state:
    for business_id, state in business_state.items():
        if state == top_state:
            businesses_in_top_state.append(business_id)

result = {
    "top_state": top_state,
    "top_state_total_reviews": top_state_total_reviews,
    "total_businesses_in_top_state": len(businesses_in_top_state),
    "all_states_count": len(total_reviews_by_state),
    "top_10_states": dict(sorted(total_reviews_by_state.items(), key=lambda x: x[1], reverse=True)[:10])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'record_count': 100}, 'var_functions.execute_python:14': {'top_state': None, 'total_reviews_top_state': 0, 'businesses_in_top_state': 0, 'state_review_sums': {}}, 'var_functions.execute_python:16': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young lear...', 'found_state': 'CA'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, inc...', 'found_state': 'MO'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination...', 'found_state': 'ID'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of ser...', 'found_state': 'FL'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services inclu...', 'found_state': 'IN'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightfu...', 'found_state': 'FL'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of service...', 'found_state': 'PA'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nai...', 'found_state': 'MO'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Anti...', 'found_state': 'IN'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of service...', 'found_state': 'NJ'}]}

exec(code, env_args)
