code = """import pandas as pd
import json

# Access the raw output from the previous tool calls
reviews_raw_output = locals()['var_function-call-15628865333346599373']['query_db_response']['results'][0]
business_raw_output = locals()['var_function-call-90982732232564603']['query_db_response']['results'][0]

# Function to extract and parse the JSON array from the tool output string
def extract_and_parse_json(output_string):
    # Find the start and end of the JSON array marker
    json_start = output_string.find('[')
    json_end = output_string.rfind(']') + 1 # Include the closing bracket

    if json_start != -1 and json_end != -1:
        json_data_str = output_string[json_start:json_end]
        return json.loads(json_data_str)
    return []

# Extract and parse the JSON data for reviews and businesses
reviews_data = extract_and_parse_json(reviews_raw_output)
business_data = extract_and_parse_json(business_raw_output)

# Create Pandas DataFrames
reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric as it is a string from the query result
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

# Merge the two dataframes on the common 'gmap_id' field
merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

# Select the required columns (name and high_rating_review_count)
# The initial SQL query already sorted and limited to top 3, so no further sorting is strictly needed here.
final_result_df = merged_df[['name', 'high_rating_review_count']]

# Convert the final result DataFrame to a JSON string
result_json = final_result_df.to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-15628865333346599373': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-90982732232564603': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
