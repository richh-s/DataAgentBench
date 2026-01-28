code = """import json
print('__RESULT__:')
print(json.dumps({
    'nyse_arca_file': str(var_functions.query_db:0),
    'available_tickers_file': str(var_functions.list_db:2)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
