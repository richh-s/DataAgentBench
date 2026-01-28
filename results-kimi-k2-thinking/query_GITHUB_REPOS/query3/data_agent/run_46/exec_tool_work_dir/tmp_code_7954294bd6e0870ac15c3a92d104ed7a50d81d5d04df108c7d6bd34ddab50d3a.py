code = """import json

# Read the Shell repositories from the stored result
with open('var_functions.query_db:0', 'r') as f:
    shell_repos = json.load(f)

# Read the Apache-2.0 repositories from the stored result
with open('var_functions.query_db:2', 'r') as f:
    apache_repos = json.load(f)

# Extract repo names
shell_repo_names = {repo['repo_name'] for repo in shell_repos}
apache_repo_names = {repo['repo_name'] for repo in apache_repos}

# Find intersection (both Shell and Apache-2.0)
qualified_repos = list(shell_repo_names & apache_repo_names)

print('__RESULT__:')
print(json.dumps({
    'shell_repos_count': len(shell_repo_names),
    'apache_repos_count': len(apache_repo_names),
    'qualified_repos_count': len(qualified_repos),
    'example_repos': qualified_repos[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['languages', 'repos', 'licenses']}

exec(code, env_args)
