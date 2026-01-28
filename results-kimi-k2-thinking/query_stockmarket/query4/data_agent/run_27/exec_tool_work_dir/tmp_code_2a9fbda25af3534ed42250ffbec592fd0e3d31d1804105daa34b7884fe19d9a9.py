code = """import json
import os

# Load all NYSE non-ETF stocks
nyse_file = locals()['var_functions.query_db:30']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    company_name = desc.split(' specializes')[0].split(' is ')[0].split(' Inc.')[0].split(' Corporation')[0].split(' Company')[0].split(' LLC')[0].split(' LP')[0].strip()
    symbol_to_company[symbol] = company_name

# Get all symbols
all_symbols = list(symbol_to_company.keys())

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(all_symbols),
    'symbols': all_symbols
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'stock_count': 234, 'sample_stocks': [['AEFC', 'Aegon Funding'], ['AIN', 'Albany International'], ['AIV', 'Apartment Investment and Management'], ['AIZP', 'Assurant,'], ['AJRD', 'Aerojet Rocketdyne Holdings,'], ['AL', 'Air Lease'], ['AMN', 'AMN Healthcare Services'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.execute_python:20': {'total_nyse_stocks': 234, 'total_trade_symbols': 2753, 'available_nyse_symbols': 234, 'sample_symbols': ['CADE', 'CUBE', 'CHAP', 'EIG', 'USX', 'MNE', 'EV', 'ORCL', 'WOR', 'SAM']}, 'var_functions.execute_python:22': {'mapped_companies': 234, 'sample_mapping': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc.'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.execute_python:24': {'total_nyse_stocks': 234, 'sample_companies': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.']]}, 'var_functions.execute_python:26': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding', 'AIN': 'Albany International', 'AIV': 'Apartment Investment and Management', 'AIZP': 'Assurant,', 'AJRD': 'Aerojet Rocketdyne Holdings,'}}}

exec(code, env_args)
