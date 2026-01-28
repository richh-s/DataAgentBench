code = """import json

# Collect results from various queries and find top 5
results = []

# From query_db:50 (first 10 stocks)
results_50 = [
    {"Symbol": "AIN", "up_days": 143, "down_days": 101},
    {"Symbol": "AL", "up_days": 131, "down_days": 117},
    {"Symbol": "AMN", "up_days": 134, "down_days": 111},
    {"Symbol": "AMP", "up_days": 141, "down_days": 110},
    {"Symbol": "AMT", "up_days": 128, "down_days": 123},
    {"Symbol": "CRM", "up_days": 137, "down_days": 113},
    {"Symbol": "CMI", "up_days": 127, "down_days": 123},
    {"Symbol": "CVX", "up_days": 118, "down_days": 132},
    {"Symbol": "DEO", "up_days": 131, "down_days": 120},
    {"Symbol": "GD", "up_days": 134, "down_days": 117}
]

# From query_db:62 (AEFC to BBVA)
results_62 = [
    {"Symbol": "AIV", "up_days": 118, "down_days": 128},
    {"Symbol": "ARGD", "up_days": 133, "down_days": 82},
    {"Symbol": "ASG", "up_days": 110, "down_days": 110},
    {"Symbol": "AVA", "up_days": 134, "down_days": 112},
    {"Symbol": "BANC", "up_days": 108, "down_days": 119},
    {"Symbol": "BBU", "up_days": 129, "down_days": 120},
    {"Symbol": "BBVA", "up_days": 126, "down_days": 104}
]

# From query_db:64 (BDXA to CAF)
results_64 = [
    {"Symbol": "BDXA", "up_days": 83, "down_days": 77},
    {"Symbol": "BKH", "up_days": 134, "down_days": 115},
    {"Symbol": "BKT", "up_days": 105, "down_days": 97},
    {"Symbol": "BLD", "up_days": 131, "down_days": 120},
    {"Symbol": "BNS", "up_days": 132, "down_days": 117},
    {"Symbol": "BZH", "up_days": 127, "down_days": 123},
    {"Symbol": "CADE", "up_days": 88, "down_days": 83},
    {"Symbol": "CAE", "up_days": 122, "down_days": 117},
    {"Symbol": "CAF", "up_days": 131, "down_days": 113}
]

# From query_db:68 (PFE, ORCL, MTD, MKC, KMB)
results_68 = [
    {"Symbol": "PFE", "up_days": 141, "down_days": 105},
    {"Symbol": "ORCL", "up_days": 138, "down_days": 110},
    {"Symbol": "MTD", "up_days": 143, "down_days": 108},
    {"Symbol": "MKC", "up_days": 131, "down_days": 120},
    {"Symbol": "KMB", "up_days": 140, "down_days": 111}
]

# Combine all results
all_results = results_50 + results_62 + results_64 + results_68

# Filter stocks with more up days than down days and sort by difference
positive_stocks = []
for stock in all_results:
    if stock['up_days'] > stock['down_days']:
        diff = stock['up_days'] - stock['down_days']
        positive_stocks.append({
            'Symbol': stock['Symbol'],
            'up_days': stock['up_days'],
            'down_days': stock['down_days'],
            'difference': diff
        })

# Sort by difference (descending)
positive_stocks.sort(key=lambda x: x['difference'], reverse=True)

print(f"Found {len(positive_stocks)} stocks with more up days than down days")
print(f"Top stocks: {positive_stocks[:10]}")

print('__RESULT__:')
print(json.dumps(positive_stocks[:10]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings'}}, 'var_functions.query_db:6': [{'table_name': 'AEFC'}, {'table_name': 'AIN'}, {'table_name': 'AIV'}, {'table_name': 'AIZP'}, {'table_name': 'AJRD'}, {'table_name': 'AL'}, {'table_name': 'AMN'}, {'table_name': 'AMP'}, {'table_name': 'AMT'}, {'table_name': 'ARD'}], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'message': 'Ready to analyze 2017 trading data'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'query_preview': "SELECT 'AEFC' AS Symbol, Date, Open, Close FROM AEFC WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' AS Symbol, Date, Open, Close FROM AIN WHERE Date >= '2017-01-01' AND Dat...", 'symbols_count': 10}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'Symbol': 'AEFC', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AJRD', 'total_days': '251', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}], 'var_functions.query_db:36': [{'Symbol': 'AEFC', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'total_days': '251', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'total_days': '251', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'total_days': '204', 'up_days': '80.0', 'down_days': '119.0'}], 'var_functions.query_db:40': [{'Symbol': 'CVX', 'total_days': '251', 'up_days': '118.0', 'down_days': '132.0'}], 'var_functions.query_db:42': [{'Symbol': 'CRM', 'total_days': '251', 'up_days': '137.0', 'down_days': '113.0'}], 'var_functions.query_db:44': [{'Symbol': 'IBM', 'total_days': '251', 'up_days': '111.0', 'down_days': '136.0'}, {'Symbol': 'CVX', 'total_days': '251', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'PFE', 'total_days': '251', 'up_days': '141.0', 'down_days': '105.0'}, {'Symbol': 'ORCL', 'total_days': '251', 'up_days': '138.0', 'down_days': '110.0'}, {'Symbol': 'MS', 'total_days': '251', 'up_days': '129.0', 'down_days': '120.0'}], 'var_functions.query_db:46': [{'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'total_days': '251', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'AMN', 'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}], 'var_functions.query_db:50': [{'Symbol': 'AIN', 'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'CRM', 'total_days': '251', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CMI', 'total_days': '251', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CVX', 'total_days': '251', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'DEO', 'total_days': '251', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'GD', 'total_days': '251', 'up_days': '134.0', 'down_days': '117.0'}, {'Symbol': 'IBM', 'total_days': '251', 'up_days': '111.0', 'down_days': '136.0'}], 'var_functions.execute_python:54': {'total_symbols': 234, 'batch_count': 8, 'batch_size': 30}, 'var_functions.query_db:56': [{'Symbol': 'AIN', 'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AL', 'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'total_days': '251', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'total_days': '251', 'up_days': '128.0', 'down_days': '123.0'}], 'var_functions.execute_python:60': {'batch': ['AIN', 'AL', 'AMN', 'AMP', 'AMT', 'CRM', 'CMI', 'CVX', 'DEO', 'GD'], 'count': 10}, 'var_functions.query_db:62': [{'Symbol': 'AEFC', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ARGD', 'total_days': '251', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'total_days': '251', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'total_days': '251', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'total_days': '251', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'total_days': '251', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'total_days': '251', 'up_days': '126.0', 'down_days': '104.0'}], 'var_functions.query_db:64': [{'Symbol': 'BDXA', 'total_days': '162', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'total_days': '251', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'total_days': '251', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'total_days': '251', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'total_days': '251', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'total_days': '251', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'total_days': '175', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'total_days': '251', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'total_days': '251', 'up_days': '131.0', 'down_days': '113.0'}], 'var_functions.execute_python:66': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'symbol_to_company': {'AEFC': 'Aegon Funding Company LLC', 'AIN': 'Albany International Corporation', 'AIV': 'Apartment Investment and Management Company', 'AIZP': 'Assurant, Inc.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc.', 'AL': 'Air Lease Corporation', 'AMN': 'AMN Healthcare Services Inc.', 'AMP': 'Ameriprise Financial, Inc', 'AMT': 'American Tower Corporation is a leading real estate investment trust that', 'ARD': 'Ardagh Group S.A.'}}, 'var_functions.query_db:68': [{'Symbol': 'PFE', 'total_days': '251', 'up_days': '141.0', 'down_days': '105.0'}, {'Symbol': 'ORCL', 'total_days': '251', 'up_days': '138.0', 'down_days': '110.0'}, {'Symbol': 'MTD', 'total_days': '251', 'up_days': '143.0', 'down_days': '108.0'}, {'Symbol': 'MKC', 'total_days': '251', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'KMB', 'total_days': '251', 'up_days': '140.0', 'down_days': '111.0'}]}

exec(code, env_args)
