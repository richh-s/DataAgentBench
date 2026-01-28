code = """import json
# Load the large results from previous query_db/list_db calls
# var_call_p4qT6DHsANC1fa3upzFJrE0u and var_call_COotKVsszDCRCxokKDd3YnYb are provided in storage
p = var_call_p4qT6DHsANC1fa3upzFJrE0u
t = var_call_COotKVsszDCRCxokKDd3YnYb

# p and t are file paths to JSON files (since results were large)
with open(p, 'r') as f:
    stockinfo = json.load(f)
with open(t, 'r') as f:
    tables = json.load(f)

# Extract symbols from stockinfo (already filtered to Listing Exchange = 'N' and non-ETF)
symbols = [r['Symbol'] for r in stockinfo]
# Intersect with tables present in stocktrade_database
tables_set = set(tables)
symbols_in_db = [s for s in symbols if s in tables_set]

# Output the list
out = {
    'symbols_to_check_count': len(symbols_in_db),
    'symbols_to_check': symbols_in_db
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_p4qT6DHsANC1fa3upzFJrE0u': 'file_storage/call_p4qT6DHsANC1fa3upzFJrE0u.json', 'var_call_COotKVsszDCRCxokKDd3YnYb': 'file_storage/call_COotKVsszDCRCxokKDd3YnYb.json'}

exec(code, env_args)
