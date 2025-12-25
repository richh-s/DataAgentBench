code = """import json

account_id_list_str = locals()['var_function-call-8595579920075190144']['query_db_response']['results'][0]
account_id_list = json.loads(account_id_list_str)
account_id = account_id_list[0]['AccountId'].lstrip('#')

print('__RESULT__:')
print(json.dumps(account_id))"""

env_args = {'var_function-call-8595579920075190144': [{'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
