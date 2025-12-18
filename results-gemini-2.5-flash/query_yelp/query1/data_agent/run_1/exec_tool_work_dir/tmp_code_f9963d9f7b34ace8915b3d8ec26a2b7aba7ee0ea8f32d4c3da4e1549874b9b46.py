code = """import json
import pandas as pd

raw_output_string = locals()['var_function-call-6366228430567125078']['query_db_response']['results'][0]

# Find the start and end of the JSON array within the string output
start_marker = 'The result is:\n'
json_start_index = raw_output_string.find(start_marker) + len(start_marker)

# The JSON array ends right before the final newline character
json_end_index = raw_output_string.rfind('\n')

# Extract the JSON string
json_array_str = raw_output_string[json_start_index:json_end_index].strip()

business_data = json.loads(json_array_str)
business_df = pd.DataFrame(business_data)

indianapolis_businesses = business_df[
    business_df['description'].str.contains('Indianapolis, Indiana', na=False)
]

business_ids = indianapolis_businesses['business_id'].tolist()
formatted_business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]

print('__RESULT__:')
print(json.dumps(formatted_business_refs))"""

env_args = {'var_function-call-15356663371053430150': [], 'var_function-call-6366228430567125078': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
