code = """import json

# Load all symbols and company names
stockinfo_path = locals()['var_functions.query_db:38']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

symbols = [item['Symbol'] for item in stockinfo_data]
symbols_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Test first batch
batch1 = symbols[:10]
print('First 10 symbols to query: ' + str(batch1))

# Build query for just these 10 to test
queries = []
for symbol in batch1:
    q = "SELECT '{}' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM \"{}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(symbol, symbol)
    queries.append(q)

batch_query = ' UNION ALL '.join(queries)
print('Query length: ' + str(len(batch_query)))
print('Query preview: ' + batch_query[:300])

result = {
    'batch_query': batch_query,
    'batch1': batch1,
    'symbols_map': symbols_map,
    'all_symbols': symbols
}

print('__RESULT__:')
print(json.dumps({
    'batch_size': len(batch1),
    'query_ready': True
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_count': 234, 'trade_count': 2753, 'common_count': 234, 'common_symbols': ['MGR', 'TCP', 'BKH', 'DGX', 'UTL', 'SRC', 'AIV', 'KW', 'H', 'SLF', 'PFE', 'TGP', 'ZNH', 'CTS', 'RES', 'CMI', 'IT', 'EBS', 'WSM', 'IBM']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'symbol_count': 234, 'sample_symbols': ['PRSP', 'EGO', 'RBC', 'CIA', 'BV', 'VRT', 'ROG', 'EMP', 'AMP', 'SBR']}, 'var_functions.execute_python:16': {'symbol_count': 0, 'sample': []}, 'var_functions.execute_python:18': {'count': 234, 'sample': ['NXN', 'MHE', 'PRSP', 'BLD', 'SOL', 'CXH', 'FMN', 'HRB', 'EPR', 'NFH']}, 'var_functions.execute_python:22': {'count': 234, 'sample': ['GWB', 'ESS', 'SPOT', 'GEL', 'HBI', 'SRT', 'BLD', 'FMN', 'ZTR', 'VRT']}, 'var_functions.execute_python:26': {'test_symbol': 'OCFT', 'total_symbols': 234}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'High': '25.68000030517578', 'Low': '25.559999465942383', 'Close': '25.670000076293945', 'Adj Close': '25.670000076293945', 'Volume': '1088300'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'High': '25.68000030517578', 'Low': '25.549999237060547', 'Close': '25.59000015258789', 'Adj Close': '25.59000015258789', 'Volume': '1128400'}], 'var_functions.query_db:36': [{'first_date': '2017-01-03', 'last_date': '2017-12-29'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:42': [{'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.query_db:44': [{'up_days': '143.0', 'down_days': '101.0', 'total_days': '251'}], 'var_functions.execute_python:46': {'total_symbols': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:48': {'total_symbols': 234, 'batch1_size': 50, 'batch1_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:50': [{'up_days': '118.0', 'down_days': '128.0', 'total_days': '251'}], 'var_functions.query_db:52': [{'up_days': '134.0', 'down_days': '111.0'}], 'var_functions.query_db:54': [{'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.execute_python:56': {'total_symbols': 234, 'ready_to_process': True}, 'var_functions.query_db:58': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.query_db:60': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_functions.execute_python:62': {'total_symbols': 234, 'batches': 5, 'batch_size': 50}}

exec(code, env_args)
