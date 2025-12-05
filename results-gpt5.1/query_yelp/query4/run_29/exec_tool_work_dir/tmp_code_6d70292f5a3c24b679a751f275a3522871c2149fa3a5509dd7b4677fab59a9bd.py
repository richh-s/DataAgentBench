code = """import json, pandas as pd

business_credit = pd.DataFrame(var_call_LwiZdCbu04usohmm35vmIASB)

with open(var_call_QQcX970zjv8tIHp6Hl9laqUF, 'r') as f:
    reviews = pd.DataFrame(json.load(f))

if 'categories' in business_credit.columns:
    business_credit['category'] = business_credit['categories'].fillna('Unknown')
else:
    business_credit['category'] = 'Unknown'

business_credit['business_ref'] = business_credit['business_id'].str.replace('businessid_', 'businessref_', False)

reviews_subset = reviews.merge(business_credit[['business_ref', 'category']], on='business_ref', how='inner')

reviews_subset['rating'] = pd.to_numeric(reviews_subset['rating'])

agg = reviews_subset.groupby('category').agg(num_businesses=('business_ref', 'nunique'), avg_rating=('rating', 'mean')).reset_index()

max_row = agg.sort_values('num_businesses', ascending=False).iloc[0]

result = {'business_category': max_row['category'], 'num_businesses': int(max_row['num_businesses']), 'average_rating': round(float(max_row['avg_rating']), 3)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LwiZdCbu04usohmm35vmIASB': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_QQcX970zjv8tIHp6Hl9laqUF': 'file_storage/call_QQcX970zjv8tIHp6Hl9laqUF.json'}

exec(code, env_args)
