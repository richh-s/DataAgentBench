code = """import json

file_path = locals()['var_function-call-2515222159544851485']
with open(file_path, 'r') as f:
    data = json.load(f)

ids = [int(row['article_id']) for row in data]
print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids)}))"""

env_args = {'var_function-call-13208856365886244928': ['authors', 'article_metadata'], 'var_function-call-13208856365886244455': ['articles'], 'var_function-call-2515222159544851485': 'file_storage/function-call-2515222159544851485.json', 'var_function-call-13593231486142691637': 6696}

exec(code, env_args)
