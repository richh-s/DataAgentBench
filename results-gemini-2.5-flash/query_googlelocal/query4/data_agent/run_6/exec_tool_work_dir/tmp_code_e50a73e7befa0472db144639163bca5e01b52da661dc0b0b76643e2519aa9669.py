code = """import pandas as pd

review_data = locals()['var_function-call-14947926169325849196']
business_data = locals()['var_function-call-229396674620463562']

df_review = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_review, df_business, on='gmap_id', how='inner')

result = merged_df[['name', 'high_rating_reviews']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14947926169325849196': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_function-call-229396674620463562': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-2144796909045237085': [{'gmap_id': 'gmap_40', 'high_rating_reviews': '9'}, {'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}]}

exec(code, env_args)
