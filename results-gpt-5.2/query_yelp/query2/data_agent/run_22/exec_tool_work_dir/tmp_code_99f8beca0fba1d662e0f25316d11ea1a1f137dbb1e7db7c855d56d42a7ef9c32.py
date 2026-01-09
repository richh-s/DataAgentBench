code = """import json, re
import pandas as pd

# load
with open(var_call_4KAaVzGoxrG48jBkEa05vc8s,'r') as f:
    biz_records=json.load(f)
with open(var_call_6xWhljShtkYDL0KmFSTuZnsG,'r') as f:
    rev_records=json.load(f)

biz_df=pd.DataFrame(biz_records)
rev_df=pd.DataFrame(rev_records)

# extract state from description
import re

def extract_state(desc):
    if not isinstance(desc,str):
        return None
    m=re.search(r",\s*([A-Z]{2})(?:\b|,)" , desc)
    return m.group(1) if m else None

biz_df['state']=biz_df['description'].apply(extract_state)
biz_df['business_ref']=biz_df['business_id'].astype(str).str.replace('businessid_','businessref_',regex=False)

rev_df['rating']=pd.to_numeric(rev_df['rating'],errors='coerce')
merged=rev_df.merge(biz_df[['business_ref','state']],on='business_ref',how='left').dropna(subset=['state','rating'])
# US states only (exclude Canadian AB)
us=merged[merged['state'].isin(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])]

state_counts=us.groupby('state').size().sort_values(ascending=False)
max_state=state_counts.index[0]
max_reviews=int(state_counts.iloc[0])

state_reviews=us[us['state']==max_state]
biz_avg=state_reviews.groupby('business_ref')['rating'].mean()
avg_business_rating=float(biz_avg.mean())

out={'state':max_state,'review_count':max_reviews,'avg_business_rating':avg_business_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7gIxMT87RjboMdV9T6WaOneF': ['checkin', 'business'], 'var_call_jyKTXJxdIwIYJ5NqhjRBnx0M': ['review', 'tip', 'user'], 'var_call_FvjP7bVbuhIaKKJAjYa1nGDC': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_VEibQLAEj2Tw0a4ExGE82xiZ': {'need_full_query': True}, 'var_call_4KAaVzGoxrG48jBkEa05vc8s': 'file_storage/call_4KAaVzGoxrG48jBkEa05vc8s.json', 'var_call_6xWhljShtkYDL0KmFSTuZnsG': 'file_storage/call_6xWhljShtkYDL0KmFSTuZnsG.json', 'var_call_CvJAqrjvbcnrlw1PMpAZp54d': {'n_reviews_total': 2000, 'n_reviews_joined': 2000, 'n_with_state': 1955, 'states_found': {'PA': 617, 'FL': 406, 'MO': 213, 'IN': 176, 'ID': 126, 'LA': 125, 'CA': 75, 'NV': 65, 'AB': 45, 'TN': 39}}}

exec(code, env_args)
