code = """import json, pandas as pd, os

# Load reviews
path = var_call_EdCA8r9wR3ICCvYLoWG66oeL
with open(path, 'r') as f:
    reviews = json.load(f)

# Business IDs for Indianapolis, Indiana
biz = var_call_De9NwUMuaFGnOYGwOdtq8sel
biz_ids = [b['business_id'].replace('businessid_', 'businessref_') for b in biz]

# Filter reviews for these businesses
ratings = [int(r['rating']) for r in reviews if r['business_ref'] in biz_ids]

avg_rating = sum(ratings) / len(ratings) if ratings else None

result = json.dumps({"average_rating": avg_rating, "num_reviews": len(ratings)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_00BZFmF79jdjAbQo0VfpqXtO': [], 'var_call_EdCA8r9wR3ICCvYLoWG66oeL': 'file_storage/call_EdCA8r9wR3ICCvYLoWG66oeL.json', 'var_call_De9NwUMuaFGnOYGwOdtq8sel': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
