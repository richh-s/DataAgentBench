code = """import json

# Load valid ETFs
etf_file_path = locals()['var_function-call-13542232815925124035']
with open(etf_file_path, 'r') as f:
    valid_etfs = json.load(f)

# Batch 1: 0 to 150
batch = valid_etfs[0:150]

query_parts = []
for sym in batch:
    # Use single quotes for python string
    # SQL: SELECT 'SYM' s FROM "SYM" WHERE "Adj Close">200 AND Date LIKE '2015%' LIMIT 1
    q = f'SELECT \'{sym}\' s FROM "{sym}" WHERE "Adj Close">200 AND Date LIKE \'2015%\' LIMIT 1'
    query_parts.append(q)

full_query = " UNION ALL ".join(query_parts)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-7475560093060171147': 'file_storage/function-call-7475560093060171147.json', 'var_function-call-11135752326348972247': 'file_storage/function-call-11135752326348972247.json', 'var_function-call-13542232815925124035': 'file_storage/function-call-13542232815925124035.json', 'var_function-call-7986853647983258996': 1435}

exec(code, env_args)
