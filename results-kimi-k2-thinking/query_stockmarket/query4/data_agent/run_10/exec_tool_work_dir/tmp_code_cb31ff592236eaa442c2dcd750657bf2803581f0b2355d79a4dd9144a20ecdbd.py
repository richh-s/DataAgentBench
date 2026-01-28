code = """import json

# Load all NYSE non-ETF stocks
nyse_stocks_file = locals()['var_functions.query_db:0']
with open(nyse_stocks_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create a dictionary mapping symbol to company name
stock_info = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    company_name = stock['Company Description'].split(',')[0].split('.')[0].split(' specializes')[0].split(' is')[0].strip()
    stock_info[symbol] = company_name

# We'll analyze all 234 stocks
symbols_to_analyze = list(stock_info.keys())

print('__RESULT__:')
print(json.dumps({
    'message': f'Prepared to analyze {len(symbols_to_analyze)} NYSE non-ETF stocks',
    'sample_symbols': symbols_to_analyze[:10],
    'sample_company_names': [stock_info[sym] for sym in symbols_to_analyze[:10]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:10': {'total_nyse_stocks': 234, 'total_available_tables': 2753, 'common_stocks_count': 234, 'sample_common_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:14': {'stocks_to_analyze': 234, 'sample_stocks': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant'], ['AJRD', 'Aerojet Rocketdyne Holdings'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc'], ['AMP', 'Ameriprise Financial'], ['AMT', 'American Tower Corporation'], ['ARD', 'Ardagh Group S']]}, 'var_functions.execute_python:16': {'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'count': 20}, 'var_functions.query_db:18': [], 'var_functions.query_db:20': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}, {'Date': '2017-01-10', 'Open': '45.5', 'High': '45.95000076293945', 'Low': '45.5', 'Close': '45.70000076293945', 'Adj Close': '43.9408073425293', 'Volume': '161700'}, {'Date': '2017-01-11', 'Open': '45.79999923706055', 'High': '46.650001525878906', 'Low': '45.54999923706055', 'Close': '46.29999923706055', 'Adj Close': '44.51770782470703', 'Volume': '104600'}, {'Date': '2017-01-12', 'Open': '46.25', 'High': '46.25', 'Low': '45.0', 'Close': '45.75', 'Adj Close': '43.9888801574707', 'Volume': '59700'}, {'Date': '2017-01-13', 'Open': '46.04999923706055', 'High': '46.70000076293945', 'Low': '46.04999923706055', 'Close': '46.70000076293945', 'Adj Close': '44.90231704711914', 'Volume': '96900'}, {'Date': '2017-01-17', 'Open': '46.5', 'High': '46.75', 'Low': '46.20000076293945', 'Close': '46.650001525878906', 'Adj Close': '44.8542366027832', 'Volume': '111100'}], 'var_functions.query_db:22': [{'Date': '2017-01-03', 'Open': '113.12000274658205', 'High': '113.1999969482422', 'Low': '110.55999755859376', 'Close': '111.8499984741211', 'Adj Close': '103.10897827148438', 'Volume': '1029800'}, {'Date': '2017-01-04', 'Open': '112.66000366210938', 'High': '115.79000091552734', 'Low': '111.9800033569336', 'Close': '115.1999969482422', 'Adj Close': '106.19718170166016', 'Volume': '1523800'}, {'Date': '2017-01-05', 'Open': '114.26000213623048', 'High': '115.48999786376952', 'Low': '112.54000091552734', 'Close': '113.73999786376952', 'Adj Close': '104.85128021240234', 'Volume': '1491900'}, {'Date': '2017-01-06', 'Open': '114.62999725341795', 'High': '116.30999755859376', 'Low': '114.02999877929688', 'Close': '115.66000366210938', 'Adj Close': '106.6212387084961', 'Volume': '1463800'}, {'Date': '2017-01-09', 'Open': '116.12999725341795', 'High': '116.88999938964844', 'Low': '115.13999938964844', 'Close': '115.1999969482422', 'Adj Close': '106.19718170166016', 'Volume': '993900'}], 'var_functions.execute_python:24': {'total_stocks': 234, 'sample_stock_names': {'AEFC': 'Aegon Funding Company LLC', 'AIN': 'Albany International Corporation', 'AIV': 'Apartment Investment and Management Company', 'AIZP': 'Assurant', 'AJRD': 'Aerojet Rocketdyne Holdings', 'AL': 'Air Lease Corporation', 'AMN': 'AMN Healthcare Services Inc', 'AMP': 'Ameriprise Financial', 'AMT': 'American Tower Corporation', 'ARD': 'Ardagh Group S'}}}

exec(code, env_args)
