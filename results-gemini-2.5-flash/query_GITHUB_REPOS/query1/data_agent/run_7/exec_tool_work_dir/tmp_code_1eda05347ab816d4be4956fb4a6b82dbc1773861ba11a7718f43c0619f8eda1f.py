code = """import json

with open(locals()['var_function-call-2205448076081000873'], 'r') as f:
    repo_names_str = json.load(f)

query = f"SELECT sample_repo_name, content FROM contents WHERE sample_repo_name IN ({repo_names_str}) AND sample_path = 'README.md';"
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-6640177142775489859': 'file_storage/function-call-6640177142775489859.json', 'var_function-call-2205448076081000873': 'file_storage/function-call-2205448076081000873.json'}

exec(code, env_args)
