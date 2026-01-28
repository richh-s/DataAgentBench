code = """import json
import os
# Load NASDAQ Capital Market stocks
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    capital_market_stocks = json.load(f)
tickers = [rec['Symbol'] for rec in capital_market_stocks]
# Build query
parts = []
for ticker in tickers:
    parts.append(f"SELECT '{ticker}' as Symbol, COUNT(*) as cnt FROM \"{ticker}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND High > Low * 1.2")
query = " UNION ALL ".join(parts) + " ORDER BY cnt DESC LIMIT 5"
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:9': {'total_nasdaq_capital': 86, 'existing_in_trade_db': 86}}

exec(code, env_args)
