code = """import json, re
import pandas as pd

businesses = var_call_8OFKxgaVzHgJgMY9djEanppl
with open(var_call_lZmRttBv8Pzc064QJaUFRaa8, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# normalize
if 'review_count' in df_b.columns:
    df_b['review_count'] = pd.to_numeric(df_b['review_count'], errors='coerce')

# extract state
import re

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

df_b['state'] = df_b.get('description', '').apply(extract_state)

# map reviews
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Which business_ids from reviews are present in business collection
unique_review_bids = set(df_r['business_id'].unique())
unique_business_bids = set(df_b['business_id'].unique())

matching_bids = sorted(list(unique_review_bids & unique_business_bids))
nonmatching_sample = sorted(list(unique_review_bids - unique_business_bids))[:20]

# Counts of reviews for matching business ids
df_merged = df_r.merge(df_b[['business_id','state']], on='business_id', how='left')
matched_reviews = df_merged[df_merged['state'].notna()]

state_grp = matched_reviews.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

out = {
    'total_reviews': int(len(df_r)),
    'unique_review_business_ids_count': len(unique_review_bids),
    'unique_business_ids_in_business_collection_count': len(unique_business_bids),
    'matching_business_ids_example': matching_bids,
    'nonmatching_business_ids_sample': nonmatching_sample,
    'matched_reviews_count': int(len(matched_reviews)),
    'state_group': state_grp.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dVDQKJmfHPp9d7FPGQP6jiAE': ['business', 'checkin'], 'var_call_plK4ltDd1O3Ctx1mY9p0kb6b': ['review', 'tip', 'user'], 'var_call_8OFKxgaVzHgJgMY9djEanppl': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_lZmRttBv8Pzc064QJaUFRaa8': 'file_storage/call_lZmRttBv8Pzc064QJaUFRaa8.json', 'var_call_Va7cfeMtMLKTHSxEUozk3iLU': {'state': None, 'review_count': 0, 'average_rating': None}}

exec(code, env_args)
