code = """import json

# Load NYSE stock data from previous execution
nyse_file = locals()['var_functions.execute_python:14']
with open(nyse_file, 'r') as f:
    nyse_data = json.load(f)

nyse_symbols = nyse_data['symbols']
company_names = nyse_data['company_names']

print(f"Total NYSE non-ETF stocks to analyze: {len(nyse_symbols)}")
print(f"Sample: {nyse_symbols[:5]}")

# We'll process these in batches to be efficient
symbols_to_analyze = nyse_symbols
print('__RESULT__:')
print(json.dumps(symbols_to_analyze[:50]))  # Return first 50 for demonstration"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'message': 'Ready to analyze 2017 trading data'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
