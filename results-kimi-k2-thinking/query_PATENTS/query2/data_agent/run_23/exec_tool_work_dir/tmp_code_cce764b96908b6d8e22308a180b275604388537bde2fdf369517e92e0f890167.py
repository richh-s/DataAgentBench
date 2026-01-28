code = """import json
# Get the result from list_db via locals()
db_list_result = locals()['var_functions.list_db:2']
print('__RESULT__:')
print(json.dumps(db_list_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0'}]}

exec(code, env_args)
