code = """import json
# var_call_tIp3uAHrqYsL9oZ7Zyo00Eyv and var_call_F8SrY8Nb3ckIzQWbP6D1vZEC are available in storage
with open(var_call_tIp3uAHrqYsL9oZ7Zyo00Eyv, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_F8SrY8Nb3ckIzQWbP6D1vZEC, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo records
stockinfo_symbols = [r['Symbol'] for r in stockinfo_records]
# trade_tables is list of table names
# Compute intersection and sort
symbols_to_check = sorted(list(set(stockinfo_symbols).intersection(set(trade_tables))))

import json
print('__RESULT__:')
print(json.dumps(symbols_to_check))"""

env_args = {'var_call_tIp3uAHrqYsL9oZ7Zyo00Eyv': 'file_storage/call_tIp3uAHrqYsL9oZ7Zyo00Eyv.json', 'var_call_F8SrY8Nb3ckIzQWbP6D1vZEC': 'file_storage/call_F8SrY8Nb3ckIzQWbP6D1vZEC.json'}

exec(code, env_args)
