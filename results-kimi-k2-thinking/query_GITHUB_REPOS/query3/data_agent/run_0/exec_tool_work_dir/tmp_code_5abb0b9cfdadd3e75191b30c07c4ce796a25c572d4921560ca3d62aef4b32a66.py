code = """import json
import re

# Read the file containing Apache-2.0 repositories
file_path = var_functions.query_db:5

with open(file_path, 'r') as f:
    apache_repos = json.load(f)

# Filter for repositories that use Shell
shell_repos = []

for repo in apache_repos:
    language_desc = repo.get('language_description', '')
    
    # Check if Shell is mentioned in the language description
    if 'shell' in language_desc.lower():
        shell_repos.append(repo['repo_name'])

print('__RESULT__:')
print(json.dumps({
    'total_apache_repos': len(apache_repos),
    'shell_repos_count': len(shell_repos),
    'shell_repos': shell_repos[:50]  # Print first 50 for inspection
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
