code = """import pandas as pd
import json

# Access the raw output dictionaries from the previous tool calls
reviews_output_dict = locals()['var_function-call-3923119794496713091']
business_output_dict = locals()['var_function-call-8402813424855366524']

# Extract the full string messages that contain the JSON data
reviews_full_message = reviews_output_dict['query_db_response']['results'][0]
business_full_message = business_output_dict['query_db_response']['results'][0]

# --- Inline JSON extraction for reviews ---
reviews_start_index = reviews_full_message.find('[')
reviews_end_index = reviews_full_message.rfind(']')
reviews_json_str = '[]'
if reviews_start_index != -1 and reviews_end_index != -1:
    reviews_json_str = reviews_full_message[reviews_start_index : reviews_end_index + 1]
reviews_data = json.loads(reviews_json_str)

# --- Inline JSON extraction for business data ---
business_start_index = business_full_message.find('[')
business_end_index = business_full_message.rfind(']')
business_json_str = '[]'
if business_start_index != -1 and business_end_index != -1:
    business_json_str = business_full_message[business_start_index : business_end_index + 1]
business_data = json.loads(business_json_str)

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

df_reviews['high_rating_review_count'] = pd.to_numeric(df_reviews['high_rating_review_count'])

merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
