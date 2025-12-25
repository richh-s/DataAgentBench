code = """import json, pandas as pd, os

# business ids from Mongo
biz = var_call_P2tt2F3n72f6opiYg0YwABZL
biz_ids = [b['business_id'] for b in biz]

# map to business_ref ids
refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

# load full review table from file
path = var_call_NohPOalYu06Szp5TKG9RwIVU
with open(path, 'r') as f:
    reviews = json.load(f)

# filter reviews for those business_refs
ref_set = set(refs)
filtered = [r for r in reviews if r['business_ref'] in ref_set]

if filtered:
    ratings = [int(r['rating']) for r in filtered]
    avg = sum(ratings) / len(ratings)
else:
    avg = None

result = json.dumps({'average_rating_indianapolis': avg})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_4b6U6nNakZjlpvQPKjgpPPu1': [], 'var_call_NohPOalYu06Szp5TKG9RwIVU': 'file_storage/call_NohPOalYu06Szp5TKG9RwIVU.json', 'var_call_ApNHL0qZezzMryBfWsqJqrCK': ['checkin', 'business'], 'var_call_P2tt2F3n72f6opiYg0YwABZL': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
