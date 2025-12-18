code = """import json
import re

businesses_query_result = locals()['var_function-call-8462912149142187824']

# Based on the typical output format of query_db, the actual data is likely in the 'results' key
# of the dictionary returned for the tool call.
# The previous error indicated that the structure I was assuming was incorrect.
# Let's assume `businesses_query_result` is directly `{"results": [...]}`

all_businesses = []
if "results" in businesses_query_result and isinstance(businesses_query_result["results"], list):
    # The 'results' field from `query_db` for MongoDB returns a list where each element is a string. 
    # And this string contains the entire success message AND the JSON array.
    # So, we still need to parse that string to extract the JSON array.
    results_string_with_json = businesses_query_result["results"][0]

    # Use regex to extract the JSON array part from the string
    match = re.search(r'\[.*?\]', results_string_with_json, re.DOTALL)

    if match:
        json_part = match.group(0)
        try:
            all_businesses = json.loads(json_part)
        except json.JSONDecodeError as e:
            print("__RESULT__:")
            print(json.dumps({"error": f"Failed to decode JSON from extracted part: {e}"}))
            # Ensure list is empty if there was an error
            all_businesses = []
    else:
        print("__RESULT__:")
        print(json.dumps({"error": "No JSON array found in the results string from query_db."}))
        all_businesses = []
else:
    print("__RESULT__:")
    print(json.dumps({"error": "'results' key not found or not a list in businesses_query_result."}))
    all_businesses = []

indy_businesses_ref_ids = []
for business in all_businesses:
    if "description" in business and business["description"] is not None and \
       "business_id" in business and business["business_id"] is not None:
        description_lower = business["description"].lower()
        if "indianapolis, in" in description_lower or "indianapolis, indiana" in description_lower:
            indy_businesses_ref_ids.append(business["business_id"].replace("businessid_", "businessref_"))

print("__RESULT__:")
print(json.dumps(indy_businesses_ref_ids))"""

env_args = {'var_function-call-5889703767481509966': [], 'var_function-call-8462912149142187824': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
