code = """import pandas as pd

review_counts = locals()['var_function-call-169876401973465938']
business_names = locals()['var_function-call-9168517039227602158']

df_review_counts = pd.DataFrame(review_counts)
df_business_names = pd.DataFrame(business_names)

merged_df = pd.merge(df_review_counts, df_business_names, on='gmap_id')

result = merged_df[['name', 'high_rating_reviews_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-169876401973465938': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-9168517039227602158': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
