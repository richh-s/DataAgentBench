code = """import json
# Load ETF symbols result from stockinfo query (stored as JSON list of dicts)
with open(var_call_OA5c55w6JsC8kjxHPlWH1BwK) as f:
    etf_records = json.load(f)
symbols = [r['Symbol'] for r in etf_records]
# Load list of tables in stocktrade_database
with open(var_call_H1CE2LVMDOMyJX0LZCSItIcn) as f:
    tables = json.load(f)
table_set = set(tables)
# Compute intersection: ETFs that have a table in stocktrade_database
common = [s for s in symbols if s in table_set]
# Build a single SQL that unions MAX("Adj Close") for 2015 per symbol
sql_parts = []
for s in common:
    # Some symbols may contain double quotes or single quotes; safe to wrap table name in double quotes and symbol literal in single quotes
    sql_parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
if sql_parts:
    sql = " UNION ALL ".join(sql_parts) + " ORDER BY symbol"
else:
    sql = ""
result = {"sql": sql, "symbols_count": len(common), "symbols": common}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EX7fJ1N82JvZuW4MmN0Y3kC2': ['stockinfo'], 'var_call_H1CE2LVMDOMyJX0LZCSItIcn': 'file_storage/call_H1CE2LVMDOMyJX0LZCSItIcn.json', 'var_call_OA5c55w6JsC8kjxHPlWH1BwK': 'file_storage/call_OA5c55w6JsC8kjxHPlWH1BwK.json'}

exec(code, env_args)
