code = """import json

# Read NYSE non-ETF stocks from SQLite
nyse_file = locals()['var_functions.query_db:5']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Read all ticker symbols from DuckDB (stocktrade_database)
all_tickers_file = locals()['var_functions.list_db:12']
with open(all_tickers_file, 'r') as f:
    all_tickers = json.load(f)

# Create mapping of symbol to company name
symbol_to_company = {s['Symbol']: s['Company Description'] for s in nyse_stocks}

# Find available NYSE stocks in the trade database
available_symbols = []
for ticker in all_tickers:
    if ticker in symbol_to_company:
        available_symbols.append(ticker)

print('__RESULT__:')
print(json.dumps({
    'total_available': len(available_symbols),
    'symbols': available_symbols
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_available': 234, 'sample_stocks': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}]}, 'var_functions.query_db:16': []}

exec(code, env_args)
