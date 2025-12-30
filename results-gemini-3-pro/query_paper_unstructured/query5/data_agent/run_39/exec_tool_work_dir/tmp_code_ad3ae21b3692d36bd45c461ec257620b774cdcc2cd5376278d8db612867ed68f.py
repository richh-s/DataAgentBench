code = """import json

with open(locals()['var_function-call-17814581391725884160'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-17814581391725884160': 'file_storage/function-call-17814581391725884160.json', 'var_function-call-15997468636264688610': 'file_storage/function-call-15997468636264688610.json', 'var_function-call-15604050048548700330': 188}

exec(code, env_args)
