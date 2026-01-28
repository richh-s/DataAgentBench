code = """import json
file_path = locals()['var_function-call-6474308532486273444']
with open(file_path, 'r') as f:
    filenames = json.load(f)

query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": {"$substr": ["$text", 0, 3000]}}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4970464269223372421': 'file_storage/function-call-4970464269223372421.json', 'var_function-call-6474308532486273444': 'file_storage/function-call-6474308532486273444.json', 'var_function-call-8662636658253547831': 158}

exec(code, env_args)
