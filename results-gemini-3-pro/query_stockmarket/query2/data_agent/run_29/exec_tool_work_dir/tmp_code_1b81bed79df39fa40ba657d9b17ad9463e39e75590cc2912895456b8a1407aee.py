code = """import json

# Read stockinfo result
with open(locals()['var_function-call-2015005240419911970'], 'r') as f:
    stockinfo_data = json.load(f)

# Read stocktrade tables list
with open(locals()['var_function-call-3113271170216609049'], 'r') as f:
    stocktrade_tables = json.load(f)

stockinfo_symbols = set(item['Symbol'] for item in stockinfo_data)
stocktrade_tables_set = set(stocktrade_tables)

# Find intersection
relevant_symbols = list(stockinfo_symbols.intersection(stocktrade_tables_set))

print("__RESULT__:")
print(json.dumps(relevant_symbols))"""

env_args = {'var_function-call-3424898909852780043': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-2015005240419911970': 'file_storage/function-call-2015005240419911970.json', 'var_function-call-3113271170216609049': 'file_storage/function-call-3113271170216609049.json'}

exec(code, env_args)
