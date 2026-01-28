code = """import json
path = var_call_0BWhQ822FlEwjtXW5PCml263
with open(path, 'r') as f:
    records = json.load(f)
ids = sorted({int(rec['article_id']) for rec in records})
# chunk size
chunk = 500
batches = [ids[i:i+chunk] for i in range(0, len(ids), chunk)]
print('__RESULT__:')
print(json.dumps({'batches': batches}))"""

env_args = {'var_call_0BWhQ822FlEwjtXW5PCml263': 'file_storage/call_0BWhQ822FlEwjtXW5PCml263.json', 'var_call_HKlcYQzFxvMVPVpU7JW8rQXo': 'file_storage/call_HKlcYQzFxvMVPVpU7JW8rQXo.json'}

exec(code, env_args)
