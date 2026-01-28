code = """import json

# Read NYSE non-ETF stocks from stockinfo
nyse_file = locals()['var_functions.query_db:5']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Read all ticker symbols from stocktrade_database
all_tickers_file = locals()['var_functions.list_db:12']
with open(all_tickers_file, 'r') as f:
    all_tickers = json.load(f)

# Create a set of NYSE symbols for fast lookup
nyse_symbols = set([s['Symbol'] for s in nyse_stocks])

# Find intersection (NYSE stocks that have price data)
available_nyse_stocks = []
for ticker in all_tickers:
    if ticker in nyse_symbols:
        # Find the company description
        company_desc = next((s['Company Description'] for s in nyse_stocks if s['Symbol'] == ticker), '')
        available_nyse_stocks.append({
            'Symbol': ticker,
            'Company Description': company_desc
        })

print('__RESULT__:')
print(json.dumps({
    'total_available': len(available_nyse_stocks),
    'sample_stocks': available_nyse_stocks[:5]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)
