code = """import pandas as pd
import json

# Access the full raw string output from the previous tool call
full_raw_output_string = locals()['var_function-call-14740977723505021157']

# Find the starting and ending brackets of the actual JSON array within the string
json_array_start = full_raw_output_string.find('[')
json_array_end = full_raw_output_string.rfind(']')

json_string_to_parse = "[]" # Default to empty list if parsing fails
if json_array_start != -1 and json_array_end != -1 and json_array_end > json_array_start:
    json_string_to_parse = full_raw_output_string[json_array_start : json_array_end + 1]

# Load the JSON string into a Python list of dictionaries
businesses = json.loads(json_string_to_parse)
df_businesses = pd.DataFrame(businesses)

# Extract state from description field
def extract_state(description):
    if description and ' in ' in description:
        # Split by ' in ' to get location part, then by ', ' to get state
        parts = description.split(' in ', 1)
        if len(parts) > 1:
            location_part = parts[1]
            city_state_zip = location_part.split(', ')
            if len(city_state_zip) > 1:
                state_zip = city_state_zip[1].strip().split(' ')
                if len(state_zip) > 0:
                    return state_zip[0]
    return None

df_businesses['state'] = df_businesses['description'].apply(extract_state)

# Convert 'review_count' to numeric, handling potential errors by coercing to NaN
df_businesses['review_count'] = pd.to_numeric(df_businesses['review_count'], errors='coerce')

# Filter for U.S. states (assuming 2-letter codes) and drop rows where state is None
df_businesses_filtered = df_businesses[df_businesses['state'].notna() & (df_businesses['state'].str.len() == 2)]

# Aggregate review counts by state to find the state with the highest number of reviews
state_review_counts = df_businesses_filtered.groupby('state')['review_count'].sum().reset_index()

# Get the state with the highest total review count
highest_state_name = None
highest_state_review_count = 0

if not state_review_counts.empty:
    highest_review_state_row = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
    highest_state_name = highest_review_state_row['state']
    highest_state_review_count = highest_review_state_row['review_count']

# Get all business_ids belonging to the identified highest review state
business_ids_in_highest_state = []
if highest_state_name:
    business_ids_in_highest_state = df_businesses_filtered[df_businesses_filtered['state'] == highest_state_name]['business_id'].tolist()

# Convert 'businessid_' format to 'businessref_' format for querying the user_database
business_refs_for_query = [bid.replace('businessid_', 'businessref_') for bid in business_ids_in_highest_state]

# Prepare the result for the next step
result_data = {
    'highest_state_name': highest_state_name,
    'highest_state_review_count': highest_state_review_count,
    'business_refs_for_query': business_refs_for_query
}

print("__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_function-call-13372583847267255680': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5200213296734229511': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14740977723505021157': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
