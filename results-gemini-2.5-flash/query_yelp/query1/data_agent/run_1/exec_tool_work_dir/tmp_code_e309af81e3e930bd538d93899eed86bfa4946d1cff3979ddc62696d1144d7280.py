code = """import json
import pandas as pd

# The full string output from the previous tool call
full_output_string = locals()['var_function-call-6366228430567125078']['query_db_response']['results'][0]

# Find the starting and ending indices of the actual JSON array within the string.
# The JSON array itself starts with '[' and ends with ']'.
json_start = full_output_string.find('[')
json_end = full_output_string.rfind(']')

# Extract the JSON array string
json_array_str = full_output_string[json_start : json_end + 1]

# Load the JSON string into a Python list of dictionaries
business_data = json.loads(json_array_str)

# Create a Pandas DataFrame from the business data
business_df = pd.DataFrame(business_data)

# Filter for businesses located in 'Indianapolis, Indiana' based on their description
indianapolis_businesses = business_df[
    business_df['description'].str.contains('Indianapolis, Indiana', na=False)
]

# Extract business_id values and format them by replacing 'businessid_' with 'businessref_'
# This is done to match the format expected by the 'user_database' tables.
formatted_business_refs = [bid.replace('businessid_', 'businessref_') for bid in indianapolis_businesses['business_id'].tolist()]

# Print the list of formatted business_refs in JSON format
print('__RESULT__:')
print(json.dumps(formatted_business_refs))"""

env_args = {'var_function-call-15356663371053430150': [], 'var_function-call-6366228430567125078': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
