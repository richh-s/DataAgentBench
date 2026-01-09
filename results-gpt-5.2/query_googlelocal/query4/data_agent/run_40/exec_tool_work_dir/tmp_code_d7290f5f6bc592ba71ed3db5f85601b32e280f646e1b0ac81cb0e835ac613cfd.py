code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_W7TRyGSFGA97jjfLTlES8Nbq)
biz = pd.DataFrame(var_call_xxIjhphqzOXpCun3LyhqUboj)

# ensure numeric
reviews['high_rating_reviews_2019'] = reviews['high_rating_reviews_2019'].astype(int)

out = reviews.merge(biz, on='gmap_id', how='left')[['name','high_rating_reviews_2019']]
out = out.sort_values('high_rating_reviews_2019', ascending=False)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_W7TRyGSFGA97jjfLTlES8Nbq': [{'gmap_id': 'gmap_20', 'high_rating_reviews_2019': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_2019': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_2019': '6'}], 'var_call_xxIjhphqzOXpCun3LyhqUboj': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
