code = """import json
# load the two previous large results from storage file paths
with open(var_call_xtcHZxFlp2AioHUoeqxRk0n8, 'r') as f:
    stockinfo_rows = json.load(f)
with open(var_call_Eu1b0Hrj3zvFAG0mEuXaHaO3, 'r') as f:
    stocktrade_tables = json.load(f)
# extract symbols from stockinfo
symbols = [r['Symbol'] for r in stockinfo_rows]
# intersection with available tables in stocktrade_database
tables_set = set(stocktrade_tables)
intersection = sorted([s for s in symbols if s in tables_set])
# print result as JSON string
result = json.dumps(intersection)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_xtcHZxFlp2AioHUoeqxRk0n8': 'file_storage/call_xtcHZxFlp2AioHUoeqxRk0n8.json', 'var_call_Eu1b0Hrj3zvFAG0mEuXaHaO3': 'file_storage/call_Eu1b0Hrj3zvFAG0mEuXaHaO3.json'}

exec(code, env_args)
