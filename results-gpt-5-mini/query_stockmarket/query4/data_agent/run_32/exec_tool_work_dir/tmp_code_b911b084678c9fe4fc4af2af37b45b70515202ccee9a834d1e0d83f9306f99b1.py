code = """import json, pandas as pd
# Load the large JSON results from previous query_db and list_db calls
# var_call_uNASOINpJo7RJxYOhWWf6jxq and var_call_4vuFn1S6rFk4wZIUKabZGWyz are provided in storage
path_stockinfo = var_call_uNASOINpJo7RJxYOhWWf6jxq
path_tables = var_call_4vuFn1S6rFk4wZIUKabZGWyz

with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

# Build list of NYSE non-ETF symbols with company description
# stockinfo records have keys: Symbol, Company Description
nyse_non_etf = [r for r in stockinfo]

# Filter to symbols that exist as tables in stocktrade_database
tables_set = set(tables)
available = [ {"Symbol": r['Symbol'], "Name": r['Company Description']} for r in nyse_non_etf if r['Symbol'] in tables_set ]

# Output the list (may be long). We'll print as JSON string.
output = json.dumps(available)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_uNASOINpJo7RJxYOhWWf6jxq': 'file_storage/call_uNASOINpJo7RJxYOhWWf6jxq.json', 'var_call_4vuFn1S6rFk4wZIUKabZGWyz': 'file_storage/call_4vuFn1S6rFk4wZIUKabZGWyz.json'}

exec(code, env_args)
