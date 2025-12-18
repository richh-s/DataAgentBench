code = """import json

# Correctly access the string containing the JSON array and parse it
raw_result_str = locals()['var_function-call-2342706987370194765']['query_db_response']['results'][0]
parsed_reviews = json.loads(raw_result_str)

# Extract gmap_ids and their counts
gmap_ids = [item['gmap_id'] for item in parsed_reviews]
high_rating_counts = {item['gmap_id']: item['high_rating_reviews_count'] for item in parsed_reviews}

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'high_rating_counts': high_rating_counts}))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
