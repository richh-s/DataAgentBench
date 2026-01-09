code = """import json, re, pandas as pd
path = var_call_gQ3UHTfrFpOmaweL7gMOzUlB
with open(path,'r') as f:
    biz = json.load(f)
df = pd.DataFrame(biz)
state_re = re.compile(r'\b([A-Z]{2})\b')
# find all state abbreviations candidates after comma
state_re2 = re.compile(r',\s*([A-Z]{2})(?:\s|,|\.)')

def ex(desc):
    if not isinstance(desc,str):
        return None
    m = state_re2.search(desc)
    return m.group(1) if m else None

df['state']=df['description'].apply(ex)
print('__RESULT__:')
print(json.dumps({'n':len(df),'state_nonnull':int(df['state'].notna().sum()),'states':sorted([s for s in df['state'].dropna().unique().tolist()])[:30], 'sample':df[['description','state']].head(5).to_dict(orient='records')}))"""

env_args = {'var_call_gQ3UHTfrFpOmaweL7gMOzUlB': 'file_storage/call_gQ3UHTfrFpOmaweL7gMOzUlB.json', 'var_call_RpzngHzLL5RY1Jr50OTT0hPk': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}], 'var_call_Zd4WsND2WwPVeXQeJj6wSCjR': 'file_storage/call_Zd4WsND2WwPVeXQeJj6wSCjR.json', 'var_call_vtUalh7ZuBnPaCANyoXWph4Z': [{'n': '2000'}], 'var_call_96PrVBccYifBDnzxtMOkRPI8': [{'n': '784'}], 'var_call_BClyHlwqhbAIaSGYH4dEFP7O': [{'_id': '6859a000fe8b31cd7362e2ab', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_V7E1XNgRNxh4LmLWo1SIlU2T': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_B6uuQmGv3KkVmJbz7ywsbAUc': {'state_with_most_reviews': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}}

exec(code, env_args)
