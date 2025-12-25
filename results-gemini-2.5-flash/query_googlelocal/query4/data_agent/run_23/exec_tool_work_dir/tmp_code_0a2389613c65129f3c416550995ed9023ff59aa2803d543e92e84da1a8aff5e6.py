code = """import pandas as pd
import json

# Access the raw output dictionaries from the previous tool calls
reviews_output_dict = locals()['var_function-call-3923119794496713091']
business_output_dict = locals()['var_function-call-8402813424855366524']

# Extract the full string messages that contain the JSON data
reviews_full_message = reviews_output_dict['query_db_response']['results'][0]
business_full_message = business_output_dict['query_db_response']['results'][0]

# Function to reliably extract the JSON array string from the full message
def extract_json_array_from_message(message_string):
    # The JSON array is preceded by 'The result is:\n'
    start_marker = 'The result is:\n'
    start_index = message_string.find(start_marker)
    
    if start_index != -1:
        json_part = message_string[start_index + len(start_marker):].strip()
        # The JSON part should start with '[' and end with ']'
        # Find the actual start and end of the JSON array within this part
        actual_start = json_part.find('[')
        actual_end = json_part.rfind(']')
        if actual_start != -1 and actual_end != -1:
            return json_part[actual_start : actual_end + 1]
            
    return '[]' # Return an empty JSON array string if the pattern is not found

# Extract and parse the JSON data for reviews
reviews_json_str = extract_json_array_from_message(reviews_full_message)
reviews_data = json.loads(reviews_json_str)

# Extract and parse the JSON data for businesses
business_json_str = extract_json_array_from_message(business_full_message)
business_data = json.loads(business_json_str)

# Create DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric type
df_reviews['high_rating_review_count'] = pd.to_numeric(df_reviews['high_rating_review_count'])

# Merge the DataFrames on 'gmap_id'
merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

# Select the required columns and convert to JSON
final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
