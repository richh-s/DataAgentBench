code = """import json
p = var_call_aU6jDJSlzaDHjwOp7Q8SA18p
with open(p, 'r') as f:
    data = json.load(f)
article_ids = []
metadata = []
for d in data:
    try:
        aid = int(d['article_id'])
    except:
        aid = int(str(d['article_id']))
    article_ids.append(aid)
    metadata.append({'article_id': aid, 'region': d.get('region')})
out = {'article_ids': article_ids, 'metadata': metadata}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aU6jDJSlzaDHjwOp7Q8SA18p': 'file_storage/call_aU6jDJSlzaDHjwOp7Q8SA18p.json'}

exec(code, env_args)
