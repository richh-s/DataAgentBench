code = """import json, re, pandas as pd
from pathlib import Path

p = Path(var_call_HyyvRxS3PLqxHpN0DQ9tGJtw)
records = json.loads(p.read_text())
df = pd.DataFrame(records)
df['review_count'] = pd.to_numeric(df.get('review_count'), errors='coerce').fillna(0).astype(int)
pat = re.compile(r",\s*([A-Z]{2})(?:,|\b)")

def extract_state(desc):
    if not isinstance(desc,str):
        return None
    m = pat.search(desc)
    return m.group(1) if m else None

df['state'] = df['description'].apply(extract_state)
df2 = df.dropna(subset=['state'])
state_reviews = df2.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
if len(state_reviews)==0:
    out = {"state": None, "total_reviews": 0}
else:
    out = {"state": state_reviews.iloc[0]['state'], "total_reviews": int(state_reviews.iloc[0]['review_count'])}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HyyvRxS3PLqxHpN0DQ9tGJtw': 'file_storage/call_HyyvRxS3PLqxHpN0DQ9tGJtw.json', 'var_call_4sSC9KgC6JHii0hyJlyKW58q': [{'ok': '1'}], 'var_call_siGcoF8XDYUvMdlKCLFQaW5T': {'state': None, 'total_reviews': 0, 'avg_rating_businesses_in_state': None}, 'var_call_YQsf7RVpZytqAs6NzBRLtjXk': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_0p6rbUOrkNZ35EQQZWDRGw43': {'n_sample': 100, 'n_matches': 0, 'unique_states': []}, 'var_call_eWa02WjsUnvnqnImt8HvGnpz': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'], 'var_call_Bca8ZIBREUDVexb83AZwB7OY': {'match': None}, 'var_call_rdRifK2QJqGQjxJskNb1tHli': {'match': 'CA'}}

exec(code, env_args)
