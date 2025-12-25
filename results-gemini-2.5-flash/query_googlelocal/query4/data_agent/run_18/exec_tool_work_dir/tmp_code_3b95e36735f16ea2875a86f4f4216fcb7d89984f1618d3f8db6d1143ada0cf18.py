code = """import json

# Access the raw output dictionary
raw_output_dict = locals()['var_function-call-2342706987370194765']

# Extract the string containing the query result, which is the first element of the 'results' list
full_output_str = raw_output_dict['query_db_response']['results'][0]

# The actual JSON array is embedded within this string. Extract it.
# Find the index of the first '[' and the last ']' to correctly slice the string.
json_start_index = full_output_str.find('[')
json_end_index = full_output_str.rfind(']') + 1

# Slice the string to get only the JSON array part
json_array_str = full_output_str[json_start_index:json_end_index]

# Parse the JSON string into a Python list of dictionaries
parsed_reviews = json.loads(json_array_str)

# Extract gmap_ids and their corresponding high_rating_reviews_count
gmap_ids = [item['gmap_id'] for item in parsed_reviews]
high_rating_counts = {item['gmap_id']: int(item['high_rating_reviews_count']) for item in parsed_reviews}

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'high_rating_counts': high_rating_counts}))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
