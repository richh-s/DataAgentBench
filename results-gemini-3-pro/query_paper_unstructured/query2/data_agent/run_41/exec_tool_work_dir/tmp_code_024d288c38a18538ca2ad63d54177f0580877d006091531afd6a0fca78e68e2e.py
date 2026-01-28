code = """import json

with open(locals()['var_function-call-4679604093615905091'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]
query = {"filename": {"$in": filenames}}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4679604093615905091': 'file_storage/function-call-4679604093615905091.json', 'var_function-call-14123313604899525614': 158}

exec(code, env_args)
