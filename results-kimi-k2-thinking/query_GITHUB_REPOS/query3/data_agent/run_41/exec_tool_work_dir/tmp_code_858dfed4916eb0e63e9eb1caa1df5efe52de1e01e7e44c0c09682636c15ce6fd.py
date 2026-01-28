code = """import json

# Get the file path from the storage variable
result_file_path = locals()['var_functions.query_db:4']

# Read the full results from the file
with open(result_file_path, 'r') as f:
    repo_data = json.load(f)

# Filter repositories that actually have Shell as a language
shell_repos = []
for repo in repo_data:
    lang_desc = repo['language_description'].lower()
    # Check if Shell is actually listed as a language with byte count
    if 'shell' in lang_desc and 'shell (0 bytes)' not in lang_desc:
        shell_repos.append(repo['repo_name'])

print(f"Total repositories found: {len(repo_data)}")
print(f"Repositories with Shell code: {len(shell_repos)}")
print(f"First 10 repositories: {shell_repos[:10]}")

# Store the shell repos list for later use
with open('/tmp/shell_repos.json', 'w') as f:
    json.dump(shell_repos, f)

print('__RESULT__:')
print(json.dumps({'shell_repo_count': len(shell_repos), 'sample_repos': shell_repos[:10]}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
