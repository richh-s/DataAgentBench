code = """import json

businesses_data_str = locals()['var_function-call-8276028613370821812']['results'][0]
# The actual JSON data is inside the string 'The result is:
[...]' within businesses_data_str
# Extract the JSON part and load it
start_index = businesses_data_str.find('\n[')
end_index = businesses_data_str.rfind(']\n') + 1
json_string = businesses_data_str[start_index:end_index]

businesses_data = json.loads(json_string)

indianapolis_business_ids = []
for business in businesses_data:
    description = business.get('description', '')
    # Note: The original query was 'Indianapolis, Indiana', but the sample data shows 'Indianapolis, IN'
    # I'm using 'Indianapolis, IN' for consistency with observed data patterns in the preview.
    if 'Indianapolis, IN' in description:
        # The business_id in businessinfo_database has a prefix 'businessid_'
        # The business_ref in user_database has a prefix 'businessref_'
        # We need to transform the business_id to business_ref format
        business_id_raw = business['business_id'].replace('businessid_', '')
        indianapolis_business_ids.append(f'businessref_{business_id_raw}')

print('__RESULT__:')
print(json.dumps(indianapolis_business_ids))"""

env_args = {'var_function-call-2849685606806434320': [], 'var_function-call-8276028613370821812': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
