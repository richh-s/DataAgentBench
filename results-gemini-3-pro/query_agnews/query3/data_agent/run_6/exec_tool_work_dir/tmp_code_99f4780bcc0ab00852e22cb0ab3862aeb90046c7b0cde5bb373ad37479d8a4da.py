code = """import json

# Read the file from the previous step
with open(locals()['var_function-call-11138479476113441497'], 'r') as f:
    data = json.load(f)

# Extract IDs and convert to int
ids = [int(row['article_id']) for row in data]

print("__RESULT__:")
print(len(ids))
print(json.dumps(ids[:10])) # Print first 10 to check format"""

env_args = {'var_function-call-11138479476113441497': 'file_storage/function-call-11138479476113441497.json'}

exec(code, env_args)
