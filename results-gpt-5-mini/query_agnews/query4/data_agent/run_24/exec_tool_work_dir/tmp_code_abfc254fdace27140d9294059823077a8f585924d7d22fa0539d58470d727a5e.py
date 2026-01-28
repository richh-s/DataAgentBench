code = """import json
p = var_call_89Uu7jc5r16mBnKwG8ZESekf
with open(p, 'r') as f:
    data = json.load(f)
article_ids = data['article_ids']
min_id = min(article_ids)
max_id = max(article_ids)
count = len(article_ids)
out = {'min_id': min_id, 'max_id': max_id, 'count': count}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aU6jDJSlzaDHjwOp7Q8SA18p': 'file_storage/call_aU6jDJSlzaDHjwOp7Q8SA18p.json', 'var_call_89Uu7jc5r16mBnKwG8ZESekf': 'file_storage/call_89Uu7jc5r16mBnKwG8ZESekf.json'}

exec(code, env_args)
