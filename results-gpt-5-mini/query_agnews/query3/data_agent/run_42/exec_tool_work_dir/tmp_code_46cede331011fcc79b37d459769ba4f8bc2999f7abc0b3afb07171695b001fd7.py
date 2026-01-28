code = """import json
# var_call_1PK3eT0GPz7pjC0XG76LYiBs is provided by the previous query_db call
data = None
if isinstance(var_call_1PK3eT0GPz7pjC0XG76LYiBs, str):
    with open(var_call_1PK3eT0GPz7pjC0XG76LYiBs, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = var_call_1PK3eT0GPz7pjC0XG76LYiBs

ids = sorted({int(rec['article_id']) for rec in data})

print('__RESULT__:')
print(json.dumps(ids))"""

env_args = {'var_call_1PK3eT0GPz7pjC0XG76LYiBs': 'file_storage/call_1PK3eT0GPz7pjC0XG76LYiBs.json'}

exec(code, env_args)
