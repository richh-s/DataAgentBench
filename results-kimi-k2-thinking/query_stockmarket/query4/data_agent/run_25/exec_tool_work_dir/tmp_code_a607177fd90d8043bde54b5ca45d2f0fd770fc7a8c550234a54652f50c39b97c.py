code = """import json

# Read NYSE non-ETF stocks and create company name mapping
nyse_file = 'file_storage/functions.query_db:12.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

company_map = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
non_etf_symbols = list(company_map.keys())

# Read available symbols from stocktrade database
stocktrade_file = 'file_storage/functions.list_db:6.json'
with open(stocktrade_file, 'r') as f:
    all_stocktrade_symbols = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'nyse_symbol_example': non_etf_symbols[0],
    'symbol_in_stocktrade': non_etf_symbols[0] in all_stocktrade_symbols,
    'company_name': company_map[non_etf_symbols[0]]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'error': "[Errno 2] No such file or directory: 'var_functions.list_db:6'", 'success': False}, 'var_functions.execute_python:20': {'count': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': ['Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'nyse_count': 234, 'available_count': 2753, 'valid_count': 234, 'first_valid': ['SSD', 'ESS', 'UHT', 'MKC', 'HIL', 'MFO', 'GWB', 'SRT', 'CRM', 'MR']}, 'var_functions.execute_python:28': {'total_valid': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:30': {'total_nyse_stocks': 234, 'valid_symbols_with_data': 234, 'sample_valid': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:32': {'symbol': 'AIN', 'total_days': 251, 'up_days': 137, 'down_days': 113, 'difference': 24}, 'var_functions.execute_python:34': {'total_nyse_stocks': 234, 'valid_symbols_with_data': 234, 'sample_valid': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'company_name_example': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, 'var_functions.execute_python:36': {'total_symbols': 234, 'first_few': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'company_example': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, 'var_functions.query_db:38': []}

exec(code, env_args)
