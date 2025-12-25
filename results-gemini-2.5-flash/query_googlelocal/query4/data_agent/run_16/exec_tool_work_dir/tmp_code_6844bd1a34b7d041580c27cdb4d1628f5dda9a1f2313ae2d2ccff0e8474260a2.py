code = """import pandas as pd

review_data = locals()['var_function-call-2676099958683708494']
business_data = locals()['var_function-call-13685899396751876144']

df_review = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_review, df_business, on='gmap_id')

result = []
for index, row in merged_df.iterrows():
    result.append(f"{row['name']} received {row['high_rating_reviews_count']} high-rating reviews.")

print("__RESULT__:")
print(pd.Series(result).to_json(orient='values'))"""

env_args = {'var_function-call-2676099958683708494': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-13685899396751876144': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
