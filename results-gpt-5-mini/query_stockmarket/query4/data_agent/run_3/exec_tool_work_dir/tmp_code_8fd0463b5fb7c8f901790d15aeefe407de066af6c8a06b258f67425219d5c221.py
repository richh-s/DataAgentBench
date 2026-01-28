code = """import json
# Load the results from the previous tool calls. These variables contain file paths to JSON results.
path_stockinfo = var_call_30Q4bH3inArkxlM7dvrMi1ha
path_tables = var_call_u7zNvvdRWah3dEIyubxloJSI

with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

# Extract symbols from stockinfo results
symbols = [rec['Symbol'] for rec in stockinfo]
# Filter symbols that have a corresponding table in stocktrade_database
available_symbols = [s for s in symbols if s in tables]

# Build SQL by unioning per-symbol aggregates for 2017
selects = []
for s in available_symbols:
    sel = f"(SELECT '{s}' AS symbol, COALESCE(SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END),0) AS up_days, COALESCE(SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END),0) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31')"
    selects.append(sel)

if not selects:
    sql = "-- NO SYMBOLS AVAILABLE"
else:
    union = "\nUNION ALL\n".join(selects)
    sql = f"SELECT symbol, up_days, down_days FROM (\n{union}\n) AS t WHERE up_days > down_days ORDER BY up_days DESC LIMIT 5;"

import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_30Q4bH3inArkxlM7dvrMi1ha': 'file_storage/call_30Q4bH3inArkxlM7dvrMi1ha.json', 'var_call_u7zNvvdRWah3dEIyubxloJSI': 'file_storage/call_u7zNvvdRWah3dEIyubxloJSI.json'}

exec(code, env_args)
