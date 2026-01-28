code = """import json

result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    packageinfo_results = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'count': len(packageinfo_results),
    'sample': packageinfo_results[0] if packageinfo_results else None
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
