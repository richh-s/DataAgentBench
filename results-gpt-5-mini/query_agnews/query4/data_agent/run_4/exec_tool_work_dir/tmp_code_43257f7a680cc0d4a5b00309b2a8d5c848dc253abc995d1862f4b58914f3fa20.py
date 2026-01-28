code = """import json
fp = var_call_Daa8lM9TAamUdd11DC7tAQtu
with open(fp, 'r') as f:
    data = json.load(f)
ids = [int(d['article_id']) for d in data]
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_Daa8lM9TAamUdd11DC7tAQtu': 'file_storage/call_Daa8lM9TAamUdd11DC7tAQtu.json'}

exec(code, env_args)
