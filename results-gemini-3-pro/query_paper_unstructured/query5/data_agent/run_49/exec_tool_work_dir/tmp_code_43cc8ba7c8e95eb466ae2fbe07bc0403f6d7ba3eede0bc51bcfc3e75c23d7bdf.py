code = """import json

# Load filenames
with open(locals()['var_function-call-10586425159794830688'], 'r') as f:
    filenames = json.load(f)

# Split into chunks of 100
chunk_size = 100
chunks = [filenames[i:i + chunk_size] for i in range(0, len(filenames), chunk_size)]

# Prepare queries
queries = []
for chunk in chunks:
    queries.append(json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": chunk}}}))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-6443066931320893183': 'file_storage/function-call-6443066931320893183.json', 'var_function-call-10586425159794830688': 'file_storage/function-call-10586425159794830688.json', 'var_function-call-9524201379307901256': 'file_storage/function-call-9524201379307901256.json', 'var_function-call-16035171356852590914': 'file_storage/function-call-16035171356852590914.json', 'var_function-call-5146827579698456724': {'count': 5, 'missing': 184}}

exec(code, env_args)
