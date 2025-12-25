code = """import pandas as pd

reviews_data = locals()['var_function-call-10452213959901156025']
business_data = locals()['var_function-call-10402780053629018176']

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = merged_df[['name', 'high_rating_reviews_count']].to_dict(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10452213959901156025': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-10402780053629018176': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
