code = """import json
p = var_call_ms1IPeXScrnLDnXJ5N74c2Gg
with open(p, 'r') as f:
    records = json.load(f)
ids = sorted({int(r['article_id']) for r in records})
# create batches of size 200
batches = [ids[i:i+200] for i in range(0, len(ids), 200)]
print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_call_ms1IPeXScrnLDnXJ5N74c2Gg': 'file_storage/call_ms1IPeXScrnLDnXJ5N74c2Gg.json', 'var_call_SjyJ9WSWLyyxJHx7WHzW2nIu': 'file_storage/call_SjyJ9WSWLyyxJHx7WHzW2nIu.json'}

exec(code, env_args)
