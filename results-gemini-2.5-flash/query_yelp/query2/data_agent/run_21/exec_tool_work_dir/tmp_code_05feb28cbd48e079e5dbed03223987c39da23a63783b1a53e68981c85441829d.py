code = """import re
import pandas as pd
import json

business_data_raw_string = locals()['var_function-call-9819834313453833337']['query_db_response']['results'][0]

# The actual JSON array is embedded within a string that also contains metadata.
# We need to extract the JSON array part specifically.
# The JSON array starts after "The result is:\n" and ends before the final "\n".
# We can find the start of the JSON array by searching for '[' after the metadata.
# And the end by searching for ']' at the very end of the meaningful data.

json_start_indicator = "The result is:\n"
start_index = business_data_raw_string.find(json_start_indicator)

if start_index == -1:
    raise ValueError("Could not find the start indicator for JSON data.")

# Adjust start_index to point to the beginning of the actual JSON array
start_index += len(json_start_indicator)
json_part_raw = business_data_raw_string[start_index:].strip()

# The actual JSON string is usually the first part up to the last ']' character if there are extra newlines or text afterwards.
end_index = json_part_raw.rfind(']')
if end_index == -1:
    raise ValueError("Could not find the end of the JSON array.")

json_str = json_part_raw[:end_index + 1]

business_data = json.loads(json_str)

df_business = pd.DataFrame(business_data)

def extract_state(description):
    match = re.search(r', ([A-Z]{2}),', description)
    if match:
        return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['review_count'] = pd.to_numeric(df_business['review_count'], errors='coerce')

df_business_filtered = df_business.dropna(subset=['state', 'review_count'])

state_review_counts = df_business_filtered.groupby('state')['review_count'].sum().reset_index()

state_name = None
total_reviews_in_state = 0
business_refs_in_state = []

if not state_review_counts.empty:
    highest_review_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
    state_name = highest_review_state['state']
    total_reviews_in_state = highest_review_state['review_count']

    business_ids_in_state = df_business_filtered[df_business_filtered['state'] == state_name]['business_id'].tolist()
    business_refs_in_state = [bid.replace('businessid_', 'businessref_') for bid in business_ids_in_state]

print("__RESULT__:")
print(pd.Series({
    'state_name': state_name,
    'total_reviews_in_state': total_reviews_in_state,
    'business_refs_in_state': business_refs_in_state
}).to_json())"""

env_args = {'var_function-call-6535560299319635028': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9819834313453833337': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
