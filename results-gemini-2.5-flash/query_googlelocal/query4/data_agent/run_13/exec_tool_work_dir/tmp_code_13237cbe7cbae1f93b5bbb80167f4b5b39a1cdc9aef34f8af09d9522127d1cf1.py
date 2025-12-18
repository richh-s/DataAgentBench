code = """import pandas as pd
import json
import re

def extract_json_from_string(s):
    # The JSON data is embedded in a string, so we need to extract it first
    match = re.search(r'\[.*\]', s, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    return []

reviews_output = locals()['var_function-call-1154572447019601798'] # This is the dictionary returned by query_db
businesses_output = locals()['var_function-call-15074447506706639510'] # This is the dictionary returned by query_db

reviews_data_str = reviews_output['query_db_response']['results'][0]
businesses_data_str = businesses_output['query_db_response']['results'][0]

reviews_data = extract_json_from_string(reviews_data_str)
businesses_data = extract_json_from_string(businesses_data_str)

reviews_df = pd.DataFrame(reviews_data)
businesses_df = pd.DataFrame(businesses_data)

# Ensure the count is an integer for proper sorting/analysis if needed
reviews_df['high_rating_review_count'] = reviews_df['high_rating_review_count'].astype(int)

merged_df = pd.merge(reviews_df, businesses_df, on='gmap_id')
result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-1154572447019601798': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-15074447506706639510': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
