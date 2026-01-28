code = """import json
import re

# Load business data from file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Example: parse state from description
# Pattern: "... in City, XX, ..." or "... in City, XX" or "... in City, State, ..." where State is two letters.
state_pattern = re.compile(r'\b([A-Z]{2})\b')

business_state_map = {}  # business_id -> state
state_review_sum = {}    # state -> total review count

for rec in business_data:
    business_id = rec.get('business_id')
    review_count_str = rec.get('review_count', '0')
    description = rec.get('description', '')
    # Extract state abbreviation (two uppercase letters) from description
    # Usually after ' in ' and before ','.
    # We'll find all two-letter uppercase sequences and pick the likely state (first occurrence).
    states = state_pattern.findall(description)
    state = None
    if states:
        # The state appears usually after a city name and before a comma
        # Choose the first matched state.
        state = states[0]
    # If not found, skip this business
    if state is None:
        continue

    # Map
    business_state_map[business_id] = state
    # Convert review count to int
    try:
        review_count = int(review_count_str)
    except ValueError:
        review_count = 0
    # Add to state's total
    state_review_sum[state] = state_review_sum.get(state, 0) + review_count

# Determine state with highest total reviews
if state_review_sum:
    top_state = max(state_review_sum, key=state_review_sum.get)
    top_reviews = state_review_sum[top_state]
else:
    top_state = None
    top_reviews = 0

# Map numeric business IDs for top state
business_ids_top_state = [bid for bid, st in business_state_map.items() if st == top_state]
# Extract numeric part (after underscore) for those business IDs
business_numeric_ids_top = [bid.split('_')[1] for bid in business_ids_top_state]
# Count of distinct businesses in top state
distinct_business_count = len(business_numeric_ids_top)

result = {
    'top_state': top_state,
    'total_reviews_top_state': top_reviews,
    'businesses_in_top_state': distinct_business_count,
    'state_review_sums': state_review_sum
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'record_count': 100}}

exec(code, env_args)
