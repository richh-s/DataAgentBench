code = """import json

# Get the file path for filenames
file_path_filenames = locals()['var_function-call-13767594165860701791']
with open(file_path_filenames, 'r') as f:
    filenames = json.load(f)

# Construct the query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {
        "filename": 1,
        "text": 1
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json', 'var_function-call-13767594165860701791': 'file_storage/function-call-13767594165860701791.json'}

exec(code, env_args)
