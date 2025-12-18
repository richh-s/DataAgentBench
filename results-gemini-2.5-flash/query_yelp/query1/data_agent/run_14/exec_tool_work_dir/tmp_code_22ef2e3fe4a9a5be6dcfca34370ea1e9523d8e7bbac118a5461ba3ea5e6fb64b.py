code = """import json
import re

business_data_raw = locals()['var_function-call-8462912149142187824']

all_businesses = []
indy_businesses_ref_ids = []

# Safely access the results string
if 'query_db_response' in business_data_raw and \
   'results' in business_data_raw['query_db_response'] and \
   isinstance(business_data_raw['query_db_response']['results'], list) and \
   len(business_data_raw['query_db_response']['results']) > 0:

    results_string = business_data_raw['query_db_response']['results'][0]

    # Use regex to extract the JSON array part from the string
    match = re.search(r'\[.*?\]', results_string, re.DOTALL)

    if match:
        json_part = match.group(0)
        try:
            all_businesses = json.loads(json_part)
        except json.JSONDecodeError as e:
            # If JSON decoding fails, print an error and stop
            print("__RESULT__:")
            print(json.dumps({"error": f"Failed to decode JSON from extracted part: {e}"}))
            exit() # Exit to prevent further execution and multiple prints
    else:
        # If no JSON array is found, print an error and stop
        print("__RESULT__:")
        print(json.dumps({"error": "No JSON array found in the results string from query_db."}))
        exit() # Exit to prevent further execution and multiple prints
else:
    # If the expected structure is not found, print an error and stop
    print("__RESULT__:")
    print(json.dumps({"error": "Unexpected structure in business_data_raw."}))
    exit() # Exit to prevent further execution and multiple prints


# Filter businesses for Indianapolis and collect business_ref_ids
for business in all_businesses:
    if "description" in business and business["description"] is not None and \
       "business_id" in business and business["business_id"] is not None:
        description_lower = business["description"].lower()
        if "indianapolis, in" in description_lower or "indianapolis, indiana" in description_lower:
            indy_businesses_ref_ids.append(business["business_id"].replace("businessid_", "businessref_"))

# Finally, print the collected business_ref_ids
print("__RESULT__:")
print(json.dumps(indy_businesses_ref_ids))"""

env_args = {'var_function-call-5889703767481509966': [], 'var_function-call-8462912149142187824': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
