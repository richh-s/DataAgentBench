code = """import json
import os

# Load ETF symbols from NYSE Arca
etf_file = locals()['var_functions.query_db:2']
with open(etf_file, 'r') as f:
    etf_data = json.load(f)

etf_symbols = [item['Symbol'] for item in etf_data]

# Get list of all tables in stocktrade database
stocktrade_tables_file = locals()['var_functions.list_db:10']
with open(stocktrade_tables_file, 'r') as f:
    all_tables = json.load(f)

# Find which ETFs have trading data available
available_etfs = set(etf_symbols) & set(all_tables)
print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'etfs_with_trading_data': len(available_etfs)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Symbol': 'AAAU', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Symbol': 'AADR', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Symbol': 'ABEQ', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.'}, {'Symbol': 'ACSG', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'Xtrackers MSCI ACWI ex USA ESG Leaders Equity ETF offers investors an opportunity to engage with international companies that are recognized for their strong environmental, social, and governance practices, excluding those based in the USA.'}, {'Symbol': 'ACWF', 'Listing Exchange': 'P', 'ETF': 'Y', 'Company Description': 'iShares Edge MSCI Multifactor Global ETF is an investment fund that provides exposure to a diversified portfolio of stocks worldwide, utilizing a multifactor approach to enhance returns and manage risk.'}], 'var_functions.execute_python:8': {'count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:16': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.execute_python:8', 'var_functions.list_db:10', '__builtins__', 'json']}, 'var_functions.execute_python:18': {'count': 1435, 'first_5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}}

exec(code, env_args)
