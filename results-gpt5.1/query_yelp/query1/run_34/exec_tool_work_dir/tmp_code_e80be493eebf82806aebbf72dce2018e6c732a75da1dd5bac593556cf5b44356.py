code = """import json, pandas as pd, os

# Load reviews from file
with open(var_call_yxvhDFKckvMbOmcwXfIpY7uN, 'r') as f:
    reviews = json.load(f)

# Indianapolis business_ids
biz_ids = [d['business_id'] for d in var_call_DS8WMqU8asJejx1eXmOa8A5L]

# Map businessid_ -> businessref_
ref_ids = {bid.replace('businessid_', 'businessref_') for bid in biz_ids}

# Filter reviews to those business_refs
ratings = [int(r['rating']) for r in reviews if r['business_ref'] in ref_ids]

avg = sum(ratings) / len(ratings) if ratings else None

result = json.dumps(avg)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_jL4WJLbKq3l3BJ2C4IKeRJWQ': [], 'var_call_yxvhDFKckvMbOmcwXfIpY7uN': 'file_storage/call_yxvhDFKckvMbOmcwXfIpY7uN.json', 'var_call_DS8WMqU8asJejx1eXmOa8A5L': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
