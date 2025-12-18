code = """import json

businesses_data = locals()['var_function-call-8462912149142187824']['results']

indy_businesses = []
for business_entry in businesses_data:
    # Assuming business_entry is a list containing the actual business dictionary
    # Based on the previous output, business_entry is a string that needs to be parsed as JSON
    # It appears to be a list of strings, each string containing a JSON object.
    # Let's inspect the actual structure of 'business_entry' if it's a string
    # If business_entry is a string representing a single JSON object, parse it.
    # If it's a list of JSON objects, then the original approach would be more direct.

    # From the example output, it seems `business_entry` is already a dictionary
    # if business_entry is a dict, it will contain '_id', 'business_id', 'description'
    if isinstance(business_entry, dict):
        business = business_entry # No need to parse if already a dict
    else:
        # If it's a string, try to parse it as JSON
        try:
            business = json.loads(business_entry)
        except json.JSONDecodeError:
            # If parsing fails, skip or handle error appropriately
            continue # Skip this entry if it's not valid JSON

    if "description" in business and business["description"] is not None:
        description_lower = business["description"].lower()
        if "indianapolis" in description_lower and "indiana" in description_lower:
            indy_businesses.append(business["business_id"].replace("businessid_", "businessref_"))

print("__RESULT__:")
print(json.dumps(indy_businesses))"""

env_args = {'var_function-call-5889703767481509966': [], 'var_function-call-8462912149142187824': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
