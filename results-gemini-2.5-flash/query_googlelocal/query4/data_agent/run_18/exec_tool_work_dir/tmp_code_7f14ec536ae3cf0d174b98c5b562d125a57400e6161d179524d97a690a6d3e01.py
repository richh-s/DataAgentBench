code = """import json

# Assuming var_function-call-2342706987370194765 directly contains the list of dictionaries
# and that the 'high_rating_reviews_count' values are strings which need to be converted to integers.
parsed_reviews = locals()['var_function-call-2342706987370194765']

# Extract gmap_ids and their corresponding high_rating_reviews_count
gmap_ids = [item['gmap_id'] for item in parsed_reviews]
high_rating_counts = {item['gmap_id']: int(item['high_rating_reviews_count']) for item in parsed_reviews}

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'high_rating_counts': high_rating_counts}))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
