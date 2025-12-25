code = """import json

# Get file paths
etf_file_path = locals()['var_function-call-689800581831186980']
tables_file_path = locals()['var_function-call-10272020244024100123']

# Load data
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_list)

with open(tables_file_path, 'r') as f:
    tables_list = json.load(f)
tables_set = set(tables_list)

common_symbols = sorted(list(etf_symbols.intersection(tables_set)))

# Create batches
batch_size = 300
batches = [common_symbols[i:i + batch_size] for i in range(0, len(common_symbols), batch_size)]

queries = []
for batch in batches:
    sub_queries = []
    for sym in batch:
        # distinct symbol
        q = f'SELECT \'{sym}\' as Symbol FROM "{sym}" WHERE "Date" LIKE \'2015-%\' AND "Adj Close" > 200 LIMIT 1'
        sub_queries.append(q)
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-689800581831186980': 'file_storage/function-call-689800581831186980.json', 'var_function-call-10272020244024100123': 'file_storage/function-call-10272020244024100123.json', 'var_function-call-13327904948754133498': 'file_storage/function-call-13327904948754133498.json'}

exec(code, env_args)
