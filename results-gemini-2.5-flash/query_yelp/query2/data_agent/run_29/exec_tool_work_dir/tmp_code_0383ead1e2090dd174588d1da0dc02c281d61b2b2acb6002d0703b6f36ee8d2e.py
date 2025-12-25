code = """import pandas as pd
import re
import json

# Access the raw dictionary output from the previous tool call
raw_output_dict = locals()['var_function-call-10334109790306661588']

# Access the list of result strings which is nested within 'query_db_response' and then 'results' list
business_data_raw_string_with_metadata = raw_output_dict['query_db_response']['results'][0]

# Extract the JSON array string from the full raw string using regex
json_match = re.search(r'\[.+\]', business_data_raw_string_with_metadata, re.DOTALL)
if json_match:
    business_data_json_string = json_match.group(0)
else:
    raise ValueError("Could not extract JSON data from businessinfo_database query result string.")

business_data = json.loads(business_data_json_string)

df_business = pd.DataFrame(business_data)

# Convert review_count to integer
df_business['review_count'] = df_business['review_count'].astype(int)

# Extract state from description. Assuming state abbreviation is always preceded by ', ' and followed by ' in ' or end of string.
def extract_state(description):
    match = re.search(r', ([A-Z]{2})(?: in |$)', description)
    return match.group(1) if match else None

df_business['state'] = df_business['description'].apply(extract_state)

# Filter out businesses where state could not be extracted
df_business = df_business.dropna(subset=['state'])

# Aggregate review_count by state
state_review_counts = df_business.groupby('state')['review_count'].sum().reset_index()

# Get the state with the highest review count
highest_review_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
state_name = highest_review_state['state']

# Filter businesses for the highest review state
businesses_in_highest_state = df_business[df_business['state'] == state_name]
business_ids = businesses_in_highest_state['business_id'].tolist()

# The business_id in business collection is like "businessid_XXX", but in review table it's "businessref_XXX".
# So, we need to convert business_id to business_ref format.
business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]

print('__RESULT__:')
print(json.dumps({'state_name': state_name, 'business_refs': business_refs}))"""

env_args = {'var_function-call-10149927896045571199': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-10334109790306661588': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
