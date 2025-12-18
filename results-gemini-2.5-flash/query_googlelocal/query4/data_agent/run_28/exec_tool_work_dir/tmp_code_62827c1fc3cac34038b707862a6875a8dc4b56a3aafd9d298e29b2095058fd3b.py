code = """import pandas as pd
import json

reviews_full_output = locals()['var_function-call-15628865333346599373']
business_full_output = locals()['var_function-call-90982732232564603']

# Correctly access the string containing JSON from the tool output structure
reviews_output_str = reviews_full_output['query_db_response']['results'][0]
business_output_str = business_full_output['query_db_response']['results'][0]

# Function to extract and parse the JSON array from the descriptive string
def extract_and_parse_json(output_string):
    # Find the start and end of the JSON array
    json_start = output_string.find('[')
    json_end = output_string.rfind(']') + 1
    if json_start != -1 and json_end != -1:
        json_data_str = output_string[json_start:json_end]
        return json.loads(json_data_str)
    return []

reviews_data = extract_and_parse_json(reviews_output_str)
business_data = extract_and_parse_json(business_output_str)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric type
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

# Merge the two dataframes on 'gmap_id'
merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

# Select the required columns and convert to JSON format
final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-15628865333346599373': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-90982732232564603': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
