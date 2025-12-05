code = """import json, pandas as pd

path = var_call_x8XqfuEaEJmdvwgwcztUv5Ci
with open(path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

select_stmts = []
for sym in etf_symbols:
    select_stmts.append("SELECT '" + sym + "' AS Symbol, Date, \"Adj Close\" FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200")

union_sql = " UNION ALL ".join(select_stmts)
final_sql = "SELECT DISTINCT Symbol FROM (" + union_sql + ");"

out = json.dumps({'sql': final_sql[:10000]})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_x8XqfuEaEJmdvwgwcztUv5Ci': 'file_storage/call_x8XqfuEaEJmdvwgwcztUv5Ci.json', 'var_call_zVJj06zwVA1qHoJ9cWWadphu': 'file_storage/call_zVJj06zwVA1qHoJ9cWWadphu.json'}

exec(code, env_args)
