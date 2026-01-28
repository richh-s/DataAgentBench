code = """# Let's get the list of NYSE non-ETF symbols directly from the query result
import json

# The result is stored in var_functions.query_db:2
nyse_data = var_functions.query_db:2

# The variable name is actually a string containing the variable name
# Let me access it properly
nyse_stocks = var_functions.query_db:2

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'sample_symbols': symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}}

exec(code, env_args)
