code = """import json, pandas as pd

biz = pd.DataFrame(var_call_FSVFqD7M2VJVaPLTH3GxCYhZ)
path = var_call_q2Wlb2GdUInksxNIXooiwFED
with open(path, 'r') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)

# map businessid_X -> businessref_X
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')

merged = rev.merge(biz[['business_ref']], on='business_ref', how='inner')
avg_rating = merged['rating'].mean()

out = {
    'average_rating': None if pd.isna(avg_rating) else float(avg_rating),
    'n_businesses': int(biz.shape[0]),
    'n_reviews': int(merged.shape[0])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FSVFqD7M2VJVaPLTH3GxCYhZ': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}], 'var_call_q2Wlb2GdUInksxNIXooiwFED': 'file_storage/call_q2Wlb2GdUInksxNIXooiwFED.json'}

exec(code, env_args)
