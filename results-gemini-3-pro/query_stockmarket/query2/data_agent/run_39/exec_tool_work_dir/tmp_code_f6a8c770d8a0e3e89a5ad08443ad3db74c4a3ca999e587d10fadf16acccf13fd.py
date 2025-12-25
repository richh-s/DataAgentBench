code = """import json

# Get file paths from variables
etfs_list_path = locals()['var_function-call-10141947115754413206']

with open(etfs_list_path, 'r') as f:
    data = json.load(f)
    etfs = data['etfs']

chunk_size = 400
queries = []

# Manual chunking
current_chunk = []
for i, symbol in enumerate(etfs):
    current_chunk.append(symbol)
    if len(current_chunk) == chunk_size or i == len(etfs) - 1:
        sub_queries = []
        for sym in current_chunk:
            # Create query string
            # SELECT 'SYM' as Symbol FROM "SYM" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND "Adj Close" > 200 LIMIT 1
            sq = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
            sub_queries.append(sq)
        
        full_query = " UNION ALL ".join(sub_queries)
        queries.append(full_query)
        current_chunk = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3498236825446053099': 'file_storage/function-call-3498236825446053099.json', 'var_function-call-17765899317089105745': 'file_storage/function-call-17765899317089105745.json', 'var_function-call-10141947115754413206': 'file_storage/function-call-10141947115754413206.json'}

exec(code, env_args)
