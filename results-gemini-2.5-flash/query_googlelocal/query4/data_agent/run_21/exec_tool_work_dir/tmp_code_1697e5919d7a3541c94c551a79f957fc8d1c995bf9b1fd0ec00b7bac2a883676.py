code = """import json
data = locals()['var_function-call-11092242839921597371']
gmap_ids = [item['gmap_id'] for item in data]
review_counts = {item['gmap_id']: item['high_rating_review_count'] for item in data}
print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'review_counts': review_counts}))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
