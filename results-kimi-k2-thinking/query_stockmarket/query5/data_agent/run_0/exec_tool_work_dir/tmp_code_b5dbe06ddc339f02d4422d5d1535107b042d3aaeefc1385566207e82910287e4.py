code = """import json
import pandas as pd

# Load NASDAQ Capital Market companies
companies_path = locals()['var_functions.query_db:24']
with open(companies_path, 'r') as f:
    nasdaq_cap_companies = json.load(f)

# Get available tickers
tickers_path = locals()['var_functions.list_db:26']
with open(tickers_path, 'r') as f:
    available_tickers = json.load(f)

# Map symbols to company names
symbol_to_name = {company['Symbol']: company['Company Description'] for company in nasdaq_cap_companies}

# Get list of symbols that have trade data
symbols = [sym for sym in symbol_to_name.keys() if sym in available_tickers]

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap': len(nasdaq_cap_companies),
    'with_trade_data': len(symbols),
    'sample_symbols': symbols[:5]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:14': 'file_storage/functions.list_db:14.json', 'var_functions.execute_python:18': 'Found 86 NASDAQ Capital companies, 86 have trade data', 'var_functions.execute_python:22': 'Found 86 capital market companies and 2753 total tickers', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.list_db:26': 'file_storage/functions.list_db:26.json', 'var_functions.query_db:28': [{'Date': '2019-01-02', 'Open': '39.59000015258789', 'High': '40.5099983215332', 'Low': '39.59000015258789', 'Close': '40.33000183105469', 'Adj Close': '40.0748176574707', 'Volume': '21100'}, {'Date': '2019-01-03', 'Open': '40.09999847412109', 'High': '40.2400016784668', 'Low': '39.7400016784668', 'Close': '39.880001068115234', 'Adj Close': '39.627662658691406', 'Volume': '37100'}, {'Date': '2019-01-04', 'Open': '40.34999847412109', 'High': '41.43000030517578', 'Low': '40.040000915527344', 'Close': '41.43000030517578', 'Adj Close': '41.16785430908203', 'Volume': '28400'}, {'Date': '2019-01-07', 'Open': '41.720001220703125', 'High': '42.06999969482422', 'Low': '41.54999923706055', 'Close': '41.91999816894531', 'Adj Close': '41.65475082397461', 'Volume': '17700'}, {'Date': '2019-01-08', 'Open': '42.20000076293945', 'High': '42.290000915527344', 'Low': '41.77999877929688', 'Close': '42.209999084472656', 'Adj Close': '41.94291687011719', 'Volume': '22300'}], 'var_functions.execute_python:30': 'NASDAQ Capital companies: 86, Available tickers: 2753', 'var_functions.query_db:32': [{'count': '13'}], 'var_functions.execute_python:34': 'Analyzing 86 companies'}

exec(code, env_args)
