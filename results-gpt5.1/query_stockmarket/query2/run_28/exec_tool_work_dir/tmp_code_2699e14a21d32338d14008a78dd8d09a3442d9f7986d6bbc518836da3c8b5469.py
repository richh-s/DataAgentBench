code = """import json, pandas as pd
from datetime import datetime

# load etf symbols
path = var_call_INMjZwxTuggVM0UvElB2DSPD
with open(path) as f:
    etf_rows = json.load(f)
syms = [r['Symbol'] for r in etf_rows]

# filter to those that exist in stocktrade_database tables list
path2 = var_call_4Vk7HCYpFXCGm55S4w8dVQQP
with open(path2) as f:
    trade_tables = set(json.load(f))

syms = [s for s in syms if s in trade_tables]

# build queries for each symbol
queries = []
for s in syms:
    q = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM '{s}' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31';"
    queries.append(q)

# to avoid overly long single query, chunk them later in SQL if needed; for now just pass back
result = {"symbols": syms, "queries": queries[:5], "total_symbols": len(syms)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_INMjZwxTuggVM0UvElB2DSPD': 'file_storage/call_INMjZwxTuggVM0UvElB2DSPD.json', 'var_call_4Vk7HCYpFXCGm55S4w8dVQQP': 'file_storage/call_4Vk7HCYpFXCGm55S4w8dVQQP.json'}

exec(code, env_args)
