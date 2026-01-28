code = """import json
# Load the large results from prior query_db and list_db calls
with open(var_call_GMzb8liIAFgyaYUJnZrUCUPM, 'r') as f:
    stockinfo_rows = json.load(f)
with open(var_call_YZ5Xgzpbizwx61KMort8zyjY, 'r') as f:
    trade_tables = json.load(f)

# Extract NYSE non-ETF symbols from stockinfo result
symbols_stockinfo = [row['Symbol'] for row in stockinfo_rows]
# trade_tables is a list of available tables in stocktrade_database
symbols_in_trade = [s for s in trade_tables]

# Intersection
symbols_to_query = sorted(list(set(symbols_stockinfo) & set(symbols_in_trade)))

import json
print("__RESULT__:")
print(json.dumps(symbols_to_query))"""

env_args = {'var_call_GMzb8liIAFgyaYUJnZrUCUPM': 'file_storage/call_GMzb8liIAFgyaYUJnZrUCUPM.json', 'var_call_YZ5Xgzpbizwx61KMort8zyjY': 'file_storage/call_YZ5Xgzpbizwx61KMort8zyjY.json'}

exec(code, env_args)
