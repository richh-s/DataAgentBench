code = """import json

# Read the NYSE non-ETF stocks from the file
file_path = var_functions.query_db_12
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols and create a mapping from symbol to company name
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    # Extract company name from description (usually before "specializes" or similar)
    desc = stock['Company Description']
    company_name = desc.split(' specializes')[0].split(' is ')[0].split(' Inc.')[0].split(' Corporation')[0].split(' Company')[0].strip()
    symbol_to_company[symbol] = company_name

print('__RESULT__:')
print(json.dumps({
    'stock_count': len(nyse_stocks),
    'sample_stocks': list(symbol_to_company.items())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
