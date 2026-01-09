code = """import json, re, pandas as pd

biz_src = var_call_gt2QW9QtpN0ykt1WKFnggqAS
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev_src = var_call_KeCzlvMQZxV4WsLkX5OOFl8X
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# extract state as two-letter uppercase preceded by comma

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df.get('description', pd.Series(dtype='object')).map(extract_state)

biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce')

state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if state_reviews.empty:
    out = {"error": "Could not extract state from business.description"}
else:
    top_state = state_reviews.index[0]
    max_reviews = int(state_reviews.iloc[0])

    rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

    join_df = rev_df.merge(biz_df[['business_id','state']], on='business_id', how='left')
    avg_rating = float(join_df.loc[join_df['state'] == top_state, 'rating'].mean())

    out = {"state": top_state, "total_reviews": max_reviews, "average_business_rating": round(avg_rating, 4)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oFp9uCuCnEHbiGWrlBK6DRO0': ['business', 'checkin'], 'var_call_0MkDbTgoI9ZkXU4S9XpNHYV4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_gt2QW9QtpN0ykt1WKFnggqAS': 'file_storage/call_gt2QW9QtpN0ykt1WKFnggqAS.json', 'var_call_KeCzlvMQZxV4WsLkX5OOFl8X': 'file_storage/call_KeCzlvMQZxV4WsLkX5OOFl8X.json'}

exec(code, env_args)
