code = """import pandas as pd

reviews_data = locals()['var_function-call-3923119794496713091'][0]['results']
business_data = locals()['var_function-call-8402813424855366524'][0]['results']

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
