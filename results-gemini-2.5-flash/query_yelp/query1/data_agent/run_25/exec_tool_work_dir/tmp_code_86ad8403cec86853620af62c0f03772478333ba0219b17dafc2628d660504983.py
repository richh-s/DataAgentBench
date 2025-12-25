code = """import json

businesses_data = locals()['var_function-call-13212411698338802671']['results']
indianapolis_business_ids = []

for business in businesses_data:
    if "description" in business and "Indianapolis, IN" in business["description"]:
        indianapolis_business_ids.append(business["business_id"])
    elif "description" in business and "Indianapolis, Indiana" in business["description"]:
        indianapolis_business_ids.append(business["business_id"])

# The business_id in MongoDB is like 'businessid_123'
# The business_ref in DuckDB is like 'businessref_123'
# We need to transform the ids for the next query
transformed_business_ids = [bid.replace("businessid_", "businessref_") for bid in indianapolis_business_ids]

print("__RESULT__:")
print(json.dumps(transformed_business_ids))"""

env_args = {'var_function-call-10520674423080167209': [], 'var_function-call-13212411698338802671': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
