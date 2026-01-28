code = """import json
path = var_call_4k9wroUinQQ9xAhohQ3PeNhb
with open(path, 'r') as f:
    data = json.load(f)
ids = sorted({int(item['article_id']) for item in data})
import json
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_4k9wroUinQQ9xAhohQ3PeNhb': 'file_storage/call_4k9wroUinQQ9xAhohQ3PeNhb.json'}

exec(code, env_args)
