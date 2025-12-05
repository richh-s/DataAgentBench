code = """import json, pandas as pd, os, re

# Load reviews
path = var_call_FoGjFp9VWoBWLs48OplR4Ar3
with open(path, 'r') as f:
    reviews = json.load(f)

# Business_ids in Indianapolis
biz = var_call_NXo8NvcVfObOT6qgG3I7Pe7c

# Map businessid_ -> businessref_
ids = [b['business_id'] for b in biz]
ref_ids = set(['businessref_' + re.sub('^businessid_', '', i) for i in ids])

# Filter reviews for these businesses
ratings = [int(r['rating']) for r in reviews if r['business_ref'] in ref_ids]

avg = sum(ratings) / len(ratings) if ratings else None

result = json.dumps(avg)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_m2BadPUKEfTjjuSVRPycZfBJ': [], 'var_call_FoGjFp9VWoBWLs48OplR4Ar3': 'file_storage/call_FoGjFp9VWoBWLs48OplR4Ar3.json', 'var_call_NXo8NvcVfObOT6qgG3I7Pe7c': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
