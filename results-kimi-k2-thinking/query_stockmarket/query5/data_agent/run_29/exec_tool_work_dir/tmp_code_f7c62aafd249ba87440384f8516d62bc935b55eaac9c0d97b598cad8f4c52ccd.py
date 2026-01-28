code = """import json

# Get company descriptions from earlier query
with open(locals()['var_functions.query_db:0'], 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Create a dictionary mapping symbols to company descriptions  
company_map = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_capital_stocks}

print('__RESULT__:')
print(json.dumps(company_map))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'nasdaq_capital_count': 86, 'trade_tables_count': 2753, 'valid_symbols_count': 86, 'sample_valid_symbols': ['CCCL', 'ELSE', 'BOTJ', 'CPAH', 'AMHC', 'MNPR', 'CPAAU', 'XBIOW', 'PECK', 'OTEL']}}

exec(code, env_args)
