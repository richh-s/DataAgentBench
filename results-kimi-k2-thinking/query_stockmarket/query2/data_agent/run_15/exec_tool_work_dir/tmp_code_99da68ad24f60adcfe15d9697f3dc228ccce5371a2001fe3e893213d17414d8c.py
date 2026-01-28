code = """import json

# Let's check what data we have for a few different symbols
arca_symbols_file = locals()['var_functions.query_db:0']
trade_symbols_file = locals()['var_functions.list_db:6']

with open(arca_symbols_file, 'r') as f:
    arca_symbols_data = json.load(f)

symbols = [item['Symbol'] for item in arca_symbols_data]

# Let's try the first 10 symbols to see what 2015 data looks like
first_symbols = symbols[:10]

result = {'symbols': first_symbols}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'arca_etf_count': 1435, 'available_in_trade_db': 1435, 'first_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': []}

exec(code, env_args)
