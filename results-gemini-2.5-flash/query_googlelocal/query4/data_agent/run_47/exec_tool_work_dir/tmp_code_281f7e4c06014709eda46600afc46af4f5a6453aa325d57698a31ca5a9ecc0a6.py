code = """import json

# Access the raw string result from the previous query_db call
raw_db_result = locals()['var_function-call-16734970030880208519']['query_db_response']['results'][0]

# The raw_db_result is a JSON string of a list of dictionaries
review_data = json.loads(raw_db_result)

# Extract gmap_id and high_rating_review_count, converting count to integer
extracted_data = [{'gmap_id': item['gmap_id'], 'high_rating_review_count': int(item['high_rating_review_count'])} for item in review_data]

# Extract gmap_ids for the next query
gmap_ids = [item['gmap_id'] for item in extracted_data]

print('__RESULT__:')
print(json.dumps({'extracted_data': extracted_data, 'gmap_ids': gmap_ids}))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
