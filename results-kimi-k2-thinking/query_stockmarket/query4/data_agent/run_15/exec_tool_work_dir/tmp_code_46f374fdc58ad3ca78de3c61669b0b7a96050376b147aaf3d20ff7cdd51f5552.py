code = """import json

# Load the NYSE stocks data
nyse_file = locals()['var_functions.query_db:0']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]

# Load the stocktrade database tables
stocktrade_file = locals()['var_functions.list_db:6']
with open(stocktrade_file, 'r') as f:
    all_tables = json.load(f)

# Find common symbols (both in NYSE list and have trade data)
common_symbols = list(set(nyse_symbols) & set(all_tables))

result = {
    'nyse_count': len(nyse_symbols),
    'total_tables': len(all_tables),
    'common_count': len(common_symbols),
    'sample_common': common_symbols[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'descriptions_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
