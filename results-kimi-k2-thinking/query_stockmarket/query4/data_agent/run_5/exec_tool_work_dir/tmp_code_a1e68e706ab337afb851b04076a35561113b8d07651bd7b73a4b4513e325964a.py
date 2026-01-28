code = """import json

# Load symbols and company names from stored data
stockinfo_path = locals()['var_functions.query_db:38']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

symbols_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
all_symbols = list(symbols_map.keys())

print(f'Loaded {len(all_symbols)} NYSE non-ETF symbols')

# Since we need to query each symbol individually, let's track our progress
# We'll query in batches and collect results

batch_size = 50
symbols_batch1 = all_symbols[:batch_size]

print(f'Processing first batch of {len(symbols_batch1)} symbols')
print(f'Batch 1: {symbols_batch1}')

result = {
    'all_symbols': all_symbols,
    'symbols_map': symbols_map,
    'batch1': symbols_batch1,
    'total_symbols': len(all_symbols)
}

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(all_symbols),
    'batch1_size': len(symbols_batch1),
    'batch1_symbols': symbols_batch1[:10]  # Show first 10
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_count': 234, 'trade_count': 2753, 'common_count': 234, 'common_symbols': ['MGR', 'TCP', 'BKH', 'DGX', 'UTL', 'SRC', 'AIV', 'KW', 'H', 'SLF', 'PFE', 'TGP', 'ZNH', 'CTS', 'RES', 'CMI', 'IT', 'EBS', 'WSM', 'IBM']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'symbol_count': 234, 'sample_symbols': ['PRSP', 'EGO', 'RBC', 'CIA', 'BV', 'VRT', 'ROG', 'EMP', 'AMP', 'SBR']}, 'var_functions.execute_python:16': {'symbol_count': 0, 'sample': []}, 'var_functions.execute_python:18': {'count': 234, 'sample': ['NXN', 'MHE', 'PRSP', 'BLD', 'SOL', 'CXH', 'FMN', 'HRB', 'EPR', 'NFH']}, 'var_functions.execute_python:22': {'count': 234, 'sample': ['GWB', 'ESS', 'SPOT', 'GEL', 'HBI', 'SRT', 'BLD', 'FMN', 'ZTR', 'VRT']}, 'var_functions.execute_python:26': {'test_symbol': 'OCFT', 'total_symbols': 234}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'High': '25.68000030517578', 'Low': '25.559999465942383', 'Close': '25.670000076293945', 'Adj Close': '25.670000076293945', 'Volume': '1088300'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'High': '25.68000030517578', 'Low': '25.549999237060547', 'Close': '25.59000015258789', 'Adj Close': '25.59000015258789', 'Volume': '1128400'}], 'var_functions.query_db:36': [{'first_date': '2017-01-03', 'last_date': '2017-12-29'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:42': [{'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.query_db:44': [{'up_days': '143.0', 'down_days': '101.0', 'total_days': '251'}], 'var_functions.execute_python:46': {'total_symbols': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}}

exec(code, env_args)
