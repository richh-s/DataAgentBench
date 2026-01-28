code = """import json

# Access the stored result directly
nyse_stocks = locals()['var_functions.query_db:18']
print('Total=' + str(len(nyse_stocks)))
print('First stock:', nyse_stocks[0]['Symbol'])

# Extract symbols
symbols = [s['Symbol'] for s in nyse_stocks]
print('Symbols count=' + str(len(symbols)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'symbols': [], 'metadata': []}, 'var_functions.query_db:14': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
