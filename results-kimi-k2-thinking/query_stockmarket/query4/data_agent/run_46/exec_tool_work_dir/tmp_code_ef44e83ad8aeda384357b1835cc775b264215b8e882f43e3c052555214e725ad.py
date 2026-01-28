code = """import json

# Read the NYSE stocks data
nyse_file = 'file_storage/functions.query_db:0.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
company_names = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Read the stocktrade database tables list
trade_tables_file = 'file_storage/functions.list_db:16.json'
with open(trade_tables_file, 'r') as f:
    all_trade_tables = json.load(f)

# Find intersection
available_symbols = list(set(nyse_symbols) & set(all_trade_tables))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'total_trade_tables': len(all_trade_tables),
    'available_symbols': len(available_symbols),
    'first_10_available': available_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.execute_python:12': {'file_path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_nyse_stocks': 234, 'first_10_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json'}

exec(code, env_args)
