code = """import json

# Read NYSE stock information
nyse_file = 'file_storage/functions.query_db:32.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract company names
company_names = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    name = desc.split('.')[0] if '.' in desc else desc
    company_names[symbol] = name

# Display first 10 symbols with company names
sample = {}
for i, stock in enumerate(nyse_stocks[:10]):
    symbol = stock['Symbol']
    sample[symbol] = company_names[symbol]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'sample': sample,
    'symbols_list': [stock['Symbol'] for stock in nyse_stocks]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.execute_python:12': {'file_path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_nyse_stocks': 234, 'first_10_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': {'total_nyse_stocks': 234, 'total_trade_tables': 2753, 'available_symbols': 234, 'first_10_available': ['SI', 'CHAP', 'AJRD', 'VKQ', 'RES', 'GLOB', 'UTL', 'PSXP', 'TRV', 'CVX']}, 'var_functions.execute_python:20': {'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'count': 10}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_symbols': 234, 'sample_data': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'symbol': 'AIN', 'company_name': 'Albany International Corporation', 'total_trading_days': 251, 'up_days': 143, 'down_days': 101, 'up_minus_down': 42}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
