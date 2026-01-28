code = """import json
import os
# Read the list of tables from stocktrade_database
file_path = locals()['var_functions.list_db:2']
with open(file_path, 'r') as f:
    all_tables = json.load(f)
# Read NASDAQ Capital Market stocks
capital_market_file = locals()['var_functions.query_db:0']
with open(capital_market_file, 'r') as f:
    capital_market_stocks = json.load(f)

nasdaq_capital_tickers = {rec['Symbol'] for rec in capital_market_stocks}
existing_tickers = nasdaq_capital_tickers.intersection(all_tables)
print('__RESULT__:')
print(json.dumps({'total_nasdaq_capital': len(nasdaq_capital_tickers), 'existing_in_trade_db': len(existing_tickers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
