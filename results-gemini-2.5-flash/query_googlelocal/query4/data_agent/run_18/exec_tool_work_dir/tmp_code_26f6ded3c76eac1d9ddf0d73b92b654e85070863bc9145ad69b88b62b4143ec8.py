code = """import json

# Access the string containing the full output from query_db
full_output_str = locals()['var_function-call-2342706987370194765']['query_db_response']['results'][0]

# Split the string by newlines and get the last non-empty line, which should be the JSON array
json_array_str = [line.strip() for line in full_output_str.splitlines() if line.strip()][-1]

# Parse the JSON array
parsed_reviews = json.loads(json_array_str)

# Extract gmap_ids and their counts
gmap_ids = [item['gmap_id'] for item in parsed_reviews]
high_rating_counts = {item['gmap_id']: item['high_rating_reviews_count'] for item in parsed_reviews}

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'high_rating_counts': high_rating_counts}))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
