code = """import json
# Load the stored query and list results
with open(var_call_xf1CqCrETxw4srOCLJsEqvBu, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_BI6PtiEix9UAIXjgNIBnuqlT, 'r') as f:
    tables = json.load(f)

# Extract symbols from stockinfo (Market Category S non-ETF)
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# tables is a list of table names
# Compute intersection (case-sensitive)
set_tables = set(tables)
intersection = [s for s in symbols_stockinfo if s in set_tables]

# Sort for determinism
intersection_sorted = sorted(intersection)

import json
print("__RESULT__:")
print(json.dumps(intersection_sorted))"""

env_args = {'var_call_xf1CqCrETxw4srOCLJsEqvBu': 'file_storage/call_xf1CqCrETxw4srOCLJsEqvBu.json', 'var_call_BI6PtiEix9UAIXjgNIBnuqlT': 'file_storage/call_BI6PtiEix9UAIXjgNIBnuqlT.json'}

exec(code, env_args)
