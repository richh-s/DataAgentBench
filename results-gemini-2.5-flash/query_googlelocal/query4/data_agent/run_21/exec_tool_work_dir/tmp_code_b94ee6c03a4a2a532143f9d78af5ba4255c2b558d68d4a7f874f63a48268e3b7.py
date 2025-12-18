code = """import json
import re
result_string = locals()['var_function-call-11092242839921597371']['query_db_response']['results'][0]
json_match = re.search(r'\[.*\]', result_string)
if json_match:
    json_data = json.loads(json_match.group(0))
    gmap_ids = [item['gmap_id'] for item in json_data]
    review_counts = {item['gmap_id']: item['high_rating_review_count'] for item in json_data}
else:
    gmap_ids = []
    review_counts = {}
print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids, 'review_counts': review_counts}))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
