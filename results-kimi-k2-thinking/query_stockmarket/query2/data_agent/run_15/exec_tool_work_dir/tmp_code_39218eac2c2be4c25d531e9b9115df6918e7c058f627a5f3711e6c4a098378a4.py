code = """import json

symbols_data = var_functions.query_db:0

with open(symbols_data, 'r') as f:
    data = json.load(f)

symbols = [item['Symbol'] for item in data]

result = {'symbol_count': len(symbols), 'first_few_symbols': symbols[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
