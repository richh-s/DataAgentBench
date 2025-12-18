code = """import json

result_reviews = json.loads(locals()['var_function-call-2342706987370194765']['results'][0])
gmap_ids = [item['gmap_id'] for item in result_reviews]
print('__RESULT__:')
print(json.dumps(gmap_ids))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}]}

exec(code, env_args)
