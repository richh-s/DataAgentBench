code = """import json

# Load data
stockinfo_path = locals()['var_functions.query_db:2']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

nyse_symbols = [item['Symbol'] for item in stockinfo_data]
symbols_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

trade_tables = locals()['var_functions.list_db:10']
with open(trade_tables, 'r') as f:
    trade_tables_list = json.load(f)

common_symbols = list(set(nyse_symbols).intersection(set(trade_tables_list)))
print('Total NYSE non-ETF symbols with price data: ' + str(len(common_symbols)))

# For demonstration, process first 10 symbols
first_ten = common_symbols[:10]
print('First 10 symbols: ' + str(first_ten))

result = {
    'common_symbols': common_symbols,
    'symbols_map': symbols_map
}

print('__RESULT__:')
print(json.dumps({
    'count': len(common_symbols),
    'sample': common_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_count': 234, 'trade_count': 2753, 'common_count': 234, 'common_symbols': ['MGR', 'TCP', 'BKH', 'DGX', 'UTL', 'SRC', 'AIV', 'KW', 'H', 'SLF', 'PFE', 'TGP', 'ZNH', 'CTS', 'RES', 'CMI', 'IT', 'EBS', 'WSM', 'IBM']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'symbol_count': 234, 'sample_symbols': ['PRSP', 'EGO', 'RBC', 'CIA', 'BV', 'VRT', 'ROG', 'EMP', 'AMP', 'SBR']}, 'var_functions.execute_python:16': {'symbol_count': 0, 'sample': []}, 'var_functions.execute_python:18': {'count': 234, 'sample': ['NXN', 'MHE', 'PRSP', 'BLD', 'SOL', 'CXH', 'FMN', 'HRB', 'EPR', 'NFH']}}

exec(code, env_args)
