code = """import json, pandas as pd

b = var_call_mbiPeEcSJERzYMFYbFc1xa3n
if isinstance(b, str):
    with open(b,'r') as f:
        b=json.load(f)
db=pd.DataFrame(b)

db['review_count']=pd.to_numeric(db['review_count'], errors='coerce')

# state parsing
import re
pat=re.compile(r',\s*([A-Z]{2}),')
db['state']=db['description'].map(lambda d: pat.search(d).group(1) if isinstance(d,str) and pat.search(d) else None)

biz_state=db.dropna(subset=['state','review_count'])[['business_id','state','review_count']]
state_reviews=biz_state.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
top=state_reviews.iloc[0].to_dict()

# reviews
r = var_call_hPv0Fw6go1L457TQZ7YRhRr0
if isinstance(r, str):
    with open(r,'r') as f:
        r=json.load(f)
dr=pd.DataFrame(r)
dr['rating']=pd.to_numeric(dr['rating'], errors='coerce')
dr['business_id']=dr['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)
bs=set(biz_state.loc[biz_state['state']==top['state'],'business_id'])
avg=float(dr.loc[dr['business_id'].isin(bs),'rating'].mean())

out={'state': top['state'], 'total_reviews_in_state': int(top['review_count']), 'average_business_rating_in_state': round(avg,4)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mbiPeEcSJERzYMFYbFc1xa3n': 'file_storage/call_mbiPeEcSJERzYMFYbFc1xa3n.json', 'var_call_hPv0Fw6go1L457TQZ7YRhRr0': 'file_storage/call_hPv0Fw6go1L457TQZ7YRhRr0.json', 'var_call_AzqdJv3Ap6l5HZdKKsRoBNnv': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}, 'var_call_PttetLwJcjWmxe13zolpvj2b': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}, 'var_call_alRtSqZxh4fQRTfu4vAIMjwF': {'sample_descriptions': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.']}, 'var_call_YDoZHnpTqgjNXGxeJ8Qddq3n': {'non_null_states': 99, 'total': 100, 'state_counts': {'PA': 26, 'FL': 23, 'IN': 12, 'MO': 9, 'LA': 7, 'AB': 4, 'ID': 4, 'CA': 3, 'IL': 3, 'TN': 3}}}

exec(code, env_args)
