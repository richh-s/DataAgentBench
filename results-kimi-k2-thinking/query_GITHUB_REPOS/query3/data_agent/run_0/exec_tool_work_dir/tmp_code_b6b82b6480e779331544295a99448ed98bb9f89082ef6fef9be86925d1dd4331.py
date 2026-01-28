code = """import json

# Read the file with Apache-2.0 repositories
file_path = "file_storage/functions.query_db:5.json"

with open(file_path, 'r') as f:
    apache_repos = json.load(f)

# Filter for repositories that use Shell
shell_repos = []
for repo in apache_repos:
    language_desc = repo.get('language_description', '')
    if 'shell' in language_desc.lower():
        shell_repos.append(repo['repo_name'])

print('__RESULT__:')
print(json.dumps({
    'total_apache_repos': len(apache_repos),
    'shell_repos_count': len(shell_repos),
    'first_few_shell_repos': shell_repos[:20]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_string': True, 'preview': 'file_storage/functions.query_db:5.json'}}

exec(code, env_args)
