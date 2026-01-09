code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business = load(var_call_wFB96nMbTQEmmYp5NBX1WEjy)
reviews = load(var_call_dVBhWgXVvikQHQ7OhGQ5uGcP)

dfb = pd.DataFrame(business)

dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce').fillna(0).astype(int)

state_re = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    ms = state_re.findall(desc)
    return ms[-1] if ms else None

dfb['state'] = dfb['description'].apply(extract_state)

# filter to recognized US state abbreviations
us_states = set('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split())
dfb = dfb[dfb['state'].isin(us_states)]

state_totals = dfb.groupby('state')['review_count'].sum().sort_values(ascending=False)

top_state = state_totals.index[0]

dfr = pd.DataFrame(reviews)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
# map businessref_X -> businessid_X
suffix = dfr['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
dfr['business_id'] = 'businessid_' + suffix

biz_in_state = set(dfb.loc[dfb['state']==top_state, 'business_id'].astype(str))
avg_rating = dfr.loc[dfr['business_id'].isin(biz_in_state), 'rating'].mean()

out = {
    'state': top_state,
    'total_reviews': int(state_totals.loc[top_state]),
    'average_rating': None if pd.isna(avg_rating) else round(float(avg_rating), 4)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wFB96nMbTQEmmYp5NBX1WEjy': 'file_storage/call_wFB96nMbTQEmmYp5NBX1WEjy.json', 'var_call_dVBhWgXVvikQHQ7OhGQ5uGcP': 'file_storage/call_dVBhWgXVvikQHQ7OhGQ5uGcP.json', 'var_call_48oPPQ9Oqr15FfTO6h9PU67w': {'error': 'Could not extract any state from business.description'}, 'var_call_cVdDCexoNf1fEHQxW5YXdSGP': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
