code = """import json
import os

# Load NYSE Arca ETF symbols
with open('file_storage/functions.query_db:16.json', 'r') as f:
    symbols_data = json.load(f)

symbols_list = [item['Symbol'] for item in symbols_data]
print(f"Total NYSE Arca ETFs: {len(symbols_list)}")

# First, let's check a sample of symbols to see what we're working with
sample_symbols = symbols_list[:10]
print(f"Sample symbols: {sample_symbols}")

# Get list of all tables from stocktrade_database
if os.path.exists('file_storage/functions.list_db:18.json'):
    with open('file_storage/functions.list_db:18.json', 'r') as f:
        all_tables = json.load(f)
else:
    print("Could not find stocktrade database listing")
    all_tables = []

print(f"Total tables in stocktrade database: {len(all_tables)}")

# Filter ETFs that actually have price data
available_tables = set(all_tables)
etf_symbols_with_data = [sym for sym in symbols_list if sym in available_tables]
print(f"NYSE Arca ETFs with price data: {len(etf_symbols_with_data)}")

print("__RESULT__:")
print(json.dumps({
    "total_nyse_arca_etfs": len(symbols_list),
    "sample_symbols": sample_symbols,
    "total_tables_in_stocktrade": len(all_tables),
    "nyse_arca_etfs_with_data": len(etf_symbols_with_data),
    "first_20_with_data": etf_symbols_with_data[:20]
}))"""

env_args = {'var_functions.query_db:0': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': 'file_storage/functions.list_db:4.json', 'var_functions.execute_python:10': {'type': "<class 'str'>", 'preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json'}

exec(code, env_args)
