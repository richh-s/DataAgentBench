code = """import json
import re

# Load business data
with open(locals()['var_functions.query_db:16'], 'r') as f:
    business_data = json.load(f)

# Load review data  
with open(locals()['var_functions.query_db:12'], 'r') as f:
    review_data = json.load(f)

# Extract state from description (pattern: "in City, State" where State is 2-letter code)
def extract_state(description):
    if not description:
        return None
    match = re.search(r'in [^,]+, ([A-Z]{2})', description)
    if match:
        return match.group(1)
    return None

# Process businesses
businesses_by_id = {}
state_review_counts = {}
state_ratings = {}

for business in business_data:
    business_id = business['business_id']
    review_count = int(business['review_count'])
    state = extract_state(business['description'])
    
    if state:
        businesses_by_id[business_id] = {
            'state': state,
            'review_count': review_count
        }
        state_review_counts[state] = state_review_counts.get(state, 0) + review_count
        state_ratings[state] = []

# Map reviews to state (business_id to business_ref mapping needed)
# business_id: "businessid_49" corresponds to business_ref: "businessref_49"
for review in review_data:
    business_ref = review['business_ref']
    rating = int(review['rating'])
    
    # Convert business_ref to business_id format
    business_id = 'business' + business_ref[8:]  # businessref_X -> businessid_X
    
    if business_id in businesses_by_id:
        state = businesses_by_id[business_id]['state']
        state_ratings[state].append(rating)

# Calculate average rating per state
state_avg_ratings = {}
for state, ratings in state_ratings.items():
    if ratings:
        state_avg_ratings[state] = sum(ratings) / len(ratings)
    else:
        state_avg_ratings[state] = 0

# Find state with highest number of reviews
max_state = None
max_reviews = 0
for state, total_reviews in state_review_counts.items():
    if total_reviews > max_reviews:
        max_reviews = total_reviews
        max_state = state

print('__RESULT__:')
print(json.dumps({
    'state': max_state,
    'total_reviews': max_reviews,
    'avg_rating': round(state_avg_ratings[max_state], 2) if max_state else None
}))"""

env_args = {'var_functions.query_db:0': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:12': [{'business_id': 'businessid_49', 'review_count': 8, 'state': 'CA'}, {'business_id': 'businessid_47', 'review_count': 81, 'state': 'MO'}, {'business_id': 'businessid_88', 'review_count': 39, 'state': 'ID'}, {'business_id': 'businessid_41', 'review_count': 5, 'state': 'FL'}, {'business_id': 'businessid_33', 'review_count': 28, 'state': 'IN'}], 'var_functions.query_db:14': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
