code = """import json

# Load the NASDAQ Capital Market symbols from the previous query
with open('var_functions.query_db:0', 'r') as f:
    nasdaq_cap_symbols = json.load(f)

# Load the list of available tables
with open('var_functions.list_db:2', 'r') as f:
    available_tables = json.load(f)

# Create a set of available symbols for quick lookup
available_symbols = set(available_tables)

# Filter to only include symbols that have data tables
valid_symbols = [{'symbol': item['Symbol'], 'description': item['Company Description']} 
                for item in nasdaq_cap_symbols 
                if item['Symbol'] in available_symbols]

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap_symbols': len(nasdaq_cap_symbols),
    'symbols_with_data': len(valid_symbols),
    'sample_symbols': valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
