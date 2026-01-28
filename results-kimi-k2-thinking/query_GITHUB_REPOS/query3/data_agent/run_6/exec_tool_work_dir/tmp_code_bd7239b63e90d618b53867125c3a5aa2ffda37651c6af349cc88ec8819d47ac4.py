code = """import json
import os
# The result of the earlier query is stored in var_functions.query_db:5 as a file path.
key = 'var_functions.query_db:5'
path = locals().get(key)
with open(path, 'r') as f:
    repos = json.load(f)  # list of dicts with repo_name
repo_names = [rec['repo_name'] for rec in repos]
print('__RESULT__:')
print(json.dumps({'total_repos': len(repo_names)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}}

exec(code, env_args)
