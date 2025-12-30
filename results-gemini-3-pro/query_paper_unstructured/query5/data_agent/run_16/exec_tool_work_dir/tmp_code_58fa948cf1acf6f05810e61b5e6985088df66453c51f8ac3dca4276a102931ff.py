code = """import json
path = locals().get('var_function-call-1495859486444725251')
with open(path, 'r') as f:
    titles = json.load(f)

filenames = [t + ".txt" for t in titles]
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188}

exec(code, env_args)
