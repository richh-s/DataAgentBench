code = """import json

file_path = locals()['var_function-call-14136390404799655173']
with open(file_path, 'r') as f:
    filenames = json.load(f)

# Construct MongoDB query
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-14272256085625645601': 'file_storage/function-call-14272256085625645601.json', 'var_function-call-14136390404799655173': 'file_storage/function-call-14136390404799655173.json'}

exec(code, env_args)
