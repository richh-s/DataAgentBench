code = """import json, pandas as pd
symbols_info = pd.read_json(var_call_1qc03ovFXaC9zij8dCb0GPkZ)
# get list of symbols
symbols = symbols_info['Symbol'].tolist()
# build duckdb query computing 2019 days with range>20% of low for each symbol table that exists
# but we don't know which tables exist efficiently here; intersect symbols with stocktrade list from file
import pathlib, ast
trade_syms = json.load(open(var_call_wtV7DWsuuIYFKfqEP3MGbneq))
trade_set = set(trade_syms)
use_syms = [s for s in symbols if s in trade_set]
# build a duckdb query using UNION ALL over existing tables
parts = []
for s in use_syms:
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS days FROM '{s}' WHERE substr(Date,1,4)='2019' AND (High-Low) > 0.2*Low")
union_query = " UNION ALL ".join(parts)
full_query = f"SELECT Symbol, SUM(days) AS days FROM ({union_query}) GROUP BY Symbol ORDER BY days DESC LIMIT 5;" if parts else "SELECT NULL as Symbol, 0 as days WHERE 0=1;"
result = {'duckdb_query': full_query}
res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_wtV7DWsuuIYFKfqEP3MGbneq': 'file_storage/call_wtV7DWsuuIYFKfqEP3MGbneq.json', 'var_call_1qc03ovFXaC9zij8dCb0GPkZ': 'file_storage/call_1qc03ovFXaC9zij8dCb0GPkZ.json', 'var_call_toLhbkRrGGwFp5ceCn1CZkdF': [{'1': '1'}]}

exec(code, env_args)
