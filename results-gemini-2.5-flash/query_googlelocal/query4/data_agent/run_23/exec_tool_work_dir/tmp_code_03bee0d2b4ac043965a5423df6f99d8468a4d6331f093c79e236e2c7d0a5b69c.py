code = """import pandas as pd
import json

# Access the raw output strings from the previous tool calls
reviews_raw_output_string = locals()['var_function-call-3923119794496713091']['query_db_response']['results'][0]
business_raw_output_string = locals()['var_function-call-8402813424855366524']['query_db_response']['results'][0]

# Function to extract the JSON array string from the tool's output
def extract_json_from_tool_output(output_text):
    # Find the start of the JSON array marker '['
    start_index = output_text.find('[')
    # Find the end of the JSON array marker ']'
    end_index = output_text.rfind(']')
    
    if start_index != -1 and end_index != -1:
        # Extract the substring that contains the JSON array
        json_array_str = output_text[start_index : end_index + 1]
        return json_array_str
    return '[]' # Return an empty JSON array string if not found

# Extract and parse the JSON data for reviews
reviews_json_str = extract_json_from_tool_output(reviews_raw_output_string)
reviews_data = json.loads(reviews_json_str)

# Extract and parse the JSON data for businesses
business_json_str = extract_json_from_tool_output(business_raw_output_string)
business_data = json.loads(business_json_str)

# Create DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

# Ensure 'high_rating_review_count' is numeric
df_reviews['high_rating_review_count'] = pd.to_numeric(df_reviews['high_rating_review_count'])

# Merge the DataFrames on 'gmap_id'
merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

# Select the required columns and convert to JSON
final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
