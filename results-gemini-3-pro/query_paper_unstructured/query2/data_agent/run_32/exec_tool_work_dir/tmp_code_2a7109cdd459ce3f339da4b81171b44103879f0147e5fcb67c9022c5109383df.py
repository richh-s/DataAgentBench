code = """import json

file_path = locals()['var_function-call-13725744379955539795']
with open(file_path, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

# Construct the Mongo query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-13725744379955539795': 'file_storage/function-call-13725744379955539795.json', 'var_function-call-16281852908939748059': 158}

exec(code, env_args)
