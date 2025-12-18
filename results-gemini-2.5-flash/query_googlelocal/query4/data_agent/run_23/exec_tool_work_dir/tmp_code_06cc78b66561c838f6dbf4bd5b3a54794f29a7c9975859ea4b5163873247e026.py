code = """import pandas as pd
import json

# Access the raw output strings from the previous tool calls
reviews_raw_output_string = locals()['var_function-call-3923119794496713091']['query_db_response']['results'][0]
business_raw_output_string = locals()['var_function-call-8402813424855366524']['query_db_response']['results'][0]

# Function to extract the JSON array string from the tool's output
def extract_json_from_tool_output(output_text):
    # The JSON array usually starts after 'The result is:\n' and is a valid JSON array string.
    # We need to find the actual beginning and end of the JSON array.
    start_marker = "The result is:\n"
    start_of_json_candidate = output_text.find(start_marker)
    
    if start_of_json_candidate != -1:
        json_part = output_text[start_of_json_candidate + len(start_marker):].strip()
        # Now, find the actual JSON array within this part
        first_bracket_index = json_part.find('[')
        last_bracket_index = json_part.rfind(']')
        if first_bracket_index != -1 and last_bracket_index != -1:
            return json_part[first_bracket_index : last_bracket_index + 1]
    return '[]' # Return an empty JSON array if extraction fails

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
