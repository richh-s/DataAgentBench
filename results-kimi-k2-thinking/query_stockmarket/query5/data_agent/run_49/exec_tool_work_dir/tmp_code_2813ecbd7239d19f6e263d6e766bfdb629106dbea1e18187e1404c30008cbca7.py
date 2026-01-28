code = """import json
import os
# Read NASDAQ Capital Market stocks
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    capital_market_stocks = json.load(f)
tickers = [rec['Symbol'] for rec in capital_market_stocks]
# Build a UNION ALL query
subqueries = []
for ticker in tickers:
    subquery = f"SELECT '{ticker}' as Symbol, COUNT(*) as cnt FROM \"{ticker}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND \"High\" > 1.2 * \"Low\""
    subqueries.append(subquery)
full_query = "\nUNION ALL\n".join(subqueries) + ";"
print('__RESULT__:')
print(json.dumps({'query': full_query}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:9': {'total_nasdaq_capital': 86, 'existing_in_trade_db': 86}}

exec(code, env_args)
