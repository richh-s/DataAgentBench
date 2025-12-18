code = """import json

swift_repos = [repo['repo_name'] for repo in json.load(open(locals()['var_function-call-1512978699432665502']))]

swift_repos_str = ", ".join([f"'{repo}'" for repo in swift_repos])

query = "SELECT id, sample_repo_name, COUNT(id) AS copy_count FROM contents WHERE sample_repo_name IN (" + swift_repos_str + ") AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY copy_count DESC LIMIT 1;"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1512978699432665502': 'file_storage/function-call-1512978699432665502.json'}

exec(code, env_args)
