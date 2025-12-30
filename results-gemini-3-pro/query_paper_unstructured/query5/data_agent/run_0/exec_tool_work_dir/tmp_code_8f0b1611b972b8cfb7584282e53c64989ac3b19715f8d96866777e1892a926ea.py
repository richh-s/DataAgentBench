code = """import json

file_path = locals()['var_function-call-2532692775873089287']
with open(file_path, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

# Construct MongoDB query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2532692775873089287': 'file_storage/function-call-2532692775873089287.json', 'var_function-call-12942966211482027150': 188}

exec(code, env_args)
