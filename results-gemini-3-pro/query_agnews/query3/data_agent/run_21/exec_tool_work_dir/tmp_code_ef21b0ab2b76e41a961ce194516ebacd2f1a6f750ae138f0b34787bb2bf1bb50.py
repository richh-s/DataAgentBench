code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-4731593455298835981']

# Read the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract article_ids
article_ids = [item['article_id'] for item in data]
count = len(article_ids)

print("__RESULT__:")
print(json.dumps({"count": count, "ids": article_ids}))"""

env_args = {'var_function-call-4731593455298835981': 'file_storage/function-call-4731593455298835981.json'}

exec(code, env_args)
