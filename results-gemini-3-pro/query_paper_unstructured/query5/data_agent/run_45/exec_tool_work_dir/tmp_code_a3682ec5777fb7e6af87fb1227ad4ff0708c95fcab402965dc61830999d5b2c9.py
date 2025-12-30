code = """import json

with open(locals()['var_function-call-14637642351661620253'], 'r') as f:
    chunks = json.load(f)

query1 = {"collection": "paper_docs", "filter": {"filename": {"$in": chunks[0]}}}
print("__RESULT__:")
print(json.dumps(query1))"""

env_args = {'var_function-call-9592996467849275882': 'file_storage/function-call-9592996467849275882.json', 'var_function-call-8827078559982422440': 'file_storage/function-call-8827078559982422440.json', 'var_function-call-2196265177759855413': 188, 'var_function-call-10885420759070414019': 'file_storage/function-call-10885420759070414019.json', 'var_function-call-1623150383067545539': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5903998820821374632': 'file_storage/function-call-5903998820821374632.json', 'var_function-call-14637642351661620253': 'file_storage/function-call-14637642351661620253.json'}

exec(code, env_args)
