code = """import json

review_data = json.loads(locals()['var_function-call-16734970030880208519']['results'][0])
gmap_ids = [item['gmap_id'] for item in review_data]

print('__RESULT__:')
print(json.dumps(gmap_ids))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
