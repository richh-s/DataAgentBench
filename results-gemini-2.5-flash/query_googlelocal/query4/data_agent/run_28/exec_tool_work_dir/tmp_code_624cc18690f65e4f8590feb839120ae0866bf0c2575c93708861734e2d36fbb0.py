code = """import pandas as pd
import json

reviews_output = locals()['var_function-call-2713994913755726959']['results'][0]
business_output = locals()['var_function-call-1432176497897247560']['results'][0]

def parse_tool_output(output_string):
    # The actual JSON string starts after 'The result is:\n'
    start_marker = 'The result is:\n'
    json_start_index = output_string.find(start_marker)
    if json_start_index != -1:
        json_data_str = output_string[json_start_index + len(start_marker):].strip()
        return json.loads(json_data_str)
    return []

reviews_data = parse_tool_output(reviews_output)
business_data = parse_tool_output(business_output)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

# Ensure 'high_rating_review_count' is numeric for potential future calculations
reviews_df['high_rating_review_count'] = pd.to_numeric(reviews_df['high_rating_review_count'])

merged_df = pd.merge(reviews_df, business_df, on='gmap_id', how='inner')

# Select the required columns and convert to JSON
result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
