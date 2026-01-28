code = """import json

# Load NYSE stocks data
result_key = "var_functions.query_db:62"
result_file = locals()[result_key]
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create dictionary mapping symbol to company name
stock_info = {stock['Symbol']: stock['CompanyName'] for stock in nyse_stocks}

# Process ARD data
ard_key = "var_functions.query_db:94"
ard_file = locals()[ard_key]
with open(ard_file, 'r') as f:
    ard_data = json.load(f)

# Count up/down days for ARD
up_days = 0
down_days = 0
for day in ard_data:
    close_price = float(day['Close'])
    open_price = float(day['Open'])
    if close_price > open_price:
        up_days += 1
    elif close_price < open_price:
        down_days += 1

ard_diff = up_days - down_days

# Current top stocks
min_diff = 14  # Current 3rd place
top_5 = [
    {'symbol': 'AMT', 'diff': 31, 'company': stock_info['AMT'], 'up': 141, 'down': 110},
    {'symbol': 'AMN', 'diff': 23, 'company': stock_info['AMN'], 'up': 134, 'down': 111},
    {'symbol': 'AL', 'diff': 14, 'company': stock_info['AL'], 'up': 131, 'down': 117}
]

# Check if ARD qualifies
if ard_diff > min_diff:
    top_5.append({
        'symbol': 'ARD',
        'diff': ard_diff,
        'company': stock_info['ARD'],
        'up': up_days,
        'down': down_days
    })
    top_5.sort(key=lambda x: x['diff'], reverse=True)
    if len(top_5) > 5:
        top_5 = top_5[:5]
        min_diff = min(stock['diff'] for stock in top_5)

print('__RESULT__:')
print(json.dumps({
    'ARD': {'up': up_days, 'down': down_days, 'diff': ard_diff},
    'top_5': top_5,
    'need_more': len(top_5) < 5
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': [{'Symbol': 'AEFC', 'CompanyName': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'CompanyName': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'CompanyName': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'CompanyName': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'CompanyName': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}, {'Symbol': 'AL', 'CompanyName': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'}, {'Symbol': 'AMN', 'CompanyName': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'CompanyName': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'AMT', 'CompanyName': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'}, {'Symbol': 'ARD', 'CompanyName': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': {'test_symbols': ['AAPL', 'MSFT', 'GOOGL', 'JPM', 'V']}, 'var_functions.query_db:32': [{'table_exists': 'True'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:40': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:42': {'total_symbols': 234, 'first_20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:44': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}], 'var_functions.execute_python:46': {'symbol': 'AIN', 'company': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'up_days': 2, 'down_days': 3, 'difference': -1}, 'var_functions.execute_python:48': {'total_symbols': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:50': {'checking_count': 30, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ']}, 'var_functions.execute_python:52': {'symbols_to_check': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ']}, 'var_functions.query_db:54': [], 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:58': {'batch_size': 20, 'batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'total_available': 234}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'total_nyse_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:66': {'total_symbols': 234, 'tracker_initialized': True, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.execute_python:70': {'symbol': 'AIV', 'up_days': 118, 'down_days': 128, 'neutral_days': 5, 'difference': -10}, 'var_functions.execute_python:72': {'total_symbols': 234, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC'], 'batch_size': 15}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.execute_python:76': {'ready_to_process': True, 'total_stocks': 234}, 'var_functions.execute_python:78': {'stock': 'AJRD', 'up_days': 123, 'down_days': 123, 'difference': 0, 'company': 'Aerojet Rocketdyne Holdings, Inc. specializes in d'}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.execute_python:82': {'stock': 'AL', 'up_days': 131, 'down_days': 117, 'difference': 14, 'company': 'Air Lease Corporation specializes in leasing comme'}, 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.execute_python:88': {'AMN': {'up': 134, 'down': 111, 'diff': 23}, 'tracker': {'top_stocks': [{'symbol': 'AMN', 'company': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'up_days': 134, 'down_days': 111, 'diff': 23}, {'symbol': 'AL', 'company': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'up_days': 131, 'down_days': 117, 'diff': 14}], 'min_diff': 14}, 'processed_count': 6}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:92': {'stock': 'AMT', 'up_days': 141, 'down_days': 110, 'difference': 31}, 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.execute_python:96': {'current_top_3': [{'symbol': 'AMT', 'diff': 31, 'company': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.', 'up': 141, 'down': 110}, {'symbol': 'AMN', 'diff': 23, 'company': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'up': 134, 'down': 111}, {'symbol': 'AL', 'diff': 14, 'company': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'up': 131, 'down': 117}], 'next_symbols': ['ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC']}}

exec(code, env_args)
