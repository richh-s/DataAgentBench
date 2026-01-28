code = """import json
import re
import pandas as pd

biz = var_call_sjU0gxiN4j5ujlsu5JKnWCGD
reviews_path = var_call_OtIIQA6kEpd4jg9w3UlnX9u7
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(biz)
df_b['id_num'] = df_b['business_id'].str.replace(r'^[^0-9]*', '', regex=True)
df_b['business_ref'] = 'businessref_' + df_b['id_num']

import re

def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    return m.group(1) if m else None

df_b['state'] = df_b['description'].apply(extract_state)

# reviews
with open(reviews_path, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)

# show business dataframe
biz_records = df_b.to_dict(orient='records')

# count reviews per business_ref
counts = df_r['business_ref'].value_counts().to_dict()

# for our business_refs, get counts
matches = []
for br in df_b['business_ref'].tolist():
    matches.append({'business_ref': br, 'state': df_b.loc[df_b['business_ref']==br,'state'].iloc[0], 'review_matches': int(counts.get(br,0))})

# Also compute overall group by state using only matched reviews
# merge
if not df_r.empty:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    df = df_r.merge(df_b[['business_ref','state']], on='business_ref', how='left')
    grp = df.dropna(subset=['state']).groupby('state').agg(review_count=('review_id','count'), average_rating=('rating','mean')).reset_index()
    grp_list = grp.to_dict(orient='records')
else:
    grp_list = []

result = {'businesses': biz_records, 'matches': matches, 'state_groups': grp_list}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M53Zd50Tdxo3C8spMUnoWPOA': ['business', 'checkin'], 'var_call_QIGLXDR8UK49ck6WHsYD4aTj': ['review', 'tip', 'user'], 'var_call_sjU0gxiN4j5ujlsu5JKnWCGD': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_OtIIQA6kEpd4jg9w3UlnX9u7': 'file_storage/call_OtIIQA6kEpd4jg9w3UlnX9u7.json', 'var_call_uDFvRZebNdcirwemcZg9t5iA': {'state': None, 'review_count': 0, 'average_rating': None}}

exec(code, env_args)
