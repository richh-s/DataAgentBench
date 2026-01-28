code = """import json
# Load the stored results files
with open(var_call_wyvLHbTah4xHBhQw3b1SWZIe, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_B2ru5dP1Xmg9M6pCqwM6R67c, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo (list of dicts with 'Symbol')
stockinfo_symbols = [rec['Symbol'] for rec in stockinfo]
# trade_tables is list of table names
# Compute intersection and sort
symbols_to_check = sorted(list(set(stockinfo_symbols).intersection(set(trade_tables))))
import json
print("__RESULT__:")
print(json.dumps(symbols_to_check))"""

env_args = {'var_call_wyvLHbTah4xHBhQw3b1SWZIe': 'file_storage/call_wyvLHbTah4xHBhQw3b1SWZIe.json', 'var_call_B2ru5dP1Xmg9M6pCqwM6R67c': 'file_storage/call_B2ru5dP1Xmg9M6pCqwM6R67c.json'}

exec(code, env_args)
