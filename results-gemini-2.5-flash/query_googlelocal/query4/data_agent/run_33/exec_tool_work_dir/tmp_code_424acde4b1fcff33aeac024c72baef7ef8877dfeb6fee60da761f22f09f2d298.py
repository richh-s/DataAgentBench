code = """import pandas as pd
import json

def parse_tool_result_string(result_string):
    # Find the start and end of the JSON array within the string
    start_idx = result_string.find('[')
    end_idx = result_string.rfind(']')

    if start_idx != -1 and end_idx != -1:
        json_array_str = result_string[start_idx : end_idx + 1]
        try:
            return json.loads(json_array_str)
        except json.JSONDecodeError:
            # If JSON decoding fails, return an empty list
            return []
    # If the JSON array markers are not found, return an empty list
    return []

# Extract the raw string results from the previous tool calls
review_data_raw_str = locals()['var_function-call-1719386802118099141']['query_db_response']['results'][0]
business_data_raw_str = locals()['var_function-call-3226297274026103404']['query_db_response']['results'][0]

# Parse the raw strings to get the actual list of dictionaries
review_data = parse_tool_result_string(review_data_raw_str)
business_data = parse_tool_result_string(business_data_raw_str)

# Create DataFrames from the parsed data
df_reviews = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

# Convert 'high_rating_reviews' to integer for proper sorting, if it's not empty
if not df_reviews.empty:
    df_reviews['high_rating_reviews'] = df_reviews['high_rating_reviews'].astype(int)

# Merge the two DataFrames on 'gmap_id'
merged_df = pd.merge(df_reviews, df_business, on='gmap_id', how='inner')

# Sort by high_rating_reviews in descending order and select the top 3
merged_df_sorted = merged_df.sort_values(by='high_rating_reviews', ascending=False).head(3)

# Select the required columns and convert to a list of dictionaries
result_list = merged_df_sorted[['name', 'high_rating_reviews']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-1719386802118099141': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_function-call-3226297274026103404': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
