code = """import json

# Load the filenames
with open(locals()['var_function-call-10586425159794830688'], 'r') as f:
    filenames = json.load(f)

# Construct the query
query = json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}})

print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-6443066931320893183': 'file_storage/function-call-6443066931320893183.json', 'var_function-call-10586425159794830688': 'file_storage/function-call-10586425159794830688.json', 'var_function-call-9524201379307901256': 'file_storage/function-call-9524201379307901256.json'}

exec(code, env_args)
