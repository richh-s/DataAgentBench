code = """import json, pandas as pd
from datetime import datetime

path = var_call_uK0LOP2BYTp8Wc7MrVew6W5o
with open(path, 'r') as f:
    etf_symbols = [r['Symbol'] for r in json.load(f)]

# limit to those that also exist in stocktrade_database tables
trade_tables = set(var_call_QyIk6SYF8XpXk78zda42DnDu)
symbols = [s for s in etf_symbols if s in trade_tables]

chunks = []
for sym in symbols:
    q = f'SELECT "Symbol" as ticker, MAX("Adj Close") as max_adj_close_2015 FROM "{sym}" WHERE CAST(Date AS DATE) BETWEEN DATE(\'2015-01-01\') AND DATE(\'2015-12-31\');'
    chunks.append({'sym': sym, 'query': q})

# We'll just output the prepared queries; execution must be done by the main agent
result = json.dumps(chunks[:50])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_uK0LOP2BYTp8Wc7MrVew6W5o': 'file_storage/call_uK0LOP2BYTp8Wc7MrVew6W5o.json', 'var_call_QyIk6SYF8XpXk78zda42DnDu': 'file_storage/call_QyIk6SYF8XpXk78zda42DnDu.json'}

exec(code, env_args)
