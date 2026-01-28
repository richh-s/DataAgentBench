code = """import json

# Load NYSE Arca ETFs from stockinfo query
nyse_arca_file = locals()['var_functions.query_db:0']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f) 

# Extract just the symbols
etf_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Load table list from stocktrade_database
table_list_file = locals()['var_functions.list_db:2']
with open(table_list_file, 'r') as f:
    all_tables = json.load(f)

# Find which ETF symbols have matching tables
common_symbols = set(etf_symbols) & set(all_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'total_tables_in_db': len(all_tables),
    'matching_symbols': len(common_symbols),
    'sample_symbols': list(common_symbols)[:10],
    'all_symbols_list': list(common_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'count': 1435, 'sample': [{'Symbol': 'AAAU', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Symbol': 'AADR', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Symbol': 'ABEQ', 'Company Description': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.'}, {'Symbol': 'ACSG', 'Company Description': 'Xtrackers MSCI ACWI ex USA ESG Leaders Equity ETF offers investors an opportunity to engage with international companies that are recognized for their strong environmental, social, and governance practices, excluding those based in the USA.'}, {'Symbol': 'ACWF', 'Company Description': 'iShares Edge MSCI Multifactor Global ETF is an investment fund that provides exposure to a diversified portfolio of stocks worldwide, utilizing a multifactor approach to enhance returns and manage risk.'}]}}

exec(code, env_args)
