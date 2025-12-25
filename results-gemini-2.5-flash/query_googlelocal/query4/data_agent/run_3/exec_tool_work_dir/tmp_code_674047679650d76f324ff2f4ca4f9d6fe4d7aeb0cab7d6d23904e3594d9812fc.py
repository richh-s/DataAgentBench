code = """import pandas as pd

review_data = pd.DataFrame(locals()['var_function-call-7184732621470134376'])
business_data = pd.DataFrame(locals()['var_function-call-13939954515279507277'])

merged_data = pd.merge(review_data, business_data, on = 'gmap_id', how = 'inner')

result = []
for index, row in merged_data.iterrows():
    result.append(f"{row['name']}: {row['high_rating_review_count']} high-rating reviews")

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10543616994899230039': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-7184732621470134376': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-13939954515279507277': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
