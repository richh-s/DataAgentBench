code = """import json, os

# Read the NYSE non-ETF stocks file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps(symbols[:10]))  # Print first 10 as preview"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AAAU', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Symbol': 'AADR', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Symbol': 'AAME', 'Listing Exchange': 'Q', 'ETF': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'ETF': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'ETF': 'Y', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
