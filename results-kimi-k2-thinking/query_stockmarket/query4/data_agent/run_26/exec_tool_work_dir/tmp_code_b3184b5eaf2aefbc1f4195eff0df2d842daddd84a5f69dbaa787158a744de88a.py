code = """import json

# Load all NYSE non-ETF stock data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
all_symbols = list(symbol_to_company.keys())

print('Total NYSE non-ETF stocks to analyze:', len(all_symbols))

# We need to query each stock for 2017 data
# Let's keep track of stocks with more up days than down days

# Starting with manual queries we've done so far:
# AIN: up_days=143, down_days=101 (more up)
# AIV: up_days=118, down_days=128 (more down)
# AEFC: no data for 2017
# AIZP: no data for 2017

# Results so far: {'AIN': {'up': 143, 'down': 101, 'company': '...'}}
results = {}

for item in stockinfo_data[:20]:
    symbol = item['Symbol']
    results[symbol] = {
        'up_days': None,
        'down_days': None,
        'company': item['Company Description']
    }

print('Prepared to track results for', len(results), 'symbols')
print('Sample:', list(results.keys())[:5])

result = {
    'status': 'setup_complete',
    'symbols_count': len(all_symbols),
    'results_keys': list(results.keys())[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_nyse_symbols': 234, 'available_tables': 234, 'sample_symbols': ['MTD', 'PAG', 'SMP', 'ESS', 'MKC']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'symbol_to_company_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.execute_python:30': {'total_stocks': 234, 'batch_size': 20, 'symbols_to_test': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:34': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}], 'var_functions.query_db:36': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}], 'var_functions.query_db:38': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}], 'var_functions.query_db:40': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0', 'total_days': '251'}], 'var_functions.execute_python:42': {'total_stocks': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:44': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0', 'total_days': '251'}], 'var_functions.query_db:46': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan', 'total_days': '0'}]}

exec(code, env_args)
