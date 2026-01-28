code = """import json
path = var_call_0BWhQ822FlEwjtXW5PCml263
with open(path, 'r') as f:
    records = json.load(f)
ids = sorted({int(rec['article_id']) for rec in records})
count = len(ids)
chunk_size = 200
chunks = [ids[i:i+chunk_size] for i in range(0, count, chunk_size)]
print('__RESULT__:')
print(json.dumps({'count': count, 'num_chunks': len(chunks), 'chunks': chunks}))"""

env_args = {'var_call_0BWhQ822FlEwjtXW5PCml263': 'file_storage/call_0BWhQ822FlEwjtXW5PCml263.json', 'var_call_HKlcYQzFxvMVPVpU7JW8rQXo': 'file_storage/call_HKlcYQzFxvMVPVpU7JW8rQXo.json', 'var_call_yhCUjmsat112LZjjClQBVvOu': 'file_storage/call_yhCUjmsat112LZjjClQBVvOu.json'}

exec(code, env_args)
