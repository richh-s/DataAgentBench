code = """import json, pandas as pd, os

businesses = var_call_b2CeWpEnYqLfIM98XURg0CRg
reviews_path = var_call_KG1Ns02zjUP00REzNKxDOrt3

with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Map business_id -> business_ref
biz_ids = [b['business_id'] for b in businesses]
ref_map = {bid: bid.replace('businessid_', 'businessref_') for bid in biz_ids}
indy_refs = set(ref_map.values())

indy_reviews = [r for r in reviews if r['business_ref'] in indy_refs]

if indy_reviews:
    ratings = [float(r['rating']) for r in indy_reviews]
    avg_rating = sum(ratings) / len(ratings)
else:
    avg_rating = None

result = json.dumps({"average_rating": avg_rating, "review_count": len(indy_reviews)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Sj1wd9kp86BatgNa4Q01xlLP': [], 'var_call_KG1Ns02zjUP00REzNKxDOrt3': 'file_storage/call_KG1Ns02zjUP00REzNKxDOrt3.json', 'var_call_b2CeWpEnYqLfIM98XURg0CRg': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
