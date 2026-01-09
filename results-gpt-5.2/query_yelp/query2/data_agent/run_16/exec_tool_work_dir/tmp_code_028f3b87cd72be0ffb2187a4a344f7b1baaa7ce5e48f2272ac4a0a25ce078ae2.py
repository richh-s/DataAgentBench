code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_records(var_call_NFEvdMmwAZrZR9o392X4YuFv)
rev = load_records(var_call_S7DU8KadOMgbH0YSvnrEUPHf)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# extract state from ' in City, ST,' pattern
pat = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2}),")
dfb['state'] = dfb['description'].astype(str).str.extract(pat, expand=False)
dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce')

state_reviews = dfb.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    out = {'state': None, 'total_review_count': None, 'average_rating': None}
else:
    state_top = state_reviews.sort_values('review_count', ascending=False).head(1)
    top_state = state_top.iloc[0]['state']
    total_reviews = int(state_top.iloc[0]['review_count'])

    dfr['business_id'] = dfr['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

    joined = dfr.merge(dfb[['business_id','state']], on='business_id', how='inner')
    state_joined = joined[(joined['state']==top_state)].dropna(subset=['rating'])
    avg_rating = float(state_joined['rating'].mean()) if len(state_joined) else None

    out = {'state': top_state, 'total_review_count': total_reviews, 'average_rating': None if avg_rating is None else round(avg_rating, 4)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NFEvdMmwAZrZR9o392X4YuFv': 'file_storage/call_NFEvdMmwAZrZR9o392X4YuFv.json', 'var_call_S7DU8KadOMgbH0YSvnrEUPHf': 'file_storage/call_S7DU8KadOMgbH0YSvnrEUPHf.json', 'var_call_HTO75oPyIwPVZTi0znAPIaAS': {'state': None, 'total_review_count': None, 'average_rating': None}, 'var_call_wQOFaHByNd8FnmkIxqJ2KWLZ': {'non_null_ex1': 0, 'non_null_ex2': 0, 'sample': [{'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'ex1': nan, 'ex2': nan}]}}

exec(code, env_args)
