code = """import json

with open(locals()['var_function-call-9592996467849275882'], 'r') as f:
    citations_data = json.load(f)

filenames = [item['title'] + ".txt" for item in citations_data]
query = {"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-9592996467849275882': 'file_storage/function-call-9592996467849275882.json', 'var_function-call-8827078559982422440': 'file_storage/function-call-8827078559982422440.json', 'var_function-call-2196265177759855413': 188}

exec(code, env_args)
