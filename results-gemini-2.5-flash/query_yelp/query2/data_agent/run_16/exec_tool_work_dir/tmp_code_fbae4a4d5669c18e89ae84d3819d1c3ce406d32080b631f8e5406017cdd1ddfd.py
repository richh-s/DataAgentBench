code = """import pandas as pd
import json

raw_result_string = locals()['var_function-call-13372583847267255680']['query_db_response']['results'][0]

# Find the first occurrence of '[' and the last occurrence of ']' to extract the JSON array
json_start_index = raw_result_string.find('[')
json_end_index = raw_result_string.rfind(']')

json_string = "[]"
if json_start_index != -1 and json_end_index != -1 and json_end_index > json_start_index:
    json_string = raw_result_string[json_start_index : json_end_index + 1]

businesses = json.loads(json_string)
df_businesses = pd.DataFrame(businesses)

# Extract state from description
def extract_state(description):
    parts = description.split(' in ')
    if len(parts) > 1:
        city_state_zip = parts[1].split(', ')
        if len(city_state_zip) > 1:
            state_zip = city_state_zip[1].split(' ')
            if len(state_zip) > 0:
                return state_zip[0]
    return None

df_businesses['state'] = df_businesses['description'].apply(extract_state)
df_businesses['review_count'] = pd.to_numeric(df_businesses['review_count'])

# Filter for U.S. states only (assuming 2-letter codes) and drop None
df_businesses_filtered = df_businesses[df_businesses['state'].notna() & (df_businesses['state'].str.len() == 2)]

# Aggregate review counts by state
state_review_counts = df_businesses_filtered.groupby('state')['review_count'].sum().reset_index()

# Get the state with the highest number of reviews
if not state_review_counts.empty:
    highest_review_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
    highest_state_name = highest_review_state['state']
    highest_state_review_count = highest_review_state['review_count']
else:
    highest_state_name = None
    highest_state_review_count = 0

# Get business_ids for the highest review state
if highest_state_name:
    business_ids_in_highest_state = df_businesses_filtered[df_businesses_filtered['state'] == highest_state_name]['business_id'].tolist()
else:
    business_ids_in_highest_state = []

# Convert business_ids for querying user_database
business_refs_for_query = [f"'{bid.replace('businessid_', 'businessref_')}'" for bid in business_ids_in_highest_state]

print("__RESULT__:")
print(json.dumps({
    'highest_state_name': highest_state_name,
    'highest_state_review_count': highest_state_review_count,
    'business_refs_for_query': business_refs_for_query
}))"""

env_args = {'var_function-call-13372583847267255680': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
