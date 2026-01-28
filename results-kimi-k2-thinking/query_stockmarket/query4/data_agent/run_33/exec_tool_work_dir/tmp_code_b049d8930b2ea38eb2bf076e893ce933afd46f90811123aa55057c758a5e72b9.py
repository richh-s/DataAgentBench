code = """import json

# Load NYSE non-ETF stocks
stockinfo_data = locals()['var_functions.query_db:54']
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Collect all batch results
all_results = []
batches = ['var_functions.query_db:42', 'var_functions.query_db:58', 'var_functions.query_db:66', 'var_functions.query_db:68', 'var_functions.query_db:70', 'var_functions.query_db:74']
for batch_key in batches:
    batch_data = locals()[batch_key]
    if isinstance(batch_data, str):
        with open(batch_data, 'r') as f:
            batch_data = json.load(f)
    all_results.extend(batch_data)

# Find stocks with more up days than down days in 2017
stocks_more_up_days = []
for stock in all_results:
    up_days = int(stock['UpDays'])
    down_days = int(stock['DownDays'])
    if up_days > down_days and up_days > 0:  # Has trading data and more up days
        stocks_more_up_days.append({
            'Symbol': stock['Symbol'],
            'Company': nyse_companies[stock['Symbol']],
            'UpDays': up_days,
            'DownDays': down_days,
            'Margin': up_days - down_days
        })

# Sort by margin (descending)
sorted_stocks = sorted(stocks_more_up_days, key=lambda x: x['Margin'], reverse=True)

# Get top 5
top_5 = sorted_stocks[:5]

print(f"Total stocks analyzed: {len(all_results)}")
print(f"Stocks with more up days: {len(stocks_more_up_days)}")
print(f"Top 5 by margin:")
for i, stock in enumerate(top_5, 1):
    print(f"  {i}. {stock['Symbol']}: {stock['UpDays']} up, {stock['DownDays']} down (margin: {stock['Margin']})")

result = {
    'total_analyzed': len(all_results),
    'stocks_more_up': len(stocks_more_up_days),
    'top_5_companies': [(stock['Symbol'], stock['Company']) for stock in top_5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'status': 'ready', 'symbol_count': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'batch_size': 20, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:18': {'total_symbols': 234, 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}, 'var_functions.execute_python:22': {'total_symbols': 234, 'batch_size': 20, 'num_batches': 12, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'status': 'starting_analysis', 'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:28': {'total_stocks': 234, 'num_batches': 5, 'batch_size': 47}, 'var_functions.execute_python:32': {'status': 'test_symbols', 'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [{'Symbol': 'AEFC', 'UpDays': '0', 'DownDays': '0', 'TotalDays': '0'}], 'var_functions.query_db:40': [{'Symbol': 'AIN', 'UpDays': '143', 'DownDays': '101', 'TotalDays': '251'}], 'var_functions.query_db:42': [{'Symbol': 'AIN', 'UpDays': '143', 'DownDays': '101'}, {'Symbol': 'AIV', 'UpDays': '118', 'DownDays': '128'}, {'Symbol': 'AJRD', 'UpDays': '123', 'DownDays': '123'}, {'Symbol': 'AL', 'UpDays': '131', 'DownDays': '117'}, {'Symbol': 'AMN', 'UpDays': '134', 'DownDays': '111'}, {'Symbol': 'AMP', 'UpDays': '141', 'DownDays': '110'}, {'Symbol': 'AMT', 'UpDays': '128', 'DownDays': '123'}, {'Symbol': 'ARD', 'UpDays': '80', 'DownDays': '119'}, {'Symbol': 'ARGD', 'UpDays': '133', 'DownDays': '82'}, {'Symbol': 'ARLO', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'ASG', 'UpDays': '110', 'DownDays': '110'}, {'Symbol': 'AVA', 'UpDays': '134', 'DownDays': '112'}, {'Symbol': 'BANC', 'UpDays': '108', 'DownDays': '119'}, {'Symbol': 'BBU', 'UpDays': '129', 'DownDays': '120'}, {'Symbol': 'BBVA', 'UpDays': '126', 'DownDays': '104'}, {'Symbol': 'BDXA', 'UpDays': '83', 'DownDays': '77'}, {'Symbol': 'BKH', 'UpDays': '134', 'DownDays': '115'}, {'Symbol': 'BKT', 'UpDays': '105', 'DownDays': '97'}, {'Symbol': 'BLD', 'UpDays': '131', 'DownDays': '120'}], 'var_functions.execute_python:46': {'total_stocks': 234, 'processed_batch1': 19, 'status': 'processing_first_batch'}, 'var_functions.execute_python:50': {'valid_stocks': 234, 'missing_stocks': 0, 'sample_valid': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': {'total_stocks': 234, 'num_batches': 24, 'batch_size': 10}, 'var_functions.query_db:58': [{'Symbol': 'BNS', 'UpDays': '132', 'DownDays': '117'}, {'Symbol': 'BV', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'BZH', 'UpDays': '127', 'DownDays': '123'}, {'Symbol': 'CADE', 'UpDays': '88', 'DownDays': '83'}, {'Symbol': 'CAE', 'UpDays': '122', 'DownDays': '117'}, {'Symbol': 'CAF', 'UpDays': '131', 'DownDays': '113'}, {'Symbol': 'CBT', 'UpDays': '128', 'DownDays': '122'}, {'Symbol': 'CCC', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'CCZ', 'UpDays': '17', 'DownDays': '10'}, {'Symbol': 'CHAP', 'UpDays': '34', 'DownDays': '23'}], 'var_functions.execute_python:60': {'found_stocks': 21, 'batch1_count': 19, 'batch2_count': 10, 'top_3': [{'Symbol': 'ARGD', 'Company': 'Argo Group International Holdings, Ltd. specializes in providing insurance and reinsurance solutions, helping businesses manage risks and safeguard their assets worldwide.', 'UpDays': 133, 'DownDays': 82, 'Margin': 51}, {'Symbol': 'AIN', 'Company': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'UpDays': 143, 'DownDays': 101, 'Margin': 42}, {'Symbol': 'AMP', 'Company': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'UpDays': 141, 'DownDays': 110, 'Margin': 31}]}, 'var_functions.execute_python:62': {'processed': 29, 'found_with_more_up': 21, 'current_top_5': [{'Symbol': 'ARGD', 'UpDays': 133, 'DownDays': 82, 'Margin': 51}, {'Symbol': 'AIN', 'UpDays': 143, 'DownDays': 101, 'Margin': 42}, {'Symbol': 'AMP', 'UpDays': 141, 'DownDays': 110, 'Margin': 31}, {'Symbol': 'AMN', 'UpDays': 134, 'DownDays': 111, 'Margin': 23}, {'Symbol': 'AVA', 'UpDays': 134, 'DownDays': 112, 'Margin': 22}]}, 'var_functions.execute_python:64': {'remaining_symbols': 205, 'next_batch': ['CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM']}, 'var_functions.query_db:66': [{'Symbol': 'CCZ', 'UpDays': '17', 'DownDays': '10'}, {'Symbol': 'CHAP', 'UpDays': '34', 'DownDays': '23'}, {'Symbol': 'CIA', 'UpDays': '130', 'DownDays': '112'}, {'Symbol': 'CMA', 'UpDays': '124', 'DownDays': '124'}, {'Symbol': 'CMI', 'UpDays': '127', 'DownDays': '123'}, {'Symbol': 'CMSA', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'CNK', 'UpDays': '128', 'DownDays': '122'}, {'Symbol': 'COTY', 'UpDays': '124', 'DownDays': '123'}, {'Symbol': 'CRC', 'UpDays': '121', 'DownDays': '128'}, {'Symbol': 'CRM', 'UpDays': '137', 'DownDays': '113'}], 'var_functions.query_db:68': [{'Symbol': 'CRS', 'UpDays': '121', 'DownDays': '128'}, {'Symbol': 'CSL', 'UpDays': '131', 'DownDays': '119'}, {'Symbol': 'CTS', 'UpDays': '113', 'DownDays': '122'}, {'Symbol': 'CUBE', 'UpDays': '133', 'DownDays': '113'}, {'Symbol': 'CURO', 'UpDays': '9', 'DownDays': '7'}, {'Symbol': 'CVIA', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'CVX', 'UpDays': '118', 'DownDays': '132'}, {'Symbol': 'CXH', 'UpDays': '126', 'DownDays': '91'}, {'Symbol': 'DAC', 'UpDays': '66', 'DownDays': '115'}, {'Symbol': 'DDS', 'UpDays': '128', 'DownDays': '123'}], 'var_functions.query_db:70': [{'Symbol': 'DDT', 'UpDays': '118', 'DownDays': '119'}, {'Symbol': 'DGX', 'UpDays': '129', 'DownDays': '121'}, {'Symbol': 'DMB', 'UpDays': '132', 'DownDays': '95'}, {'Symbol': 'DTQ', 'UpDays': '139', 'DownDays': '98'}, {'Symbol': 'DXC', 'UpDays': '133', 'DownDays': '116'}, {'Symbol': 'EARN', 'UpDays': '114', 'DownDays': '124'}, {'Symbol': 'EBS', 'UpDays': '133', 'DownDays': '115'}, {'Symbol': 'EGO', 'UpDays': '108', 'DownDays': '123'}, {'Symbol': 'CVX', 'UpDays': '118', 'DownDays': '132'}, {'Symbol': 'CXH', 'UpDays': '126', 'DownDays': '91'}], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': [{'Symbol': 'EGY', 'UpDays': '100', 'DownDays': '128'}, {'Symbol': 'EIG', 'UpDays': '125', 'DownDays': '116'}, {'Symbol': 'ELF', 'UpDays': '121', 'DownDays': '129'}, {'Symbol': 'EMP', 'UpDays': '74', 'DownDays': '100'}, {'Symbol': 'ENLC', 'UpDays': '107', 'DownDays': '124'}, {'Symbol': 'EPR', 'UpDays': '132', 'DownDays': '117'}, {'Symbol': 'EPRT', 'UpDays': '0', 'DownDays': '0'}, {'Symbol': 'ES', 'UpDays': '132', 'DownDays': '117'}, {'Symbol': 'ESRT', 'UpDays': '124', 'DownDays': '125'}, {'Symbol': 'ESS', 'UpDays': '128', 'DownDays': '123'}]}

exec(code, env_args)
