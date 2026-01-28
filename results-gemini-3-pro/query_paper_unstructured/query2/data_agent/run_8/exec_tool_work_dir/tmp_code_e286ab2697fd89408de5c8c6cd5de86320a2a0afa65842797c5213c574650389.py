code = """import json

# Read filenames from the previous result
file_path = locals()['var_function-call-15015239705628452412']
with open(file_path, 'r') as f:
    filenames = json.load(f)

# Construct the query dictionary
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

# Print as a JSON string
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158, 'var_function-call-15015239705628452412': 'file_storage/function-call-15015239705628452412.json'}

exec(code, env_args)
