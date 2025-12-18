code = """import pandas as pd

review_data = pd.DataFrame(locals()['var_function-call-10889661857834623012'])
business_data = pd.DataFrame(locals()['var_function-call-4662037511375471077'])

merged_data = pd.merge(review_data, business_data, on='gmap_id')

result = merged_data[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10889661857834623012': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-4662037511375471077': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
