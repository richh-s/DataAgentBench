code = """import json
sales_data = [{"store": "Amazon Music", "total_revenue": 304.13}, {"store": "Apple Music", "total_revenue": 47.52}]
max_store = max(sales_data, key=lambda x: x['total_revenue'])
print("__RESULT__:")
print(json.dumps(max_store))"""

env_args = {'var_function-call-17874948485914521280': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_function-call-12667043518178159716': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_function-call-2016286204723538760': [{'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '47.52'}], 'var_function-call-7469045540074766872': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_function-call-5378673715207993938': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}]}

exec(code, env_args)
