code = """import json, pandas as pd

business_records = var_call_5NKdlimcB4x4Ygcg3xajowyv

biz_df = pd.DataFrame(business_records)

indianapolis_mask = biz_df['description'].str.contains('Indianapolis, IN', case=False, na=False) | biz_df['description'].str.contains('Indianapolis, Indiana', case=False, na=False)
indianapolis_biz = biz_df[indianapolis_mask].copy()

indianapolis_biz['business_ref'] = indianapolis_biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

result = indianapolis_biz['business_ref'].tolist()

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_X5k8cUcBjFj1obNxx7Z2btce': [], 'var_call_biPIoXMp2oT6ycF7fDq7l2bB': 'file_storage/call_biPIoXMp2oT6ycF7fDq7l2bB.json', 'var_call_e5Fqfr4iFQqTQqJSZ0sAql7f': ['checkin', 'business'], 'var_call_5NKdlimcB4x4Ygcg3xajowyv': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
