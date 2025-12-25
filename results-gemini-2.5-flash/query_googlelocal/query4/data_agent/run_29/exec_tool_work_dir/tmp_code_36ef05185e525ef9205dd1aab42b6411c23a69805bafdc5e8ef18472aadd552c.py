code = """import pandas as pd

reviews_df = pd.DataFrame(locals()['var_function-call-17054838408837804918'])
business_df = pd.DataFrame(locals()['var_function-call-5081746791130703546'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-17054838408837804918': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-5081746791130703546': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
