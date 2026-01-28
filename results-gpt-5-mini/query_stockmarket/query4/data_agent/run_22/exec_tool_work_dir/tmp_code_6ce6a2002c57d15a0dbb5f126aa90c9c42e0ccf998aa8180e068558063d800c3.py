code = """import json
# Load the stockinfo filtered results (stored in a JSON file path)
with open(var_call_QYmSJ4a5h1qX6ejjrb40amfT, 'r') as f:
    stockinfo_rows = json.load(f)
# Load the list of tables in stocktrade_database
with open(var_call_aQoeNw5nSqywRD7EjJP9yNGT, 'r') as f:
    trade_tables = json.load(f)

# Build set of symbols present in both
symbols_in_stockinfo = [r['Symbol'] for r in stockinfo_rows]
trade_set = set(trade_tables)
common_symbols = [s for s in symbols_in_stockinfo if s in trade_set]

# Also build a mapping symbol -> company description
sym_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo_rows if r['Symbol'] in common_symbols}

# Prepare output
out = {
    'common_symbols': common_symbols,
    'sym_to_name': sym_to_name,
    'n_common': len(common_symbols)
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_QYmSJ4a5h1qX6ejjrb40amfT': 'file_storage/call_QYmSJ4a5h1qX6ejjrb40amfT.json', 'var_call_aQoeNw5nSqywRD7EjJP9yNGT': 'file_storage/call_aQoeNw5nSqywRD7EjJP9yNGT.json'}

exec(code, env_args)
