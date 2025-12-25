code = """import json, pandas as pd, os

biz_ids_raw = var_call_6onVkD9oBAQazVjX7CmVsRR2
review_path = var_call_bDNmgSqCJ8n6HX18IRS877dN

biz_df = pd.DataFrame(biz_ids_raw)
# map businessid_X -> businessref_X
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

with open(review_path, 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

merged = rev_df.merge(biz_df[['business_ref']], on='business_ref', how='inner')

avg_rating = None
if not merged.empty:
    avg_rating = merged['rating'].mean()

result = json.dumps(avg_rating)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ePdSmVfPofIW6hptRlIN5Bjo': [], 'var_call_bDNmgSqCJ8n6HX18IRS877dN': 'file_storage/call_bDNmgSqCJ8n6HX18IRS877dN.json', 'var_call_6onVkD9oBAQazVjX7CmVsRR2': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
