code = """import json

# Load symbols from step 2
with open(locals()['var_function-call-9917169383885839858'], 'r') as f:
    stockinfo_results = json.load(f)
candidate_symbols = set(item['Symbol'] for item in stockinfo_results)

# Load tables from step 3
with open(locals()['var_function-call-12815242675246571232'], 'r') as f:
    trade_tables = json.load(f)
available_tables = set(trade_tables)

# Intersection
intersection = candidate_symbols.intersection(available_tables)

print("__RESULT__:")
print(json.dumps({"count": len(intersection), "sample": list(intersection)[:20]}))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json'}

exec(code, env_args)
