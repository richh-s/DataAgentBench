code = """import json

# Get NYSE non-ETF stocks from query result
nyse_result = locals().get('var_functions.query_db:0')
if isinstance(nyse_result, str) and nyse_result.endswith('.json'):
    with open(nyse_result, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = nyse_result

# Create company description lookup
desc_lookup = {}
for stock in nyse_stocks:
    desc_lookup[stock['Symbol']] = stock['Company Description']

# Get available trade symbols
trade_tables = locals().get('var_functions.list_db:2')
if isinstance(trade_tables, str) and trade_tables.endswith('.json'):
    with open(trade_tables, 'r') as f:
        trade_symbols = json.load(f)
else:
    trade_symbols = trade_tables

trade_set = set(trade_symbols)

# Get common symbols only
common = []
for stock in nyse_stocks:
    sym = stock['Symbol']
    if sym in trade_set:
        common.append(sym)

print('Found', len(common), 'common symbols')

# Now we need to query 2017 data for each symbol
# Store them for batch processing
print('__RESULT__:')
print(json.dumps({'symbols': common, 'count': len(common), 'desc_lookup': desc_lookup}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_symbols_count': 234, 'common_symbols_count': 234, 'common_symbols_preview': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
