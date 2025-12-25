code = """import json

with open(locals()['var_function-call-11996756743093828097'], 'r') as f:
    data = json.load(f)
    ids = data['ids']
    print("__RESULT__:")
    print(json.dumps({"min": min(ids), "max": max(ids), "count": len(ids)}))"""

env_args = {'var_function-call-4087601676422552917': ['authors', 'article_metadata'], 'var_function-call-4087601676422553258': ['articles'], 'var_function-call-16836183799483844241': 'file_storage/function-call-16836183799483844241.json', 'var_function-call-11996756743093828097': 'file_storage/function-call-11996756743093828097.json'}

exec(code, env_args)
