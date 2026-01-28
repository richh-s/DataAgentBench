code = """import json
path = var_call_Xnnh54iL6cs5wg7PT2JhApXO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
count = len(docs)
print("__RESULT__:")
print(json.dumps({"doc_count": count}))"""

env_args = {'var_call_Xnnh54iL6cs5wg7PT2JhApXO': 'file_storage/call_Xnnh54iL6cs5wg7PT2JhApXO.json'}

exec(code, env_args)
