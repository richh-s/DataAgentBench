code = """import json

# Read the Swift repositories data
result_data = locals()['var_functions.query_db:2']

# Load the data
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        swift_repos = json.load(f)
else:
    swift_repos = result_data

# Count and show basic info
total_repos = len(swift_repos)
first_repo = swift_repos[0] if swift_repos else None

# Extract repo names
repo_names = [repo['repo_name'] for repo in swift_repos]
unique_count = len(repo_names)

result = {
    'total_swift_repos': total_repos,
    'first_repo_sample': first_repo,
    'unique_repo_names': unique_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files']}

exec(code, env_args)
