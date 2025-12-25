code = """import json
result_str = locals()['var_function-call-11092242839921597371'][0]
data_start_index = result_str.find('[')
data_end_index = result_str.rfind(']') + 1
json_data_str = result_str[data_start_index:data_end_index]
data = json.loads(json_data_str)
gmap_ids = [item['gmap_id'] for item in data]
print('__RESULT__:')
print(json.dumps(gmap_ids))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
