code = """import pandas as pd
import json

reviews_raw_output = locals()['var_function-call-2713994913755726959']['results'][0]
business_raw_output = locals()['var_function-call-1432176497897247560']['results'][0]

def extract_json_from_tool_output(raw_output_string):
    # Find the start and end of the JSON array within the string
    json_start_index = raw_output_string.find('[')
    json_end_index = raw_output_string.rfind(']')

    if json_start_index != -1 and json_end_index != -1:
        json_string = raw_output_string[json_start_index : json_end_index + 1]
        return json.loads(json_string)
    return []

reviews_data = extract_json_from_tool_output(reviews_raw_output)
business_data = extract_json_from_tool_output(business_raw_output)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Convert 'high_rating_review_count' to numeric type as it's a string from the query
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

# Sort by high_rating_review_count in descending order and get the top 3
# (though the initial SQL query already limited to 3, this is good practice)
final_result = merged_df.sort_values(by='high_rating_review_count', ascending=False).head(3)

result_json = final_result[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
