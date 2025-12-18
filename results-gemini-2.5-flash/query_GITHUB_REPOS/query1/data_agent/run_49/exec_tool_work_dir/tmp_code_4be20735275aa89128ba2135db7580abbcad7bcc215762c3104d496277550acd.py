code = """import json

repo_names_str_from_storage = locals()['var_function-call-12562817640177838482']

query = f"SELECT sample_repo_name, content FROM contents WHERE sample_repo_name IN ({repo_names_str_from_storage}) AND lower(sample_path) = 'readme.md';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-17696950855351198832': 'file_storage/function-call-17696950855351198832.json', 'var_function-call-12562817640177838482': 'file_storage/function-call-12562817640177838482.json'}

exec(code, env_args)
