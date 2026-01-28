code = """import json
import pandas as pd
import re

reviews_path = var_call_YiEYGld1ya0k8BarnLXoU7o1
business_path = var_call_Bm2uvDw7QJnUsy7daA2cu3oH

with open(reviews_path, 'r') as f:
    reviews = json.load(f)
with open(business_path, 'r') as f:
    businesses = json.load(f)

rdf = pd.DataFrame(reviews)
bdf = pd.DataFrame(businesses)

rdf['rating'] = rdf['rating'].astype(int)
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# US states
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
pattern = re.compile(r"\b(" + "|".join(states) + r")\b", flags=re.IGNORECASE)

# Map business_id to extracted state
biz_state = {}
for b in businesses:
    desc = b.get('description') or ''
    m = pattern.search(desc)
    if m:
        biz_state[b['business_id']] = m.group(1).upper()
    else:
        biz_state[b['business_id']] = None

rdf['state'] = rdf['business_id'].map(biz_state)

merged = rdf[rdf['state'].notna()].copy()

if merged.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    grp = merged.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()
    top = grp.sort_values(by='review_count', ascending=False).iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": round(float(top['average_rating']), 2)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_A9JqEFm4qqMrKC8bcXwY0iyq': ['business', 'checkin'], 'var_call_ALf0KC0Q08mDuxtPzHdGIDzz': ['review', 'tip', 'user'], 'var_call_evcPb0YLqREngMtRfpjdOKeV': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_YiEYGld1ya0k8BarnLXoU7o1': 'file_storage/call_YiEYGld1ya0k8BarnLXoU7o1.json', 'var_call_8Qx06XwLVfY1r5sXAfw0BhE5': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_2TFq7sT8U3MgsL8JPMv6x3kV': 'file_storage/call_2TFq7sT8U3MgsL8JPMv6x3kV.json', 'var_call_Bm2uvDw7QJnUsy7daA2cu3oH': 'file_storage/call_Bm2uvDw7QJnUsy7daA2cu3oH.json', 'var_call_QXgoWXf2gygZ8g4z0XccNs7V': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_d6xnECHKWAVBWWpCMf1KRdbI': 'file_storage/call_d6xnECHKWAVBWWpCMf1KRdbI.json'}

exec(code, env_args)
