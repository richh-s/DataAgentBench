code = """import pandas as pd

reviews_df = pd.DataFrame(locals()['var_function-call-8346541049290418175'])
business_df = pd.DataFrame(locals()['var_function-call-10514793957614381982'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = []
for index, row in merged_df.iterrows():
    result.append(f"{row['name']}: {row['high_rating_review_count']} high-rating reviews")

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8346541049290418175': [{'gmap_id': 'gmap_40', 'high_rating_review_count': '9'}, {'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}], 'var_function-call-10514793957614381982': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
