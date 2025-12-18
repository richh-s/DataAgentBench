code = """import pandas as pd

high_rating_reviews = locals()['var_function-call-4277610702218006162']['results']
business_names = locals()['var_function-call-10945428614472258574']['results']

df_reviews = pd.DataFrame(high_rating_reviews)
df_businesses = pd.DataFrame(business_names)

df_reviews['high_rating_reviews_count'] = df_reviews['high_rating_reviews_count'].astype(int)

merged_df = pd.merge(df_reviews, df_businesses, on='gmap_id')

# Sort again just to be sure, though it should already be sorted
merged_df = merged_df.sort_values(by='high_rating_reviews_count', ascending=False)

result = merged_df[['name', 'high_rating_reviews_count']].to_dict(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4277610702218006162': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-10945428614472258574': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
