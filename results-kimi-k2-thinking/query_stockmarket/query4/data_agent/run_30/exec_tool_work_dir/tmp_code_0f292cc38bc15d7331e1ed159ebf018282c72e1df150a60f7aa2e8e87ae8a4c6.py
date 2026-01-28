code = """import json

# vars are provided directly
all_tickers = json.loads(globals()['var_functions.list_db:0'])
nyse_records = json.loads(globals()['var_functions.query_db:2'])

nyse_tickers = {rec['Symbol'] for rec in nyse_records}

# Intersection (tickers that exist in stocktrade_database and are NYSE non-ETF)
valid_tickers = [t for t in all_tickers if t in nyse_tickers]

# Print valid tickers and count
print('__RESULT__:')
print(json.dumps(valid_tickers[:20], indent=2))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
