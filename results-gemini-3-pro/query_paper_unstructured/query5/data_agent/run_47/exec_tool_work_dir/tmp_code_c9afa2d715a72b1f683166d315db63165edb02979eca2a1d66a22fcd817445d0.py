code = """import json

# Load citations
path = locals()['var_function-call-11859459418229751864']
with open(path, 'r') as f:
    citations = json.load(f)

# Extract titles and create filenames
filenames = [c['title'] + ".txt" for c in citations]

# Construct query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print(f"Number of filenames: {len(filenames)}")
# Print the query as a JSON string
print("__RESULT__:")
print(json.dumps(json.dumps(query)))"""

env_args = {'var_function-call-11859459418229751864': 'file_storage/function-call-11859459418229751864.json', 'var_function-call-11859459418229752705': 'file_storage/function-call-11859459418229752705.json', 'var_function-call-3949769233705587424': 188, 'var_function-call-16819266969204168891': 'file_storage/function-call-16819266969204168891.json'}

exec(code, env_args)
