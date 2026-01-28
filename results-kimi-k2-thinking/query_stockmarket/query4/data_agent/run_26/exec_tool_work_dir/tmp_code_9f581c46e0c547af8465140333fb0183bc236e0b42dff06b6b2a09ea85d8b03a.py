code = """import json

# Load the NYSE stock data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
valid_symbols = list(symbol_to_company.keys())

print('Total NYSE non-ETF stocks:', len(valid_symbols))
print('Sample symbols:', valid_symbols[:10])

# We'll need to query each stock table for 2017 data
# For efficiency, let's start with a smaller subset to test
batch_size = 20
symbols_to_test = valid_symbols[:batch_size]

result = {
    'total_stocks': len(valid_symbols),
    'batch_size': batch_size,
    'symbols_to_test': symbols_to_test
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_nyse_symbols': 234, 'available_tables': 234, 'sample_symbols': ['MTD', 'PAG', 'SMP', 'ESS', 'MKC']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'symbol_to_company_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}}

exec(code, env_args)
