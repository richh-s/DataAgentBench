code = """import json

# Access the string containing the full output from query_db
full_output_str = locals()['var_function-call-2342706987370194765']['query_db_response']['results'][0]

# Find the start of the actual JSON array by searching for the known prefix
json_prefix = '[{"gmap_id":'
json_start_index = full_output_str.find(json_prefix)

# Extract the JSON array string from the identified start to the end of the string
# and remove any trailing newline characters if present.
json_array_str = full_output_str[json_start_index:].strip()

# Parse the JSON array
parsed_reviews = json.loads(json_array_str)

# Extract gmap_ids and their counts
gmap_ids = [item['gmap_id'] for item in parsed_reviews]
high_rating_counts = {item['gmap_id']: int(item['high_rating_reviews_count']) for item in parsed_reviews}

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'high_rating_counts': high_rating_counts}))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
