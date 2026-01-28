code = """import json
# var_call_JgVdZ5lPpvNbcr53P85FVhko and var_call_pg5PrTVxGV9a7THHNxzy7odL are file paths to JSON results
with open(var_call_JgVdZ5lPpvNbcr53P85FVhko, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_pg5PrTVxGV9a7THHNxzy7odL, 'r') as f:
    trade_tables = json.load(f)

# trade_tables is a list of table names
trade_set = set(trade_tables)
# Filter stockinfo symbols to those present in trade_tables
matched = [r for r in stockinfo if r['Symbol'] in trade_set]
# Prepare a mapping symbol -> company name (Company Description contains name and description; extract the name as the first token before ' is ' or maybe first up to ' Inc' or common patterns are varied. For safety, keep full Company Description as name.
results = matched

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json'}

exec(code, env_args)
