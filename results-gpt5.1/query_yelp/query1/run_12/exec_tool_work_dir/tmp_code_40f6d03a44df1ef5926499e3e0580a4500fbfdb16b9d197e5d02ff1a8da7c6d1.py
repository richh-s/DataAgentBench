code = """import json, pandas as pd, os

biz_ids = [r['business_id'] for r in var_call_y9opPExB0lDXOcfOsbeVgPNz]

file_path = var_call_EW4wOMP2v04PotC7c43jEAMJ
with open(file_path, 'r') as f:
    reviews = json.load(f)

for r in reviews:
    r['business_id'] = r['business_ref'].replace('businessref_', 'businessid_')

indy_ids = set(biz_ids)
indy_reviews = [r for r in reviews if r['business_id'] in indy_ids]

if indy_reviews:
    for r in indy_reviews:
        r['rating'] = float(r['rating'])
    avg_rating = sum(r['rating'] for r in indy_reviews) / len(indy_reviews)
else:
    avg_rating = None

result = json.dumps(avg_rating)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_vZ2JDZdWQpiT6gGoAGxE3iVm': [], 'var_call_EW4wOMP2v04PotC7c43jEAMJ': 'file_storage/call_EW4wOMP2v04PotC7c43jEAMJ.json', 'var_call_y9opPExB0lDXOcfOsbeVgPNz': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
