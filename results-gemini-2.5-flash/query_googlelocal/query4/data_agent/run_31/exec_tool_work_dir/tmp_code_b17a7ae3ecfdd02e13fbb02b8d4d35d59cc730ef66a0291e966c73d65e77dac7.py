code = """import json

gmap_ids_str = json.loads(locals()['var_function-call-15828406422703651902'])

sql_query = f"SELECT name, gmap_id FROM business_description WHERE gmap_id IN ({gmap_ids_str});"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-5084043016580269099': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-15828406422703651902': "'gmap_20', 'gmap_53', 'gmap_40'"}

exec(code, env_args)
