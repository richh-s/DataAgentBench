code = """import json
# Load the result from the first query
ticker_var = locals()['var_functions.query_db:0']
if isinstance(ticker_var, str):
    with open(ticker_var, 'r') as f:
        ticker_list = json.load(f)
else:
    ticker_list = ticker_var

# Filter for Market Category 'S' (NASDAQ Capital Market)
capital_market_tickers = [ticker for ticker in ticker_list if ticker.get('Market Category') == 'S']
print('__RESULT__:')
print(json.dumps(f"Found {len(capital_market_tickers)} NASDAQ Capital Market tickers"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
