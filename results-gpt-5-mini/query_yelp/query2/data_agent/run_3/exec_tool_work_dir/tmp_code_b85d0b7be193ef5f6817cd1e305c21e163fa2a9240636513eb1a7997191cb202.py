code = """import json
import pandas as pd
import re

business_docs = var_call_evcPb0YLqREngMtRfpjdOKeV
reviews_path = var_call_YiEYGld1ya0k8BarnLXoU7o1
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(business_docs)
rdf = pd.DataFrame(reviews)

rdf['rating'] = rdf['rating'].astype(int)
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
merged = rdf.merge(bdf, on='business_id', how='left')

# Count merged rows per business_id
counts = merged.groupby('business_id').agg(review_rows=('rating','count'), description_present=('description', lambda x: int(x.notna().sum()))).reset_index()

# Also show sample merged rows where business_id in our business docs
sample = merged[merged['business_id'].isin(bdf['business_id'])].head(20).to_dict(orient='records')

result = {'counts': counts.to_dict(orient='records'), 'sample_rows': sample}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_A9JqEFm4qqMrKC8bcXwY0iyq': ['business', 'checkin'], 'var_call_ALf0KC0Q08mDuxtPzHdGIDzz': ['review', 'tip', 'user'], 'var_call_evcPb0YLqREngMtRfpjdOKeV': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_YiEYGld1ya0k8BarnLXoU7o1': 'file_storage/call_YiEYGld1ya0k8BarnLXoU7o1.json', 'var_call_8Qx06XwLVfY1r5sXAfw0BhE5': {'state': None, 'review_count': 0, 'average_rating': None}}

exec(code, env_args)
