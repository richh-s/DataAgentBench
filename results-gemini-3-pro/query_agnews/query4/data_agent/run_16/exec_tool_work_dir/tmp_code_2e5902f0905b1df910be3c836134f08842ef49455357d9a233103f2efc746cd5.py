code = """import json

file_path = locals()['var_function-call-18346563918913497179']
with open(file_path, 'r') as f:
    article_ids = json.load(f)

min_id = min(article_ids)
max_id = max(article_ids)
count = len(article_ids)
span = max_id - min_id + 1
density = count / span

print(f"Min ID: {min_id}")
print(f"Max ID: {max_id}")
print(f"Count: {count}")
print(f"Span: {span}")
print(f"Density: {density:.4f}")

print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id}))"""

env_args = {'var_function-call-16407373274121457065': 'file_storage/function-call-16407373274121457065.json', 'var_function-call-18346563918913497179': 'file_storage/function-call-18346563918913497179.json', 'var_function-call-1343490920313838881': 6696}

exec(code, env_args)
