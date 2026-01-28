code = """import json

arca_symbols_file = locals()['var_functions.query_db:0']
with open(arca_symbols_file, 'r') as f:
    arca_symbols_data = json.load(f)

symbols = [item['Symbol'] for item in arca_symbols_data]

query_template = 'SELECT "Adj Close" FROM {symbol} WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'

queries = []
for symbol in symbols:
    query = query_template.format(symbol=symbol)
    queries.append({'db_name': 'stocktrade_database', 'query': query})

result = {
    'total_symbols': len(symbols),
    'queries_count': len(queries)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'arca_etf_count': 1435, 'available_in_trade_db': 1435, 'first_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:18': []}

exec(code, env_args)
