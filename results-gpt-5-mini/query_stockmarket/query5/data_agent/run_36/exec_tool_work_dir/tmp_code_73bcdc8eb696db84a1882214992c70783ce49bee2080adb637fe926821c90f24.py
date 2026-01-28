code = """import json
# var_call_gd5CWdzsZx0rDOMd65g9c3aG and var_call_QzqB9vLpeuskhuikHIbwl4Zy are provided in storage
p1 = var_call_gd5CWdzsZx0rDOMd65g9c3aG
p2 = var_call_QzqB9vLpeuskhuikHIbwl4Zy
with open(p1, 'r') as f:
    data1 = json.load(f)
with open(p2, 'r') as f:
    data2 = json.load(f)
# Extract symbols from stockinfo results
symbols_stockinfo = [r['Symbol'] for r in data1]
# data2 is list of table names
tables = data2
# Intersection
symbols = sorted(list(set(symbols_stockinfo).intersection(set(tables))))
# Output JSON
out = json.dumps(symbols)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gd5CWdzsZx0rDOMd65g9c3aG': 'file_storage/call_gd5CWdzsZx0rDOMd65g9c3aG.json', 'var_call_QzqB9vLpeuskhuikHIbwl4Zy': 'file_storage/call_QzqB9vLpeuskhuikHIbwl4Zy.json'}

exec(code, env_args)
