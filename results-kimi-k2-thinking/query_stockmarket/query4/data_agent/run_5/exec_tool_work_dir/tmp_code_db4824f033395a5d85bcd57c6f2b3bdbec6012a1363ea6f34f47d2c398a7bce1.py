code = """import json

# Load all the batch results directly (they're already lists)
batch1 = locals()['var_functions.query_db:58']
batch2 = locals()['var_functions.query_db:68']
batch3 = locals()['var_functions.query_db:78']
batch4 = locals()['var_functions.query_db:80']
batch5 = locals()['var_functions.query_db:76']

print(f'Batch sizes: {len(batch1)}, {len(batch2)}, {len(batch3)}, {len(batch4)}, {len(batch5)}')

# Load company names from file
stockinfo_file = locals()['var_functions.query_db:38']
with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

symbols_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Combine all results
all_results = batch1 + batch2 + batch3 + batch4 + batch5
print(f'Total results: {len(all_results)}')

# Filter stocks with more up days than down days
positive_stocks = []
for row in all_results:
    try:
        up_days = row['up_days']
        down_days = row['down_days']
        
        # Skip NaN values
        if up_days == 'nan' or down_days == 'nan':
            continue
            
        up = float(up_days)
        down = float(down_days)
        
        if up > down:
            diff = up - down
            symbol = row['symbol']
            positive_stocks.append({
                'symbol': symbol,
                'up_days': up,
                'down_days': down,
                'difference': diff,
                'company_name': symbols_map.get(symbol, 'N/A')
            })
    except Exception as e:
        continue

# Sort by difference in descending order
sorted_stocks = sorted(positive_stocks, key=lambda x: x['difference'], reverse=True)

print(f'Found {len(sorted_stocks)} stocks with more up days than down days')
print('Top 10 by difference:')
for i, stock in enumerate(sorted_stocks[:10], 1):
    print(f"{i}. {stock['symbol']}: {stock['up_days']}-{stock['down_days']} (diff: {stock['difference']:.0f})")

# Get top 5
top_5 = sorted_stocks[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5_stocks': top_5,
    'total_with_more_up_days': len(sorted_stocks)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_count': 234, 'trade_count': 2753, 'common_count': 234, 'common_symbols': ['MGR', 'TCP', 'BKH', 'DGX', 'UTL', 'SRC', 'AIV', 'KW', 'H', 'SLF', 'PFE', 'TGP', 'ZNH', 'CTS', 'RES', 'CMI', 'IT', 'EBS', 'WSM', 'IBM']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'symbol_count': 234, 'sample_symbols': ['PRSP', 'EGO', 'RBC', 'CIA', 'BV', 'VRT', 'ROG', 'EMP', 'AMP', 'SBR']}, 'var_functions.execute_python:16': {'symbol_count': 0, 'sample': []}, 'var_functions.execute_python:18': {'count': 234, 'sample': ['NXN', 'MHE', 'PRSP', 'BLD', 'SOL', 'CXH', 'FMN', 'HRB', 'EPR', 'NFH']}, 'var_functions.execute_python:22': {'count': 234, 'sample': ['GWB', 'ESS', 'SPOT', 'GEL', 'HBI', 'SRT', 'BLD', 'FMN', 'ZTR', 'VRT']}, 'var_functions.execute_python:26': {'test_symbol': 'OCFT', 'total_symbols': 234}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'High': '25.68000030517578', 'Low': '25.559999465942383', 'Close': '25.670000076293945', 'Adj Close': '25.670000076293945', 'Volume': '1088300'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'High': '25.68000030517578', 'Low': '25.549999237060547', 'Close': '25.59000015258789', 'Adj Close': '25.59000015258789', 'Volume': '1128400'}], 'var_functions.query_db:36': [{'first_date': '2017-01-03', 'last_date': '2017-12-29'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:42': [{'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.query_db:44': [{'up_days': '143.0', 'down_days': '101.0', 'total_days': '251'}], 'var_functions.execute_python:46': {'total_symbols': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:48': {'total_symbols': 234, 'batch1_size': 50, 'batch1_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:50': [{'up_days': '118.0', 'down_days': '128.0', 'total_days': '251'}], 'var_functions.query_db:52': [{'up_days': '134.0', 'down_days': '111.0'}], 'var_functions.query_db:54': [{'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.execute_python:56': {'total_symbols': 234, 'ready_to_process': True}, 'var_functions.query_db:58': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.query_db:60': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_functions.execute_python:62': {'total_symbols': 234, 'batches': 5, 'batch_size': 50}, 'var_functions.query_db:68': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_functions.query_db:70': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'symbol': 'H', 'up_days': '135.0', 'down_days': '115.0'}, {'symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}, {'symbol': 'PFE', 'up_days': '141.0', 'down_days': '105.0'}], 'var_functions.query_db:72': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'symbol': 'ESS', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'GEL', 'up_days': '103.0', 'down_days': '144.0'}, {'symbol': 'HBI', 'up_days': '134.0', 'down_days': '112.0'}], 'var_functions.execute_python:74': {'total': 234, 'batches': 6, 'ready': True}, 'var_functions.query_db:76': [{'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'symbol': 'GEL', 'up_days': '103.0', 'down_days': '144.0'}, {'symbol': 'H', 'up_days': '135.0', 'down_days': '115.0'}, {'symbol': 'HBI', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}, {'symbol': 'PFE', 'up_days': '141.0', 'down_days': '105.0'}], 'var_functions.query_db:78': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_functions.query_db:80': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'symbol': 'H', 'up_days': '135.0', 'down_days': '115.0'}, {'symbol': 'PFE', 'up_days': '141.0', 'down_days': '105.0'}]}

exec(code, env_args)
