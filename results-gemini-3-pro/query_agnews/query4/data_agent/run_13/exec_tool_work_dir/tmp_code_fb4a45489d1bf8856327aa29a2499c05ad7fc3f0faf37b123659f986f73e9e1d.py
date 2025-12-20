code = """import json

with open(locals()['var_function-call-517009556635827832'], 'r') as f:
    metadata = json.load(f)

ids = [int(item['article_id']) for item in metadata]
# Make sure they are unique just in case
ids = list(set(ids))

print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-517009556635827832': 'file_storage/function-call-517009556635827832.json', 'var_function-call-5428732152861875432': 6696}

exec(code, env_args)
