code = """import json

# Read the full NYSE stocks data
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Total NYSE non-ETF stocks: {len(nyse_symbols)}")
print(f"Symbols: {nyse_symbols}")

# Also store the mappings
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    symbol_to_company[symbol] = stock['Company Description']

# Store for future use
output_data = {
    'symbols': nyse_symbols,
    'symbol_to_company': symbol_to_company
}

print('__RESULT__:')
print(json.dumps(output_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
