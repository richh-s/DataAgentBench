code = """import json, pandas as pd
from datetime import datetime

# load ETF symbols file
path = var_call_2cjDNvC9giWrmceNmqUQJcDT
with open(path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# load all trade tables
trade_tables_path = var_call_bGYn6eRPnhi7YgDHKTt7REL1
with open(trade_tables_path, 'r') as f:
    all_tables = json.load(f)

# intersect to keep only ETF symbols that have a table
symbols = sorted(set(etf_symbols).intersection(set(all_tables)))

# we will build a DuckDB query that unions all relevant tables with condition
# but here we only prepare the symbol list and return it; the actual per-table query will be done via query_db tools

result = symbols

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2cjDNvC9giWrmceNmqUQJcDT': 'file_storage/call_2cjDNvC9giWrmceNmqUQJcDT.json', 'var_call_bGYn6eRPnhi7YgDHKTt7REL1': 'file_storage/call_bGYn6eRPnhi7YgDHKTt7REL1.json'}

exec(code, env_args)
