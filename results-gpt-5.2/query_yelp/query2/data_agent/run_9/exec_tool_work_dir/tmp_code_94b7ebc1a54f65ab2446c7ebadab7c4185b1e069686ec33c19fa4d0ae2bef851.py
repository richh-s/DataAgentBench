code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_0FCafEWNzDCyxFVfMTQjn1fl)
rev = load_records(var_call_d2B8rtRoEAk1d7rH7WdBrch3)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

pat = re.compile(r',\s*([A-Z]{2})(?=,|\.|\s|$)')
dfb['state'] = dfb['description'].map(lambda d: pat.findall(d)[-1] if isinstance(d,str) and pat.findall(d) else None)

dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce')
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

# consider only US states: exclude non-US like AB
us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
dfb_us = dfb[dfb['state'].isin(us_states)].copy()

state_reviews = dfb_us.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

top_state = state_reviews.iloc[0]['state']
top_total_reviews = int(state_reviews.iloc[0]['review_count'])

# map refs
business_id_from_ref = dfr['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
dfr2 = dfr.assign(business_id=business_id_from_ref)

joined = dfr2.merge(dfb_us[['business_id','state']], on='business_id', how='inner')
avg_rating = float(joined.loc[joined['state']==top_state, 'rating'].mean())

out = {"state": top_state, "total_reviews": top_total_reviews, "average_rating": avg_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0FCafEWNzDCyxFVfMTQjn1fl': 'file_storage/call_0FCafEWNzDCyxFVfMTQjn1fl.json', 'var_call_d2B8rtRoEAk1d7rH7WdBrch3': 'file_storage/call_d2B8rtRoEAk1d7rH7WdBrch3.json', 'var_call_ILw30yE0blAuVTLXSApnwEqn': {'error': 'No state/review_count data parsed'}, 'var_call_MzpxbkPSXKoeEN2LtPHl09Vd': {'n_rows': 100, 'n_state_nonnull': 0, 'sample_states': [], 'review_count_null': 0, 'review_count_min': 5.0, 'review_count_max': 1742.0, 'sample_desc': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.']}, 'var_call_78JsB6Q2STWanQ9NPEh2ZC7a': {'n_state_nonnull': 100, 'sample_states': ['CA', 'MO', 'ID', 'FL', 'IN', 'PA', 'NJ', 'LA', 'IL', 'TN', 'NV', 'AZ', 'AB'], 'state_counts': {'PA': 27, 'FL': 23, 'IN': 12, 'MO': 9, 'LA': 7, 'AB': 4, 'ID': 4, 'CA': 3, 'IL': 3, 'TN': 3}}}

exec(code, env_args)
