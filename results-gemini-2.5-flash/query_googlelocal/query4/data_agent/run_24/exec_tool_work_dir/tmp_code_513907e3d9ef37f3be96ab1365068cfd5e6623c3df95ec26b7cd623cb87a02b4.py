code = """import pandas as pd

review_counts = [{"gmap_id": "gmap_20", "high_rating_review_count": "8"}, {"gmap_id": "gmap_53", "high_rating_review_count": "7"}, {"gmap_id": "gmap_40", "high_rating_review_count": "6"}]
business_names = [{"name": "Aurora Massage", "gmap_id": "gmap_20"}, {"name": "The Boochyard @ Local Roots", "gmap_id": "gmap_53"}, {"name": "Widows Peak Salon", "gmap_id": "gmap_40"}]

df_reviews = pd.DataFrame(review_counts)
df_businesses = pd.DataFrame(business_names)

merged_df = pd.merge(df_reviews, df_businesses, on='gmap_id')
result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-12870002700024485307': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-3774866274573869395': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
