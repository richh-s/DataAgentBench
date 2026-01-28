code = """import json, pandas as pd

# top business from reviews
top = var_call_sdh69YxrbaaM84BtrkwE0Ni0[0]
business_ref = top['business_ref']
business_id = business_ref.replace('businessref_', 'businessid_')

# load business metadata (name, description)
path_meta = var_call_dNlUtevC2kf7HJPbwTDoPFH8
with open(path_meta, 'r') as f:
    meta = json.load(f)
meta_map = {r['business_id']: r for r in meta}

rec = meta_map.get(business_id, {})
name = rec.get('name')
description = rec.get('description','') or ''

# infer category from description: take text after 'categories of' or 'category of'
category = None
lower = description.lower()
for token in ["categories of ", "category of "]:
    idx = lower.find(token)
    if idx != -1:
        category = description[idx+len(token):].strip()
        # trim trailing punctuation/quotes
        category = category.strip().strip(".\"")
        break
# fallback: try 'including'
if not category:
    idx = lower.find('including')
    if idx != -1:
        category = description[idx+len('including'):].strip().strip('."')

out = {
    "business_id": business_id,
    "business_name": name,
    "category": category,
    "avg_rating": float(top['avg_rating']),
    "review_count_in_period": int(top['review_cnt'])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sdh69YxrbaaM84BtrkwE0Ni0': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_dNlUtevC2kf7HJPbwTDoPFH8': 'file_storage/call_dNlUtevC2kf7HJPbwTDoPFH8.json', 'var_call_DSMfMx7DUWwe2k7tnXFK3W8E': 'file_storage/call_DSMfMx7DUWwe2k7tnXFK3W8E.json'}

exec(code, env_args)
