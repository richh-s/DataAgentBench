code = """import json,re
biz = var_call_B6IM8jaF5rX1p5iM8qF2VgoU
states=set(['CA','MO','ID','FL','IN'])
# test regex
res=[]
for r in biz:
    desc=r['description']
    matches=re.findall(r"\b([A-Z]{2})\b", desc)
    res.append({'desc':desc,'matches':matches})
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json', 'var_call_2KcQNtpgWpdSy1Ok7ZD7VufB': [{'ok': '1'}], 'var_call_iDLnvQzRnnHRmtOtfJh3kfSb': {'error': 'no data'}, 'var_call_sEv23LjnqO49MSBvPhfKlGY3': 'file_storage/call_sEv23LjnqO49MSBvPhfKlGY3.json', 'var_call_zXiTEzX91odMa4CJxEAx00gP': {'rows': 100, 'non_null_state': 0, 'states': []}, 'var_call_B6IM8jaF5rX1p5iM8qF2VgoU': [{'_id': '6859a000fe8b31cd7362e2ab', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
