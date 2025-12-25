code = """import json, pandas as pd, os

biz_cc = pd.DataFrame(var_call_GSsD1q6EYgXK7m5eFg7X6UOg)

reviews_path = var_call_pBvKiCIl2QYLKZZ0qDwQaYWY
with open(reviews_path, 'r') as f:
    reviews = json.load(f)
reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Map business_id to business_ref
biz_cc['business_ref'] = biz_cc['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Count businesses per (category) – but we don't actually have a categories field in the result
# So we can only say among these credit-card-accepting businesses (5 of them) overall

subset_reviews = reviews_df[reviews_df['business_ref'].isin(biz_cc['business_ref'])]

avg_rating = subset_reviews['rating'].mean() if not subset_reviews.empty else None

result = {"note": "Dataset excerpt only; no category data available in returned fields.",
          "businesses_accepting_credit_cards_count": int(biz_cc['business_id'].nunique()),
          "average_rating_all_these_businesses": avg_rating}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZB4sxe3jCnbu50Tt9gqmovED': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_pBvKiCIl2QYLKZZ0qDwQaYWY': 'file_storage/call_pBvKiCIl2QYLKZZ0qDwQaYWY.json', 'var_call_GSsD1q6EYgXK7m5eFg7X6UOg': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}]}

exec(code, env_args)
