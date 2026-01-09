code = """import json, re, pandas as pd

# load
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

# extract state
biz_df['state'] = biz_df['description'].map(lambda d: (re.search(r',\s*([A-Z]{2})', d).group(1) if isinstance(d,str) and re.search(r',\s*([A-Z]{2})', d) else None))

biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)

state_reviews = biz_df.groupby('state')['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]
max_reviews = int(state_reviews.iloc[0])

rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

join_df = rev_df.merge(biz_df[['business_id','state']], on='business_id', how='left')
avg_rating = float(join_df.loc[join_df['state']==top_state,'rating'].mean())

out = {"state": top_state, "total_reviews": max_reviews, "average_rating": round(avg_rating, 4)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oFp9uCuCnEHbiGWrlBK6DRO0': ['business', 'checkin'], 'var_call_0MkDbTgoI9ZkXU4S9XpNHYV4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_gt2QW9QtpN0ykt1WKFnggqAS': 'file_storage/call_gt2QW9QtpN0ykt1WKFnggqAS.json', 'var_call_KeCzlvMQZxV4WsLkX5OOFl8X': 'file_storage/call_KeCzlvMQZxV4WsLkX5OOFl8X.json', 'var_call_D3LcbIMjO6Sm1QyxnwW9bmWV': {'error': 'Could not extract state from business.description'}, 'var_call_47X4yKk959EdeoBehlgQ7Vu3': 'file_storage/call_47X4yKk959EdeoBehlgQ7Vu3.json', 'var_call_DKaqO0dsvDSm2G84a4TFhN7b': {'sample_states': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 'unique': []}, 'var_call_LiVGIsHUlp6GG9QciqCpVy4E': {'match': None}, 'var_call_qhAyIcRCK8ybxEUx3tmC1VX6': {'context': 'n Goleta, CA, this f', 'ord': [110, 32, 71, 111, 108, 101, 116, 97, 44, 32, 67, 65, 44, 32, 116, 104, 105, 115, 32, 102], 'patterns': {'comma_state': True, 'in_city_state': True, 'state_before_comma': False}, 'm1': 'CA', 'm2': 'CA', 'm3': None}, 'var_call_xvrOaG4f1sUDwqyoaT2UsOtB': {'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'regex': 'CA', 'type': "<class 'str'>"}, 'var_call_tvte77fgNtEWhAndNpAVjvSY': {'state_non_null': 100, 'total': 100, 'unique_states': ['AB', 'AZ', 'CA', 'FL', 'ID', 'IL', 'IN', 'LA', 'MO', 'NJ', 'NV', 'PA', 'TN']}}

exec(code, env_args)
