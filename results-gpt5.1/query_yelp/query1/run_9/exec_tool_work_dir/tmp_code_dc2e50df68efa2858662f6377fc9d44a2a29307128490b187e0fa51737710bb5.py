code = """import json, pandas as pd

businesses = var_call_ifF8UP9eztg8GI0Iac6UmU6u
ids = [b['business_id'].replace('businessid_', 'businessref_') for b in businesses]

path = var_call_CJBUC2XlGZJXtnIEPhwa7KwO
with open(path, 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)
filtered = df[df['business_ref'].isin(ids)].copy()
filtered['rating'] = pd.to_numeric(filtered['rating'])

avg_rating = None
if not filtered.empty:
    avg_rating = filtered['rating'].mean()

result = json.dumps({"average_rating": avg_rating, "business_refs": ids, "review_count": int(filtered.shape[0])})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_uBFZDFnEUYeQBW5BlQ8m7RC3': [], 'var_call_CJBUC2XlGZJXtnIEPhwa7KwO': 'file_storage/call_CJBUC2XlGZJXtnIEPhwa7KwO.json', 'var_call_ifF8UP9eztg8GI0Iac6UmU6u': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
