code = """import pandas as pd
import json

# Access the dictionary output from the previous tool calls
reviews_output = locals()['var_function-call-3923119794444583191']
business_output = locals()['var_function-call-8402813424855366524']

# The actual results are nested within 'query_db_response' and then 'results' list
# We need to get the string from the list first
reviews_raw_string = reviews_output['query_db_response']['results'][0]
business_raw_string = business_output['query_db_response']['results'][0]

# Define a helper function to extract the JSON array string from the full string output
def extract_json_array_string(text):
    # Find the start of the JSON array, which usually comes after "The result is:\n"
    start_marker = "The result is:\n"
    start_index = text.find(start_marker)
    
    if start_index != -1:
        json_part = text[start_index + len(start_marker):].strip()
        # The JSON part should end with ']' followed by a newline or end of string
        # We need to ensure we capture the full JSON array string.
        # Let's find the first '[' and the last ']' to be safe
        actual_start = json_part.find('[')
        actual_end = json_part.rfind(']')
        if actual_start != -1 and actual_end != -1:
            return json_part[actual_start : actual_end + 1]
    return '[]' # Return an empty JSON array string if not found

# Extract and parse the JSON data for reviews
reviews_json_array_str = extract_json_array_string(reviews_raw_string)
reviews_data = json.loads(reviews_json_array_str)

# Extract and parse the JSON data for businesses
business_json_array_str = extract_json_array_string(business_raw_string)
business_data = json.loads(business_json_array_str)

# Create DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric type
df_reviews['high_rating_review_count'] = pd.to_numeric(df_reviews['high_rating_review_count'])

# Merge the Dataframes on 'gmap_id'
merged_df = pd.merge(df_reviews, df_business, on='gmap_id')

# Select the required columns and convert to JSON
final_result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-3923119794496713091': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-8402813424855366524': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
