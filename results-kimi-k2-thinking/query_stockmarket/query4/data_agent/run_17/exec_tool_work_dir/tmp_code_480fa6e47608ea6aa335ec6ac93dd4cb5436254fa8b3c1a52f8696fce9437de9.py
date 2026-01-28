code = """import json

f = open('var_functions.query_db:18', 'r')
nyse_stocks = json.load(f)
f.close()

print('Total=' + str(len(nyse_stocks)))
print('First stock:', nyse_stocks[0]['Symbol'])

symbols = [s['Symbol'] for s in nyse_stocks]
print('Symbols count=' + str(len(symbols)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'symbols': [], 'metadata': []}, 'var_functions.query_db:14': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
