code = """import json
path = var_call_GyTzqACDcvIV3zGDKVIrK555
with open(path, 'r') as f:
    records = json.load(f)
ids = []
for r in records:
    try:
        ids.append(int(r.get('article_id')))
    except:
        try:
            ids.append(int(r.get('article_id').strip()))
        except:
            pass
ids = sorted(list(set(ids)))
# create batches of size 500
batch_size = 500
batches = [ids[i:i+batch_size] for i in range(0, len(ids), batch_size)]
print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_call_GyTzqACDcvIV3zGDKVIrK555': 'file_storage/call_GyTzqACDcvIV3zGDKVIrK555.json', 'var_call_tGVA907GjKRDbTQyKyeuKl9d': 'file_storage/call_tGVA907GjKRDbTQyKyeuKl9d.json'}

exec(code, env_args)
