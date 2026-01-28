code = """import json
nyse_arca_key = 'var_functions.query_db:0'
list_db_key = 'var_functions.list_db:2'
nyse_arca_file = locals()[nyse_arca_key]
list_db_file = locals()[list_db_key]
print('__RESULT__:')
print(json.dumps({'file1': nyse_arca_file, 'file2': list_db_file}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
