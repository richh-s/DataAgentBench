code = """import json
# Load previous tool results from storage
with open(var_call_0yaHAZkfGrcaXHyke6o3ibIL, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_dKSpiYnifg74W8Lb0g48hfat, 'r') as f:
    trade_tables = json.load(f)

# Build mapping from Symbol to Company Description for market category S (already filtered by query)
symbol_to_name = {rec['Symbol']: rec.get('Company Description', '') for rec in stockinfo}

# Intersect with tables present in trade database
available_symbols = [s for s in symbol_to_name.keys() if s in trade_tables]
available_symbols_sorted = sorted(available_symbols)

out = {'symbols': available_symbols_sorted, 'mapping': {s: symbol_to_name[s] for s in available_symbols_sorted}}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0yaHAZkfGrcaXHyke6o3ibIL': 'file_storage/call_0yaHAZkfGrcaXHyke6o3ibIL.json', 'var_call_dKSpiYnifg74W8Lb0g48hfat': 'file_storage/call_dKSpiYnifg74W8Lb0g48hfat.json'}

exec(code, env_args)
