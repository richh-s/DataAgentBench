code = """import json
import re
import pandas as pd

# Access business data file path from storage
business_data_path = vars()['var_functions.query_db:22']

# Load the full business dataset
with open(business_data_path, 'r') as f:
    business_data = json.load(f)

# Convert to DataFrame
df_business = pd.DataFrame(business_data)

# Extract state from description
def extract_state(description):
    if pd.isna(description) or not description:
        return None
    
    # Look for pattern like "City, State" where State is 2-letter code
    match = re.search(r'in [^,]+, ([A-Z]{2})', str(description))
    if match:
        return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)

# Convert review_count to numeric
df_business['review_count'] = pd.to_numeric(df_business['review_count'], errors='coerce')

# Group by state and sum review counts
state_reviews = df_business.groupby('state')['review_count'].sum().reset_index()

# Filter out None/NaN states and sort
state_reviews = state_reviews.dropna(subset=['state'])
state_reviews = state_reviews.sort_values('review_count', ascending=False)

# Get the state with highest number of reviews
top_state_row = state_reviews.iloc[0]
top_state = top_state_row['state']
top_state_reviews = int(top_state_row['review_count'])

# Get all business_ids for the top state
top_state_businesses = df_business[df_business['state'] == top_state]['business_id'].tolist()

print('__RESULT__:')
print(json.dumps({
    "top_state": top_state,
    "total_reviews": top_state_reviews,
    "business_ids": top_state_businesses
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:14': {'top_state': 'MO', 'total_reviews': 81, 'state_reviews_summary': [{'state': 'MO', 'review_count': 81}, {'state': 'ID', 'review_count': 39}, {'state': 'IN', 'review_count': 28}, {'state': 'CA', 'review_count': 8}, {'state': 'FL', 'review_count': 5}]}, 'var_functions.execute_python:16': {'mo_business_refs': ['businessref_47']}, 'var_functions.list_db:18': ['review', 'tip', 'user'], 'var_functions.query_db:20': [{'avg_rating': '3.9047619047619047'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
