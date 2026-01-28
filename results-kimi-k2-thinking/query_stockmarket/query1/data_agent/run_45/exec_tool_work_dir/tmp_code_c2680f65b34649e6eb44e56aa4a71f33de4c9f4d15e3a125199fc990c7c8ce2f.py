code = """result = [{"max_adj_close": 18.440000534057617}]
max_price = result[0]["max_adj_close"]
print('__RESULT__:')
print(json.dumps(max_price))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'REAL'}], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
