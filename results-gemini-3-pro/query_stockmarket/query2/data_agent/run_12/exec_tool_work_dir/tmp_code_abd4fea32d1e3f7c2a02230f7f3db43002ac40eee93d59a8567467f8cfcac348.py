code = """import json

path1 = locals()['var_function-call-13379061347181110174']
with open(path1, 'r') as f:
    etf_list = json.load(f)

etf_symbols = set(item['Symbol'] for item in etf_list)

path2 = locals()['var_function-call-6559325847238713717']
with open(path2, 'r') as f:
    trade_tables = set(json.load(f))

valid_symbols = sorted(list(etf_symbols.intersection(trade_tables)))

queries = []
chunk_size = 50
current_chunk = []

for sym in valid_symbols:
    # Construct subquery
    subq = 'SELECT \'' + sym + '\' as Symbol FROM "' + sym + '" WHERE "Adj Close" > 200 AND Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' LIMIT 1'
    current_chunk.append(subq)
    
    if len(current_chunk) >= chunk_size:
        queries.append(" UNION ALL ".join(current_chunk))
        current_chunk = []

if current_chunk:
    queries.append(" UNION ALL ".join(current_chunk))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "queries": queries}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json'}

exec(code, env_args)
