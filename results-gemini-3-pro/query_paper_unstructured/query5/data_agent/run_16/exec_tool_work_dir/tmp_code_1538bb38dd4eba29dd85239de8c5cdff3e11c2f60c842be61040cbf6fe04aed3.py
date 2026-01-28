code = """import json
path = locals().get('var_function-call-1495859486444725251')
with open(path, 'r') as f:
    titles = json.load(f)

filenames = [t + ".txt" for t in titles]
chunk_size = 100
chunks = [filenames[i:i + chunk_size] for i in range(0, len(filenames), chunk_size)]

queries = []
for chunk in chunks:
    q = {
        "collection": "paper_docs",
        "filter": {"filename": {"$in": chunk}},
        "projection": {"filename": 1, "text": 1}
    }
    queries.append(json.dumps(q))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188, 'var_function-call-15965521281973898392': 'file_storage/function-call-15965521281973898392.json'}

exec(code, env_args)
