code = """import json, pandas as pd, os

businesses = var_call_Hh7w1VdZlPT9YrvPqGB3efZA
review_path = var_call_7xCqpI81AhIkKrAeUZN1miZO

with open(review_path, 'r') as f:
    reviews = json.load(f)

biz_df = pd.DataFrame(businesses)
if biz_df.empty:
    result = None
else:
    # map business_id -> business_ref
    biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)
    rev_df = pd.DataFrame(reviews)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'])
    merged = rev_df.merge(biz_df[['business_ref']], on='business_ref', how='inner')
    if merged.empty:
        result = None
    else:
        result = merged['rating'].mean()

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_RgnpYgdDMoIZxisQkx02y4AB': [], 'var_call_7xCqpI81AhIkKrAeUZN1miZO': 'file_storage/call_7xCqpI81AhIkKrAeUZN1miZO.json', 'var_call_HmqUHXZWViYlHAHdNeWRod9q': ['business', 'checkin'], 'var_call_Hh7w1VdZlPT9YrvPqGB3efZA': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
