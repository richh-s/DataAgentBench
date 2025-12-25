code = """import json, pandas as pd, os

businesses = var_call_OxfgdRGx1qQOfPVpszjuZAiV
review_file = var_call_W0ShvuugB8cZ0O6w47rLAHgR

# load all reviews
with open(review_file, 'r') as f:
    reviews = json.load(f)

# build mapping of business_ids in Indianapolis
biz_ids = [b['business_id'] for b in businesses]
# convert to corresponding business_ref values
refs = set(['businessref_' + bid.split('_',1)[1] for bid in biz_ids])

# filter reviews for those business_refs
subset = [r for r in reviews if r['business_ref'] in refs]

if not subset:
    avg = None
else:
    ratings = [int(r['rating']) for r in subset]
    avg = sum(ratings) / len(ratings)

result = json.dumps(avg)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_q7DrYklZwKKqz2jvdNUJ9JVQ': [], 'var_call_W0ShvuugB8cZ0O6w47rLAHgR': 'file_storage/call_W0ShvuugB8cZ0O6w47rLAHgR.json', 'var_call_OxfgdRGx1qQOfPVpszjuZAiV': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
