code = """import pandas as pd

reviews_df = pd.DataFrame(locals()['var_function-call-5412217530846681266'])
business_df = pd.DataFrame(locals()['var_function-call-15555277164857305659'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = merged_df[['name', 'high_rating_reviews']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5412217530846681266': [{'gmap_id': 'gmap_40', 'high_rating_reviews': '9'}, {'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}], 'var_function-call-15555277164857305659': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
