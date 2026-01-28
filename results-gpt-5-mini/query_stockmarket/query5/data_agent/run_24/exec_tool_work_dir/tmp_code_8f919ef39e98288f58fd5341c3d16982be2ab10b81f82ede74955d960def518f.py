code = """import json
# Load the previously stored query results from files
with open(var_call_WiFsL400Q5C19G4M4JJKzxhC, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_cXskrnIrtkwOykVNMFdjtQuT, 'r') as f:
    trade_tables = json.load(f)

# Build mapping for Market Category 'S' entries from stockinfo (already filtered by query)
symbols = []
sym_to_name = {}
for row in stockinfo:
    sym = row.get('Symbol')
    name = row.get('Company Description')
    if sym:
        sym = sym.strip()
        sym_to_name[sym] = name
        symbols.append(sym)

# Intersect with available trade tables
available = set(trade_tables)
symbols_to_query = [s for s in symbols if s in available]

# Output a JSON with symbols_to_query and mapping sym_to_name for those symbols
out = {'symbols': symbols_to_query, 'names': {s: sym_to_name[s] for s in symbols_to_query}}

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WiFsL400Q5C19G4M4JJKzxhC': 'file_storage/call_WiFsL400Q5C19G4M4JJKzxhC.json', 'var_call_cXskrnIrtkwOykVNMFdjtQuT': 'file_storage/call_cXskrnIrtkwOykVNMFdjtQuT.json'}

exec(code, env_args)
