code = """import json
# Load storage variables created by previous tool calls
p1 = var_call_UM52fwnGjM9w8qHHmlixozgo
p2 = var_call_EIIjC7y9LrLLtIr5yfS5xcFp

with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)

# Build symbol list from stockinfo where Market Category S was already filtered in the previous query
symbols = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)

# Intersection
common = [s for s in symbols if s in trade_set]
# Build mapping symbol -> company description
mapping = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo if rec['Symbol'] in common}

out = {'symbols': common, 'mapping_sample_count': len(mapping)}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_UM52fwnGjM9w8qHHmlixozgo': 'file_storage/call_UM52fwnGjM9w8qHHmlixozgo.json', 'var_call_EIIjC7y9LrLLtIr5yfS5xcFp': 'file_storage/call_EIIjC7y9LrLLtIr5yfS5xcFp.json'}

exec(code, env_args)
