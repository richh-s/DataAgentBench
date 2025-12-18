code = """import pandas as pd

review_data = locals()['var_function-call-15390539203997698213']
business_data = locals()['var_function-call-1776895266584710485']

df_review = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

df_merged = pd.merge(df_review, df_business, on='gmap_id')

result = df_merged[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-15390539203997698213': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1776895266584710485': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
