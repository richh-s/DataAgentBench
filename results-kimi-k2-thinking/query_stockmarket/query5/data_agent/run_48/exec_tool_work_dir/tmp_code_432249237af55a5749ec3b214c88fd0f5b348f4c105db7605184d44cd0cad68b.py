code = """# Load the data
import json
ticker_var = locals()['var_functions.query_db:0']
if isinstance(ticker_var, str):
    with open(ticker_var, 'r') as f:
        ticker_list = json.load(f)
else:
    ticker_list = ticker_var

# Get tables
all_tables_var = locals()['var_functions.list_db:2']
if isinstance(all_tables_var, str):
    with open(all_tables_var, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_var

# Get NASDAQ Capital Market tickers
capital_market_tickers = [ticker['Symbol'] for ticker in ticker_list if ticker.get('Market Category') == 'S']
capital_tickers_set = set(capital_market_tickers)
all_tables_set = set(all_tables)

# Find intersection (tickers that have data tables)
available_tickers = list(capital_tickers_set & all_tables_set)
print('__RESULT__:')
print(json.dumps(f"Found {len(available_tickers)} NASDAQ Capital Market tickers with data tables"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': 'Found 86 NASDAQ Capital Market tickers', 'var_functions.execute_python:8': 'Found 2753 total tables in stocktrade_database'}

exec(code, env_args)
