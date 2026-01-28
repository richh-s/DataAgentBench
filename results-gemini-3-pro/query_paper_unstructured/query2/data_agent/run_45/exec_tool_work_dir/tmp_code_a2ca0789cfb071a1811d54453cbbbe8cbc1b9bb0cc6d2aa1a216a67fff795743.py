code = """import json

with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations = json.load(f)

titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158}

exec(code, env_args)
