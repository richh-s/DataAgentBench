code = """import json
key = 'var_functions.query_db:5'
path = locals().get(key)
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [rec['repo_name'] for rec in repos]
# Build large SQL IN clause string. We'll format with quotes and commas.
# To avoid too large query maybe we can compress? We'll use standard quoting.
# Let's create a string with comma-separated quoted repo names.
quoted = ','.join(f"'{name}'" for name in repo_names)
print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'quoted_sample': quoted[:500]}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:10': {'total_repos': 114972}, 'var_functions.execute_python:12': {'total_repos': 114972}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
