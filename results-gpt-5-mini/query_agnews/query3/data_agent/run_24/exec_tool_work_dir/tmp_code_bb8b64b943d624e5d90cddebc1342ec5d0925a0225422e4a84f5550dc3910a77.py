code = """import json
# var_call_ERF3gFj16azSSIJ8NVCzuylk is a file path to the metadata query result
path = var_call_ERF3gFj16azSSIJ8NVCzuylk
with open(path, 'r') as f:
    records = json.load(f)

article_ids = []
year_map = {}
for r in records:
    aid = int(r['article_id'])
    article_ids.append(aid)
    year = int(r['publication_date'][:4])
    year_map[str(aid)] = year

# ensure unique article_ids
article_ids = sorted(list(set(article_ids)))

out = {'article_ids': article_ids, 'year_map': year_map}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ERF3gFj16azSSIJ8NVCzuylk': 'file_storage/call_ERF3gFj16azSSIJ8NVCzuylk.json'}

exec(code, env_args)
