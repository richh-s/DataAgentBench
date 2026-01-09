code = """import json, pandas as pd

top = pd.DataFrame(var_call_KGszsibSWUTlpjJttCNyPYJk)
biz = pd.DataFrame(var_call_CrHLAFHFgni7pHtS8k8boHAT)

top['high_rating_reviews_2019'] = top['high_rating_reviews_2019'].astype(int)

out = top.merge(biz, on='gmap_id', how='left')[['name','high_rating_reviews_2019']]
out = out.sort_values('high_rating_reviews_2019', ascending=False)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KGszsibSWUTlpjJttCNyPYJk': [{'gmap_id': 'gmap_20', 'high_rating_reviews_2019': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_2019': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_2019': '6'}], 'var_call_CrHLAFHFgni7pHtS8k8boHAT': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
