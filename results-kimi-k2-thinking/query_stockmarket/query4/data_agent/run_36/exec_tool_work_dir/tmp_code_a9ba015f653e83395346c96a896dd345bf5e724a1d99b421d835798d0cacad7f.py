code = """import json
import os

# Get the path to the NYSE stocks file
nyse_file_path = locals()['var_functions.query_db:8']

# Read NYSE stocks data
with open(nyse_file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
symbols = list(symbol_to_company.keys())

# Prepare result structure
detailed_results = []
error_symbols = []

print('__RESULT__:')
print(json.dumps({
    'message': f'Prepared to analyze {len(symbols)} NYSE non-ETF stocks',
    'sample_symbols': symbols[:10],
    'total_stocks': len(symbols)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AAAU', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Symbol': 'AADR', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Symbol': 'AAME', 'Listing Exchange': 'Q', 'ETF': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'ETF': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'ETF': 'Y', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'var_functions.list_db:14': 'file_storage/functions.list_db:14.json', 'var_functions.execute_python:16': {'total_nyse_stocks': 234, 'stocks_with_data': 234, 'sample_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:18': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2019-10-24'}, {'Date': '2019-10-25'}, {'Date': '2019-10-28'}, {'Date': '2019-10-29'}, {'Date': '2019-10-30'}, {'Date': '2019-10-31'}, {'Date': '2019-11-01'}, {'Date': '2019-11-04'}, {'Date': '2019-11-05'}, {'Date': '2019-11-06'}], 'var_functions.query_db:24': [{'Date': '2004-06-23'}], 'var_functions.query_db:26': [{'Date': '2017-01-03', 'Open': '69.29000091552734', 'Close': '70.54000091552734'}, {'Date': '2017-01-04', 'Open': '71.08000183105469', 'Close': '72.80000305175781'}, {'Date': '2017-01-05', 'Open': '72.80999755859375', 'Close': '72.79000091552734'}, {'Date': '2017-01-06', 'Open': '72.88999938964844', 'Close': '73.80000305175781'}, {'Date': '2017-01-09', 'Open': '74.05000305175781', 'Close': '73.95999908447266'}, {'Date': '2017-01-10', 'Open': '74.12000274658203', 'Close': '73.9800033569336'}, {'Date': '2017-01-11', 'Open': '74.2699966430664', 'Close': '75.7699966430664'}, {'Date': '2017-01-12', 'Open': '75.16999816894531', 'Close': '75.20999908447266'}, {'Date': '2017-01-13', 'Open': '74.83999633789062', 'Close': '75.63999938964844'}, {'Date': '2017-01-17', 'Open': '75.30000305175781', 'Close': '75.0199966430664'}], 'var_functions.execute_python:28': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
