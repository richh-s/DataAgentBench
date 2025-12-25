code = """import json
import pandas as pd

reviews = pd.DataFrame(var_call_FroT4oUb6f3s3YjsT9CAAC6p)
business = pd.DataFrame(var_call_WePFnDpSpKFh3qqkzeEtfUat)

reviews['high_review_count'] = reviews['high_review_count'].astype(int)

merged = reviews.merge(business, on='gmap_id', how='left')
result = merged[['name', 'high_review_count']].to_dict(orient='records')

json_result = json.dumps(result)
print("__RESULT__:")
print(json_result)"""

env_args = {'var_call_FroT4oUb6f3s3YjsT9CAAC6p': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_JZPZuNVQi6TwbQDhPtIzgHWW': ['business_description'], 'var_call_WePFnDpSpKFh3qqkzeEtfUat': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
