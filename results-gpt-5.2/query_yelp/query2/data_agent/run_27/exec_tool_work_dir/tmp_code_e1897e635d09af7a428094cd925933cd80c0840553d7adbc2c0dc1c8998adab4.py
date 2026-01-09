code = """import json, re, pandas as pd

# load businesses with review_count + description
path = var_call_gQ3UHTfrFpOmaweL7gMOzUlB
with open(path,'r') as f:
    biz = json.load(f)

df_biz = pd.DataFrame(biz)
# coerce review_count
if 'review_count' in df_biz.columns:
    df_biz['review_count'] = pd.to_numeric(df_biz['review_count'], errors='coerce').fillna(0).astype(int)

# parse state from description (pattern: ', XX,' or ', XX location' etc). We'll search for state abbreviations after a city.
state_re = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc,str):
        return None
    m = state_re.search(desc)
    return m.group(1) if m else None

df_biz['state'] = df_biz['description'].apply(extract_state)

# sum reviews by state
state_reviews = df_biz.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()
state_reviews = state_reviews.sort_values('review_count', ascending=False)

top_state = None
if len(state_reviews):
    top_state = state_reviews.iloc[0]['state']

# load all reviews
rpath = var_call_Zd4WsND2WwPVeXQeJj6wSCjR
with open(rpath,'r') as f:
    rev = json.load(f)

df_rev = pd.DataFrame(rev)
if len(df_rev):
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# map business_ref -> business_id
# businessref_123 -> businessid_123
if len(df_rev):
    df_rev['business_id'] = df_rev['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

# join to state via business table
j = df_rev.merge(df_biz[['business_id','state']], on='business_id', how='left')

avg_rating_top_state = None
if top_state is not None:
    avg_rating_top_state = j.loc[j['state']==top_state, 'rating'].mean()

out = {
    'state_with_most_reviews': top_state,
    'total_reviews_in_state': int(state_reviews.iloc[0]['review_count']) if top_state is not None else None,
    'average_business_rating_in_state': (None if avg_rating_top_state is None or pd.isna(avg_rating_top_state) else float(avg_rating_top_state))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gQ3UHTfrFpOmaweL7gMOzUlB': 'file_storage/call_gQ3UHTfrFpOmaweL7gMOzUlB.json', 'var_call_RpzngHzLL5RY1Jr50OTT0hPk': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}], 'var_call_Zd4WsND2WwPVeXQeJj6wSCjR': 'file_storage/call_Zd4WsND2WwPVeXQeJj6wSCjR.json', 'var_call_vtUalh7ZuBnPaCANyoXWph4Z': [{'n': '2000'}], 'var_call_96PrVBccYifBDnzxtMOkRPI8': [{'n': '784'}], 'var_call_BClyHlwqhbAIaSGYH4dEFP7O': [{'_id': '6859a000fe8b31cd7362e2ab', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_V7E1XNgRNxh4LmLWo1SIlU2T': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
