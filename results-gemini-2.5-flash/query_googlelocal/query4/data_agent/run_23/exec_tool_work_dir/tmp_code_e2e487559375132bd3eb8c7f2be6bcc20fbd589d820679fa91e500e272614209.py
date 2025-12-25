code = """import pandas as pd
import json

reviews_raw_list = locals()['var_function-call-3923119794496713091']['query_db_response']['results']
business_raw_list = locals()['var_function-call-8402813424855366524']['query_db_response']['results']

reviews_data = []
for item in reviews_raw_list:
    # Find the start and end of the JSON array
    start_index = item.find('[')
    end_index = item.rfind(']')
    if start_index != -1 and end_index != -1:
        json_str = item[start_index : end_index + 1]
        reviews_data.extend(json.loads(json_str))

business_data = []
for item in business_raw_list:
    start_index = item.find('[')
    end_index = item.rfind(']')
    if start_index != -1 and end_index != -1:
        json_str = item[start_index : end_index + 1]
        business_data.extend(json.loads(json_str))

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
