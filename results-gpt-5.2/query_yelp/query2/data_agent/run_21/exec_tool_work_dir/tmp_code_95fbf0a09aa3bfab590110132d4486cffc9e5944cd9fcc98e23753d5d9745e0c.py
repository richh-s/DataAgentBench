code = """import json, re, pandas as pd

b = var_call_mbiPeEcSJERzYMFYbFc1xa3n
if isinstance(b, str):
    with open(b,'r') as f:
        b=json.load(f)
db=pd.DataFrame(b)

pat = re.compile(r',\s*([A-Z]{2}),')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.search(desc)
    return m.group(1) if m else None

db['state']=db['description'].map(extract_state)

out={'non_null_states': int(db['state'].notna().sum()), 'total': int(len(db)), 'state_counts': db['state'].value_counts().head(10).to_dict()}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mbiPeEcSJERzYMFYbFc1xa3n': 'file_storage/call_mbiPeEcSJERzYMFYbFc1xa3n.json', 'var_call_hPv0Fw6go1L457TQZ7YRhRr0': 'file_storage/call_hPv0Fw6go1L457TQZ7YRhRr0.json', 'var_call_AzqdJv3Ap6l5HZdKKsRoBNnv': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}, 'var_call_PttetLwJcjWmxe13zolpvj2b': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}, 'var_call_alRtSqZxh4fQRTfu4vAIMjwF': {'sample_descriptions': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.']}}

exec(code, env_args)
