code = """import pandas as pd
import json

# Access the list of outputs from the previous tool calls
# Assuming locals() returns a list, and each item in the list is the dictionary output
reviews_output_list = locals()['var_function-call-3923119794496713091']
business_output_list = locals()['var_function-call-8402813424855366524']

# Get the first (and likely only) dictionary from the list
reviews_output_dict = reviews_output_list[0]
business_output_dict = business_output_list[0]

# Extract the raw string containing the JSON data
reviews_full_string = reviews_output_dict['query_db_response']['results'][0]
business_full_string = business_output_dict['query_db_response']['results'][0]

# Split the string to isolate the JSON part
reviews_json_part_start_tag = "The result is:\n"
business_json_part_start_tag = "The result is:\n"

reviews_json_str = reviews_full_string.split(reviews_json_part_start_tag, 1)[1].strip()
business_json_str = business_full_string.split(business_json_part_start_tag, 1)[1].strip()

# Now, parse the JSON strings
reviews_data = json.loads(reviews_json_str)
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
