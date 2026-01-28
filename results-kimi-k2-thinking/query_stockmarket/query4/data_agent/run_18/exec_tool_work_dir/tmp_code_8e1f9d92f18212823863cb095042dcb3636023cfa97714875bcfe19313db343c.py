code = """import json
import os

# Load NYSE stocks
stockinfo_path = locals().get('var_functions.query_db:14', '')
with open(stockinfo_path, 'r') as f:
    nyse_stocks = json.load(f)

symbol_to_name = {stock['Symbol']: stock['Company Description'].split(' specializes in')[0].strip() for stock in nyse_stocks}
all_symbols = list(symbol_to_name.keys())

# Check which tables exist
trade_tables_path = locals().get('var_functions.list_db:5', '')
with open(trade_tables_path, 'r') as f:
    available_tables = set(json.load(f))

# Only process symbols that have trade data
valid_symbols = [sym for sym in all_symbols if sym in available_tables]

# Process in smaller batches - let's start with first 20 symbols
batch_size = 20
first_batch = valid_symbols[:batch_size]

print('__RESULT__:')
print(json.dumps({
    'total_valid_stocks': len(valid_symbols),
    'first_batch_symbols': first_batch,
    'sample_company_name': symbol_to_name[first_batch[1]] if len(first_batch) > 1 else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 234, 'first_few': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'first_few_available': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'sample_mapping': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.execute_python:12': {'total_nyse_stocks': 234, 'first_ten_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_symbols': 234, 'first_few_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_name': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, 'var_functions.execute_python:18': {'count': 234, 'first_stock': {'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.execute_python:20': {'total_stocks': 234, 'num_batches': 8, 'batch_size': 30, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ']}, 'var_functions.execute_python:22': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:24': {'message': 'Preparing to analyze 234 NYSE stocks for 2017 performance', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:32': {'message': 'Processing 234 NYSE stocks', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
