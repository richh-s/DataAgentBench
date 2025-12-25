code = """import json

# Get file path
path = locals()['var_function-call-13818981913607902178']

# Load symbols
with open(path, 'r') as f:
    valid_symbols = json.load(f)

# Chunk size
chunk_size = 20
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

dq = chr(34) # double quote
sq = chr(39) # single quote

queries = []
for chunk in chunks:
    sub_queries = []
    for sym in chunk:
        q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date LIKE " + sq + "2015%" + sq + " LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("Generated " + str(len(queries)) + " queries.")
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-14799188465443802831': 'file_storage/function-call-14799188465443802831.json', 'var_function-call-8672756111804777550': 'file_storage/function-call-8672756111804777550.json', 'var_function-call-13818981913607902178': 'file_storage/function-call-13818981913607902178.json', 'var_function-call-4259646914698355504': 'file_storage/function-call-4259646914698355504.json', 'var_function-call-12839715956376139086': 8, 'var_function-call-3557291789943859589': 'file_storage/function-call-3557291789943859589.json'}

exec(code, env_args)
