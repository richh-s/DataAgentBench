code = """import json
import re

business_data_raw_list = locals()['var_function-call-6525012195930113835']['query_db_response']['results']
# The actual JSON string is the first element of the list
full_string = business_data_raw_list[0]

# Find the starting and ending index of the actual JSON array
json_start_index = full_string.find('[')
json_end_index = full_string.rfind(']') + 1

# Extract the JSON string part
json_part_str = full_string[json_start_index:json_end_index]

business_data = json.loads(json_part_str)

extracted_business_info = []
for business in business_data:
    description = business.get('description', '')
    # Regex to find a two-letter US state abbreviation
    # It looks for two uppercase letters preceded by a space or comma, and followed by a space, comma, or end of string
    state_match = re.search(r'(?:, |\s)([A-Z]{2})(?:, |\s|$)', description)
    state = state_match.group(1) if state_match else None
    if state:
        # Convert business_id to match business_ref format for joining later
        business_ref = business['business_id'].replace('businessid_', 'businessref_')
        extracted_business_info.append({
            'business_ref': business_ref,
            'state': state,
            'review_count': int(business.get('review_count', 0))
        })

print('__RESULT__:')
print(json.dumps(extracted_business_info))"""

env_args = {'var_function-call-6525012195930113835': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
