code = """import json

# Load the full query string
with open(locals()['var_function-call-13901570492172126839'], 'r') as f:
    full_query = json.load(f)

# The full_query is a single string "SELECT ... UNION ALL ...".
# Split by " UNION ALL "
queries = full_query.split(" UNION ALL ")

# Batch them
batch_size = 50
batches = []
for i in range(0, len(queries), batch_size):
    batch_q = " UNION ALL ".join(queries[i:i+batch_size])
    batches.append(batch_q)

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-8629880559091051052': 'file_storage/function-call-8629880559091051052.json', 'var_function-call-8629880559091050687': 'file_storage/function-call-8629880559091050687.json', 'var_function-call-1791396151003041946': 'file_storage/function-call-1791396151003041946.json', 'var_function-call-2330781380349541887': 'file_storage/function-call-2330781380349541887.json', 'var_function-call-13901570492172126839': 'file_storage/function-call-13901570492172126839.json'}

exec(code, env_args)
