code = """import json

# Define the keys
nyse_arca_key = 'var_functions.query_db:0'
list_db_key = 'var_functions.list_db:2'

# Load the data from storage
with open(locals()[nyse_arca_key], 'r') as f:
    nyse_arca_etfs = json.load(f)

with open(locals()[list_db_key], 'r') as f:
    available_tickers = json.load(f)

# Get the set of NYSE Arca ETF symbols
nyse_arca_symbols = set(etf['Symbol'] for etf in nyse_arca_etfs)

# Find intersection with available tickers
available_symbols_set = set(available_tickers)
common_symbols = nyse_arca_symbols.intersection(available_symbols_set)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_available_tickers': len(available_symbols_set),
    'common_symbols_count': len(common_symbols),
    'sample_common_symbols': list(common_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:12': {'file1': 'file_storage/functions.query_db:0.json', 'file2': 'file_storage/functions.list_db:2.json'}, 'var_functions.execute_python:14': {'nyse_arca_etfs_count': 1435, 'available_tickers_count': 2753, 'sample_etfs': [{'Symbol': 'AAAU', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Symbol': 'AADR', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Symbol': 'ABEQ', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.'}, {'Symbol': 'ACSG', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Xtrackers MSCI ACWI ex USA ESG Leaders Equity ETF offers investors an opportunity to engage with international companies that are recognized for their strong environmental, social, and governance practices, excluding those based in the USA.'}, {'Symbol': 'ACWF', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'iShares Edge MSCI Multifactor Global ETF is an investment fund that provides exposure to a diversified portfolio of stocks worldwide, utilizing a multifactor approach to enhance returns and manage risk.'}], 'sample_tickers': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}}

exec(code, env_args)
