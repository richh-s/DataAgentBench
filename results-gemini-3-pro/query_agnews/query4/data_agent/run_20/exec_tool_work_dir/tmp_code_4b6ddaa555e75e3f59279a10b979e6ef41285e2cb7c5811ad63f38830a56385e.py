code = """import json

with open(locals()['var_function-call-121859605526448438'], 'r') as f:
    articles_2015 = json.load(f)

ids = [int(a['article_id']) for a in articles_2015]
print("__RESULT__:")
print(json.dumps({"count": len(ids), "ids": ids}))"""

env_args = {'var_function-call-121859605526448438': 'file_storage/function-call-121859605526448438.json'}

exec(code, env_args)
