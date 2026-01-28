code = """import json
# Load the previous tool results from files whose paths are provided in variables
p1 = var_call_WYj9pogZCYTcEDnv54U6hRxc
p2 = var_call_ftMABduYO756PjQlNZ6OYSdL
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    tables = json.load(f)
# Extract symbols from stockinfo (already filtered for Listing Exchange N and non-ETF in the earlier query)
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# Intersect with tables present in stocktrade_database
set_tables = set(tables)
symbols_in_both = sorted([s for s in symbols_stockinfo if s in set_tables])
# Output the list
import json
print("__RESULT__:")
print(json.dumps(symbols_in_both))"""

env_args = {'var_call_WYj9pogZCYTcEDnv54U6hRxc': 'file_storage/call_WYj9pogZCYTcEDnv54U6hRxc.json', 'var_call_ftMABduYO756PjQlNZ6OYSdL': 'file_storage/call_ftMABduYO756PjQlNZ6OYSdL.json'}

exec(code, env_args)
