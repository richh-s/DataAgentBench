code = """import json

# Load full list of tickers from stocktrade_database
with open('var_functions.list_db:0', 'r') as f:
    # The result is a JSON string of a list of tickers
    all_tickers = json.load(f)

# Load NYSE non-ETF tickers from stockinfo query result
with open('var_functions.query_db:2', 'r') as f:
    nyse_records = json.load(f)

nyse_tickers = {rec['Symbol'] for rec in nyse_records}

# Intersection
intersection = [t for t in all_tickers if t in nyse_tickers]

# For debugging, let's count
print('__RESULT__:')
print(json.dumps({'all_tickers_count': len(all_tickers), 'nyse_count': len(nyse_tickers), 'intersection_count': len(intersection)}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
