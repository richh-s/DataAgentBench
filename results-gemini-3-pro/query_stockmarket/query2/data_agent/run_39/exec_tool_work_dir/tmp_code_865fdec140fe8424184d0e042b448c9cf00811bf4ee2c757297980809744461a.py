code = """import json

# Get file paths from variables (using the correct key from previous step)
etfs_list_path = locals()['var_function-call-10141947115754413206']

with open(etfs_list_path, 'r') as f:
    data = json.load(f)
    etfs = data['etfs']

# Chunk size
chunk_size = 400
chunks = [etfs[i:i + chunk_size] for i in range(0, len(etfs), chunk_size)]

queries = []
for chunk in chunks:
    sub_queries = []
    for symbol in chunk:
        # Escape double quotes in symbol if any (unlikely for tickers but good practice)
        safe_symbol = symbol.replace('"', '""')
        # Construct sub-query
        q = f'SELECT \'{safe_symbol}\' as Symbol FROM "{safe_symbol}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3498236825446053099': 'file_storage/function-call-3498236825446053099.json', 'var_function-call-17765899317089105745': 'file_storage/function-call-17765899317089105745.json', 'var_function-call-10141947115754413206': 'file_storage/function-call-10141947115754413206.json'}

exec(code, env_args)
