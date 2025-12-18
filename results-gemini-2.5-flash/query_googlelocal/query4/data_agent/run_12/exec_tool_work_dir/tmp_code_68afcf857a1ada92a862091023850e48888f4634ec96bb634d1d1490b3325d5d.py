code = """import pandas as pd

review_data = locals()['var_function-call-5932954492026361458']
business_data = locals()['var_function-call-15629143246705701963']

df_review = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_review, df_business, on='gmap_id')

final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-5932954492026361458': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-15629143246705701963': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
