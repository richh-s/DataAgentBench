code = """import json
import pandas as pd

# business IDs from Indianapolis
biz_docs = var_call_ubsbLnhfPHeRcFv28NJIw2t1
biz_ids = [d['business_id'] for d in biz_docs]
# map to business_ref style
biz_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

# load reviews file
import os
path = var_call_wLOiTNO515hXwpYZUbAqnOZF
with open(path, 'r') as f:
    reviews = json.load(f)

# filter reviews for those business_refs
df = pd.DataFrame(reviews)
mask = df['business_ref'].isin(biz_refs)
sub = df[mask].copy()

if sub.empty:
    result = json.dumps({"average_rating": None, "note": "No reviews found for Indianapolis businesses."})
else:
    sub['rating'] = sub['rating'].astype(float)
    avg = sub['rating'].mean()
    result = json.dumps({"average_rating": round(float(avg), 3)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Lc88awKBmdCBDQ7mVWGwh1EH': [], 'var_call_wLOiTNO515hXwpYZUbAqnOZF': 'file_storage/call_wLOiTNO515hXwpYZUbAqnOZF.json', 'var_call_YuVoN2xnTzNWD0MJDSndV9KR': ['checkin', 'business'], 'var_call_ubsbLnhfPHeRcFv28NJIw2t1': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
