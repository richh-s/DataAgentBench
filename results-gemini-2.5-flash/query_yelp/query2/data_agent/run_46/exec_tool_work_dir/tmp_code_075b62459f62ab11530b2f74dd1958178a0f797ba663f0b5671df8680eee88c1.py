code = """import pandas as pd
import re
import json

# Access the raw string output which is the first element in the 'results' list
raw_tool_output = locals()['var_function-call-10195001444016038111']['results'][0]

# The raw_tool_output contains extra newline characters and the string 'The result is:\n', so extract just the JSON array.
# Using a regex to find the actual JSON array string which starts with '[' and ends with ']'
match = re.search(r'\[.*?\]', raw_tool_output, re.DOTALL)

if match:
    json_array_str = match.group(0)
    parsed_business_data = json.loads(json_array_str)
    df_business = pd.DataFrame(parsed_business_data)
else:
    # If no JSON array is found, create an empty DataFrame
    df_business = pd.DataFrame()

# Function to extract state from description
def extract_state(description):
    if description:
        # Regex to find two uppercase letters (state) following a comma and a space,
        # and then either another comma, a period, or end of string.
        # This covers cases like ", CA," or ", CA." or ", CA" at the end of the string.
        match = re.search(r', ([A-Z]{2})(?:,|$|\.)', description)
        if match:
            return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)
# Convert review_count to numeric, coercing errors to NaN
df_business['review_count'] = pd.to_numeric(df_business['review_count'], errors='coerce')

# Drop rows where state is None or review_count is NaN, as these cannot be used for the calculation
df_business.dropna(subset=['state', 'review_count'], inplace=True)

if not df_business.empty:
    state_review_counts = df_business.groupby('state')['review_count'].sum().reset_index()
    # Find the state with the highest review count
    highest_review_state_df = state_review_counts.loc[state_review_counts['review_count'].idxmax()]

    highest_review_state_name = highest_review_state_df['state']

    # Get all business_ids for businesses in the highest review count state
    business_ids_in_state = df_business[df_business['state'] == highest_review_state_name]['business_id'].tolist()

    # Convert business_id (e.g., 'businessid_1') to business_ref (e.g., 'businessref_1') format
    business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids_in_state]

    print("__RESULT__:")
    print(json.dumps({
        'highest_review_state_name': highest_review_state_name,
        'business_refs': business_refs
    }))
else:
    print("__RESULT__:")
    print(json.dumps({'highest_review_state_name': None, 'business_refs': []}))"""

env_args = {'var_function-call-10195001444016038111': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
