code = """import json
p = var_call_uhQeRuiHYv64OeMnsHMjVwST
with open(p, 'r') as f:
    data = json.load(f)
ids = [int(d['article_id']) for d in data]
query_obj = {"collection": "articles", "filter": {"article_id": {"$in": ids}}, "projection": {"article_id": 1, "title": 1, "description": 1}}
query_str = json.dumps(query_obj)
print("__RESULT__:")
print(query_str)"""

env_args = {'var_call_uhQeRuiHYv64OeMnsHMjVwST': 'file_storage/call_uhQeRuiHYv64OeMnsHMjVwST.json'}

exec(code, env_args)
