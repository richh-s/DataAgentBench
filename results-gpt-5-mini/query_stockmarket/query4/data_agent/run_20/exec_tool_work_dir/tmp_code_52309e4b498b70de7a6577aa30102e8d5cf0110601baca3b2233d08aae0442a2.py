code = """import json
# Load the previous tool results which are stored as file paths in var_call_JlxE4BuJT5co98rQkeCxMO0k and var_call_XHd94ZK4eaI4ZdpusJOXlZv5
p1 = var_call_JlxE4BuJT5co98rQkeCxMO0k
p2 = var_call_XHd94ZK4eaI4ZdpusJOXlZv5

with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo result
symbols = [rec['Symbol'] for rec in stockinfo]
# Normalize trade_tables entries
trade_set = set(trade_tables)

# Intersection
intersection = [s for s in symbols if s in trade_set]

# Build mapping symbol -> company description
company_map = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}

output = {'symbols': intersection, 'company_map': company_map, 'count': len(intersection)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_XHd94ZK4eaI4ZdpusJOXlZv5': 'file_storage/call_XHd94ZK4eaI4ZdpusJOXlZv5.json', 'var_call_JlxE4BuJT5co98rQkeCxMO0k': 'file_storage/call_JlxE4BuJT5co98rQkeCxMO0k.json'}

exec(code, env_args)
