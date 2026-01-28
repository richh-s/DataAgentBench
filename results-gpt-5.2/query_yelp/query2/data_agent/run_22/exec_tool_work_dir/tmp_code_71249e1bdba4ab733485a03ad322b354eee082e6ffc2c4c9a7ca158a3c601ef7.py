code = """import json, re
import pandas as pd

# Load businesses
biz_src = var_call_4KAaVzGoxrG48jBkEa05vc8s
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz_records = json.load(f)
else:
    biz_records = biz_src

# Load reviews
rev_src = var_call_6xWhljShtkYDL0KmFSTuZnsG
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev_records = json.load(f)
else:
    rev_records = rev_src

biz_df = pd.DataFrame(biz_records)

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df.get('state') if 'state' in biz_df.columns else None
# use extracted from description
biz_df['state'] = biz_df['description'].apply(extract_state)

# normalize business_ref from business_id
biz_df['business_ref'] = biz_df['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

rev_df = pd.DataFrame(rev_records)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# join reviews with state via business
merged = rev_df.merge(biz_df[['business_ref','state']], on='business_ref', how='left')
merged = merged.dropna(subset=['state','rating'])

# state with highest number of reviews
state_counts = merged.groupby('state').size().sort_values(ascending=False)
max_state = state_counts.index[0]
max_reviews = int(state_counts.iloc[0])

# average rating of businesses in that state: interpret as average star rating per business (mean of its reviews), then mean across businesses in state.
state_reviews = merged[merged['state']==max_state]
biz_avg = state_reviews.groupby('business_ref')['rating'].mean()
state_business_avg_rating = float(biz_avg.mean()) if len(biz_avg)>0 else None

out = {
    'state': max_state,
    'review_count': max_reviews,
    'avg_business_rating': state_business_avg_rating
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7gIxMT87RjboMdV9T6WaOneF': ['checkin', 'business'], 'var_call_jyKTXJxdIwIYJ5NqhjRBnx0M': ['review', 'tip', 'user'], 'var_call_FvjP7bVbuhIaKKJAjYa1nGDC': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_VEibQLAEj2Tw0a4ExGE82xiZ': {'need_full_query': True}, 'var_call_4KAaVzGoxrG48jBkEa05vc8s': 'file_storage/call_4KAaVzGoxrG48jBkEa05vc8s.json', 'var_call_6xWhljShtkYDL0KmFSTuZnsG': 'file_storage/call_6xWhljShtkYDL0KmFSTuZnsG.json'}

exec(code, env_args)
