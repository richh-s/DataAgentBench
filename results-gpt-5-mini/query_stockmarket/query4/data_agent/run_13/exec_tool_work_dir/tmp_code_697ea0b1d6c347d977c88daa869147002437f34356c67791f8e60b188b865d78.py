code = """import json
# Load previous tool results from storage file paths
with open(var_call_Zch6f3xWajnrHg8UxUqfGx5y, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_YyTI2DqlV8KmfJTSLERIkxKH, 'r') as f:
    trade_tables = json.load(f)

# Extract NYSE non-ETF symbols from stockinfo
nyse_symbols = [rec['Symbol'] for rec in stockinfo]
# trade_tables is list of table names
# Compute intersection (symbols present as tables)
symbols_to_query = sorted([s for s in nyse_symbols if s in trade_tables])

result = json.dumps(symbols_to_query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Zch6f3xWajnrHg8UxUqfGx5y': 'file_storage/call_Zch6f3xWajnrHg8UxUqfGx5y.json', 'var_call_YyTI2DqlV8KmfJTSLERIkxKH': 'file_storage/call_YyTI2DqlV8KmfJTSLERIkxKH.json'}

exec(code, env_args)
