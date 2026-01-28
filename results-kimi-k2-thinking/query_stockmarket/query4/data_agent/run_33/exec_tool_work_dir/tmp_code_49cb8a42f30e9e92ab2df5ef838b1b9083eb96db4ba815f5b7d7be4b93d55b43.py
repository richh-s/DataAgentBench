code = """import json

# Load all NYSE non-ETF stocks
stockinfo_data = locals()['var_functions.query_db:36']
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

# Create mapping and list
nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
nyse_symbols = list(nyse_companies.keys())

print(f"Total symbols to analyze: {len(nyse_symbols)}")

# Build the massive UNION ALL query
query_parts = []
for symbol in nyse_symbols:
    part = f"SELECT '{symbol}' as Symbol, (SELECT COUNT(*) FROM \"{symbol}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' AND Close > Open) as UpDays, (SELECT COUNT(*) FROM \"{symbol}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' AND Close < Open) as DownDays"
    query_parts.append(part)

full_query = " UNION ALL ".join(query_parts)

print(f"Query length: {len(full_query)} characters")
print(f"First 500 chars: {full_query[:500]}")

result = {
    'total_symbols': len(nyse_symbols),
    'query_length': len(full_query),
    'ready_to_execute': True
}

# Store the query for next step
with open('/tmp/full_analysis_query.txt', 'w') as f:
    f.write(full_query)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'status': 'ready', 'symbol_count': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'batch_size': 20, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:18': {'total_symbols': 234, 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}, 'var_functions.execute_python:22': {'total_symbols': 234, 'batch_size': 20, 'num_batches': 12, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'status': 'starting_analysis', 'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:28': {'total_stocks': 234, 'num_batches': 5, 'batch_size': 47}, 'var_functions.execute_python:32': {'status': 'test_symbols', 'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [{'Symbol': 'AEFC', 'UpDays': '0', 'DownDays': '0', 'TotalDays': '0'}], 'var_functions.query_db:40': [{'Symbol': 'AIN', 'UpDays': '143', 'DownDays': '101', 'TotalDays': '251'}], 'var_functions.query_db:42': [{'Symbol': 'AIN', 'UpDays': '143', 'DownDays': '101'}, {'Symbol': 'AIV', 'UpDays': '118', 'DownDays': '128'}, {'Symbol': 'AJRD', 'UpDays': '123', 'DownDays': '123'}, {'Symbol': 'AL', 'UpDays': '131', 'DownDays': '117'}, {'Symbol': 'AMN', 'UpDays': '134', 'DownDays': '111'}, {'Symbol': 'AMP', 'UpDays': '141', 'DownDays': '110'}, {'Symbol': 'AMT', 'UpDays': '128', 'DownDays': '123'}, {'Symbol': 'ARD', 'UpDays': '80', 'DownDays': '119'}, {'Symbol': 'ARGD', 'UpDays': '133', 'DownDays': '82'}, {'Symbol': 'ARLO', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'ASG', 'UpDays': '110', 'DownDays': '110'}, {'Symbol': 'AVA', 'UpDays': '134', 'DownDays': '112'}, {'Symbol': 'BANC', 'UpDays': '108', 'DownDays': '119'}, {'Symbol': 'BBU', 'UpDays': '129', 'DownDays': '120'}, {'Symbol': 'BBVA', 'UpDays': '126', 'DownDays': '104'}, {'Symbol': 'BDXA', 'UpDays': '83', 'DownDays': '77'}, {'Symbol': 'BKH', 'UpDays': '134', 'DownDays': '115'}, {'Symbol': 'BKT', 'UpDays': '105', 'DownDays': '97'}, {'Symbol': 'BLD', 'UpDays': '131', 'DownDays': '120'}], 'var_functions.execute_python:46': {'total_stocks': 234, 'processed_batch1': 19, 'status': 'processing_first_batch'}, 'var_functions.execute_python:50': {'valid_stocks': 234, 'missing_stocks': 0, 'sample_valid': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}}

exec(code, env_args)
