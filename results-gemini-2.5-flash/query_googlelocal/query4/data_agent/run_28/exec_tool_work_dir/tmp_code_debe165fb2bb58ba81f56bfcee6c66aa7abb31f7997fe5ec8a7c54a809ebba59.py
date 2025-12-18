code = """import pandas as pd
import json

reviews_full_output = locals()['var_function-call-15628865333346599373'] # This should be the entire dict
business_full_output = locals()['var_function-call-90982732232564603'] # This should be the entire dict

# Extract the string containing JSON from the 'results' list
reviews_output_str = reviews_full_output['query_db_response']['results'][0]
business_output_str = business_full_output['query_db_response']['results'][0]

# Find the actual JSON array within the string
def extract_json_data(output_string):
    json_start = output_string.find('[')
    json_end = output_string.rfind(']') + 1
    if json_start != -1 and json_end != -1:
        return json.loads(output_string[json_start:json_end])
    return []

reviews_data = extract_json_data(reviews_output_str)
business_data = extract_json_data(business_output_str)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

final_result = merged_df[['name', 'high_rating_review_count']].sort_values(by='high_rating_review_count', ascending=False)

result_json = final_result.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-15628865333346599373': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-90982732232564603': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
