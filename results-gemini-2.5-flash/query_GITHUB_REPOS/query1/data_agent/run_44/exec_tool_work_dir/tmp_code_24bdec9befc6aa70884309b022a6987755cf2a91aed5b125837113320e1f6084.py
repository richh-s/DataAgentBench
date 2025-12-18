code = """import json

with open(locals()['var_function-call-18026234265819425101'], 'r') as f:
    repo_names_data = json.load(f)

non_python_repos = [repo['repo_name'] for repo in repo_names_data]
sampled_non_python_repos = non_python_repos[:1000]
repo_names_in_clause = ', '.join([f"'{repo}'" for repo in sampled_non_python_repos])

query = f"""
SELECT
    sample_repo_name,
    content
FROM
    contents
WHERE
    sample_path = 'README.md' AND
    sample_repo_name IN ({repo_names_in_clause})
"""

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2032146281819723315': 'file_storage/function-call-2032146281819723315.json', 'var_function-call-10889049203667993504': 'file_storage/function-call-10889049203667993504.json', 'var_function-call-11759728202920264499': 'file_storage/function-call-11759728202920264499.json', 'var_function-call-13813243618852406302': 'file_storage/function-call-13813243618852406302.json', 'var_function-call-18026234265819425101': 'file_storage/function-call-18026234265819425101.json'}

exec(code, env_args)
