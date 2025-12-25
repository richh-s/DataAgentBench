code = """import json

# Read the file from the previous step
with open(locals()['var_function-call-11138479476113441497'], 'r') as f:
    data = json.load(f)

ids = [int(row['article_id']) for row in data]
min_id = min(ids)
max_id = max(ids)
count = len(ids)

result = {
    "count": count,
    "min_id": min_id,
    "max_id": max_id
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11138479476113441497': 'file_storage/function-call-11138479476113441497.json'}

exec(code, env_args)
