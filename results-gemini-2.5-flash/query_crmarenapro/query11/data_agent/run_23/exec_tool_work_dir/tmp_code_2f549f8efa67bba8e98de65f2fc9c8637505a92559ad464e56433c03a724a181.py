code = """import json

account_data = locals()['var_function-call-8595579920075190144']['query_db_response']['results'][0]
account_id_with_hash = account_data['AccountId']
account_id = account_id_with_hash.lstrip('#')

print('__RESULT__:')
print(json.dumps(account_id))"""

env_args = {'var_function-call-8595579920075190144': [{'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
