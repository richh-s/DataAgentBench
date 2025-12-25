code = """import json

with open('var_function-call-16274142036252595144.json', 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]
print(f"Total repos: {len(repo_names)}")
print(f"Example repos: {repo_names[:5]}")

print("__RESULT__:")
print(json.dumps({"count": len(repo_names), "examples": repo_names[:5]}))"""

env_args = {'var_function-call-16274142036252595144': 'file_storage/function-call-16274142036252595144.json'}

exec(code, env_args)
