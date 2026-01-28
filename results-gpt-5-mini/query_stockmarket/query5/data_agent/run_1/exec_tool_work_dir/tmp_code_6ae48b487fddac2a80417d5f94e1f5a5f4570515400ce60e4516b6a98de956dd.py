code = """import json
# load the two previous tool results from storage
path_stockinfo = var_call_h4lURv0gsFsNbbGeJpA93oUb
path_tables = var_call_wrrVFEISzbCFFa5DhbWeDDsL

with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

# Build mapping of symbols to company description for Market Category 'S' (already filtered by query)
sym_to_name = {rec['Symbol']: rec.get('Company Description', '') for rec in stockinfo}
symbols = list(sym_to_name.keys())

# Intersect with available tables in stocktrade_database
available = [s for s in symbols if s in tables]

output = {'symbols': available, 'sym_to_name': sym_to_name}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_h4lURv0gsFsNbbGeJpA93oUb': 'file_storage/call_h4lURv0gsFsNbbGeJpA93oUb.json', 'var_call_wrrVFEISzbCFFa5DhbWeDDsL': 'file_storage/call_wrrVFEISzbCFFa5DhbWeDDsL.json'}

exec(code, env_args)
