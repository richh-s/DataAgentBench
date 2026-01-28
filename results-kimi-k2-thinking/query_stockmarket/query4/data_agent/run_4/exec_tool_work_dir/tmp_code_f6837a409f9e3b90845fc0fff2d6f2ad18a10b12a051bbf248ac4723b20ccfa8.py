code = """import json
import os

# Access the variable properly from locals
var_key = 'var_functions.query_db:24'
nyse_stocks_data = locals()[var_key]

# Check if it's a file path or already loaded data
if isinstance(nyse_stocks_data, str) and os.path.exists(nyse_stocks_data):
    with open(nyse_stocks_data, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = nyse_stocks_data

print(f"Loaded {len(nyse_stocks)} NYSE non-ETF stocks")
print("First 10 stocks:", nyse_stocks[:10])

# Extract just the symbols for further processing
symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Total symbols: {len(symbols)}")
print("Sample symbols:", symbols[:20])

# Store for later use
print("Done")

# Prepare the result for JSON output
result_json = json.dumps({
    'count': len(symbols),
    'symbols': symbols[:50]  # First 50 for preview
})

print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'ABEQ', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'ABMD', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'ABIOMED, Inc. specializes in developing advanced heart pumps to assist patients with severe cardiac conditions, playing a crucial role in modern cardiovascular care.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'ACAD', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': "ACADIA Pharmaceuticals Inc. is dedicated to developing treatments that improve the lives of patients with central nervous system disorders, focusing on innovative solutions for conditions like Parkinson's disease and schizophrenia."}, {'Nasdaq Traded': 'Y', 'Symbol': 'ACES', 'Listing Exchange': 'Z', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'ALPS Clean Energy ETF provides investors with access to a diverse portfolio of companies focused on renewable energy solutions, supporting the transition to a cleaner and more sustainable future.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'ACIO', 'Listing Exchange': 'Z', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'ETF Series Solutions Aptus Collared Income Opportunity ETF specializes in providing investors with a strategic approach to generating income through a unique blend of options strategies and equity investments, aimed at minimizing risk while maximizing potential returns.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:16': ['stockinfo'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}, {'Symbol': 'ARGD'}, {'Symbol': 'ARLO'}, {'Symbol': 'ASG'}, {'Symbol': 'AVA'}, {'Symbol': 'BANC'}, {'Symbol': 'BBU'}, {'Symbol': 'BBVA'}, {'Symbol': 'BDXA'}, {'Symbol': 'BKH'}, {'Symbol': 'BKT'}, {'Symbol': 'BLD'}, {'Symbol': 'BNS'}, {'Symbol': 'BV'}, {'Symbol': 'BZH'}, {'Symbol': 'CADE'}, {'Symbol': 'CAE'}, {'Symbol': 'CAF'}, {'Symbol': 'CBT'}, {'Symbol': 'CCC'}, {'Symbol': 'CCZ'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
