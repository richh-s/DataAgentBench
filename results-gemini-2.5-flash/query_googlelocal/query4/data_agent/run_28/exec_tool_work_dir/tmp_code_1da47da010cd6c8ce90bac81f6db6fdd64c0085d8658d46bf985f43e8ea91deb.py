code = """import pandas as pd
import json

reviews_data_str = locals()['var_function-call-2713994913755726959']['results'][0]
business_data_str = locals()['var_function-call-1432176497897247560']['results'][0]

# Extract JSON string by finding the first '[' and last ']'
reviews_json_start = reviews_data_str.find('[')
reviews_json_end = reviews_data_str.rfind(']') + 1
reviews_data = json.loads(reviews_data_str[reviews_json_start:reviews_json_end])

business_json_start = business_data_str.find('[')
business_json_end = business_data_str.rfind(']') + 1
business_data = json.loads(business_data_str[business_json_start:business_json_end])

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
