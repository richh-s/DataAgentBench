code = """import json
# load the results from previous query_db and list_db calls
# var_call_vjXSw3GgFSZmNZ3yUiZxY25q is a JSON file path
# var_call_HYFoZC2x6p6sNxHwwLnio59Y is a JSON file path
with open(var_call_vjXSw3GgFSZmNZ3yUiZxY25q, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_HYFoZC2x6p6sNxHwwLnio59Y, 'r') as f:
    trade_tables = json.load(f)
# extract symbols from stockinfo_records
stockinfo_symbols = [r['Symbol'] for r in stockinfo_records]
# compute intersection with trade_tables
trade_set = set(trade_tables)
symbols_to_query = [s for s in stockinfo_symbols if s in trade_set]
# sort for consistency
symbols_to_query = sorted(symbols_to_query)
import json
print("__RESULT__:")
print(json.dumps(symbols_to_query))"""

env_args = {'var_call_vjXSw3GgFSZmNZ3yUiZxY25q': 'file_storage/call_vjXSw3GgFSZmNZ3yUiZxY25q.json', 'var_call_HYFoZC2x6p6sNxHwwLnio59Y': 'file_storage/call_HYFoZC2x6p6sNxHwwLnio59Y.json'}

exec(code, env_args)
