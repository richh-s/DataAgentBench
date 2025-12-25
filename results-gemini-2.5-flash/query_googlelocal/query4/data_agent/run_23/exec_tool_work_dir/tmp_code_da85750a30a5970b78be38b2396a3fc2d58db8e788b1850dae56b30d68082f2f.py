code = """import pandas as pd
import json

reviews_raw = locals()['var_function-call-3923119794496713091']['query_db_response']['results'][0]
business_raw = locals()['var_function-call-8402813424855366524']['query_db_response']['results'][0]

# Extract the JSON part from the raw strings and parse them
reviews_json_str = reviews_raw.split('\n', 2)[2].strip()
business_json_str = business_raw.split('\n', 2)[2].strip()

# Remove any leading/trailing comments or text and parse the actual JSON array
reviews_data = json.loads(reviews_json_str)
business_data = json.loads(business_json_str)

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
