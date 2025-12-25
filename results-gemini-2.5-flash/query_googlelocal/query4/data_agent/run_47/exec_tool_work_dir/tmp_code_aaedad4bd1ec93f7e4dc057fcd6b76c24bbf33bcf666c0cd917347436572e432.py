code = """import json

# Access the result directly, which should be a Python list of dictionaries
review_data = locals()['var_function-call-16734970030880208519']

extracted_data = []
gmap_ids = []
for item in review_data:
    gmap_id = item['gmap_id']
    high_rating_review_count = int(item['high_rating_review_count'])
    extracted_data.append({'gmap_id': gmap_id, 'high_rating_review_count': high_rating_review_count})
    gmap_ids.append(gmap_id)

print('__RESULT__:')
print(json.dumps({'extracted_data': extracted_data, 'gmap_ids': gmap_ids}))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
