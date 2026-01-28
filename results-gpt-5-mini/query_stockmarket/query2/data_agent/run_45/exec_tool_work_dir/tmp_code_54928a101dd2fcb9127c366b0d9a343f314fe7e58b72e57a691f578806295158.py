code = """import json
# var_call_Cqc50H7gOaxK4opWuAJHG9ou and var_call_sLwBJkaPyOb6PONpT7TKbMr9 are available in storage
with open(var_call_Cqc50H7gOaxK4opWuAJHG9ou, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_sLwBJkaPyOb6PONpT7TKbMr9, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo records
stockinfo_symbols = [r['Symbol'] for r in stockinfo]
# Intersection
trade_set = set(trade_tables)
candidates = sorted([s for s in stockinfo_symbols if s in trade_set])
# Return the candidate list as JSON string
result = json.dumps(candidates)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Cqc50H7gOaxK4opWuAJHG9ou': 'file_storage/call_Cqc50H7gOaxK4opWuAJHG9ou.json', 'var_call_sLwBJkaPyOb6PONpT7TKbMr9': 'file_storage/call_sLwBJkaPyOb6PONpT7TKbMr9.json'}

exec(code, env_args)
