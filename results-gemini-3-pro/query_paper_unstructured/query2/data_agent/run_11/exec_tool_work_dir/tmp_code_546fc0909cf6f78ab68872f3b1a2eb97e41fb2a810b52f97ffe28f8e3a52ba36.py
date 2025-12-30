code = """import json

file_path = locals()['var_function-call-17219727327219922543']
with open(file_path, 'r') as f:
    filenames = json.load(f)

batch1 = filenames[:80]
query1 = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch1}
    }
}
print("__RESULT__:")
print(json.dumps(query1))"""

env_args = {'var_function-call-1413150651152435569': 'file_storage/function-call-1413150651152435569.json', 'var_function-call-17219727327219922543': 'file_storage/function-call-17219727327219922543.json', 'var_function-call-11336605744931727696': 158, 'var_function-call-6187342808786642302': 14080}

exec(code, env_args)
