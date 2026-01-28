code = """import json
import pandas as pd
import re

# Load business documents from storage variable
business_docs = var_call_evcPb0YLqREngMtRfpjdOKeV

# Load reviews from the JSON file path stored in var_call_YiEYGld1ya0k8BarnLXoU7o1
reviews_path = var_call_YiEYGld1ya0k8BarnLXoU7o1
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(business_docs)
rdf = pd.DataFrame(reviews)

# Normalize ratings to integers
rdf['rating'] = rdf['rating'].astype(int)

# Create business_id from business_ref by replacing prefix
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Merge reviews with business descriptions
merged = rdf.merge(bdf, on='business_id', how='left')

# Function to extract state (two-letter) from description
state_pattern = re.compile(r',\s*([A-Za-z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1).upper()
    return None

merged['state'] = merged['description'].apply(extract_state)

# Filter reviews that have a state
merged_state = merged[merged['state'].notna()].copy()

# Group by state to get review counts and average rating
grp = merged_state.groupby('state').agg(review_count=('rating', 'count'), average_rating=('rating', 'mean')).reset_index()

# If no states found, prepare empty result
if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # Find state with highest review_count
    top = grp.sort_values(['review_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": round(float(top['average_rating']), 2)}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_A9JqEFm4qqMrKC8bcXwY0iyq': ['business', 'checkin'], 'var_call_ALf0KC0Q08mDuxtPzHdGIDzz': ['review', 'tip', 'user'], 'var_call_evcPb0YLqREngMtRfpjdOKeV': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_YiEYGld1ya0k8BarnLXoU7o1': 'file_storage/call_YiEYGld1ya0k8BarnLXoU7o1.json'}

exec(code, env_args)
