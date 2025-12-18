code = """import pandas as pd
import json

reviews_output_str = locals()['var_function-call-2713994913755726959']['results'][0]
business_output_str = locals()['var_function-call-1432176497897247560']['results'][0]

# Function to extract the JSON string from the tool output format
def extract_json_data(output_string):
    # The JSON data is usually after 'The result is:\n' and before any trailing newlines
    start_marker = 'The result is:\n'
    start_index = output_string.find(start_marker)
    if start_index != -1:
        json_data_str = output_string[start_index + len(start_marker):].strip()
        # Ensure the string is indeed JSON and not just the beginning of it
        if json_data_str.startswith('[') and json_data_str.endswith(']') or \
           json_data_str.startswith('{') and json_data_str.endswith('}'):
            return json.loads(json_data_str)
    return []

reviews_data = extract_json_data(reviews_output_str)
business_data = extract_json_data(business_output_str)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric type
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
