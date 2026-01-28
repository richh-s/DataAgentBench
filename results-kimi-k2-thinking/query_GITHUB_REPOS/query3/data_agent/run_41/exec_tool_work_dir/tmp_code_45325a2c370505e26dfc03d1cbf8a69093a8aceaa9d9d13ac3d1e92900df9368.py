code = """import json

# Load the shell repos list
with open('/tmp/shell_repos.json', 'r') as f:
    shell_repos = json.load(f)

# Get the file path for commits
commits_file_path = locals()['var_functions.query_db:12']

# Read the full commits data
with open(commits_file_path, 'r') as f:
    commits = json.load(f)

print(f"Total commits retrieved: {len(commits)}")
print(f"Shell repos to filter against: {len(shell_repos)}")

# Create a set for faster lookup
shell_repos_set = set(shell_repos)

# Filter commits based on criteria
def passes_message_filter(msg):
    if msg is None:
        return False
    if len(msg) >= 1000:
        return False
    msg_lower = msg.lower().strip()
    if msg_lower.startswith('merge') or msg_lower.startswith('update') or msg_lower.startswith('test'):
        return False
    return True

filtered_commits = []
for commit in commits:
    if commit['repo_name'] in shell_repos_set and passes_message_filter(commit['message']):
        filtered_commits.append(commit)

print(f"Filtered commits count: {len(filtered_commits)}")

# Print the result
print('__RESULT__:')
print(json.dumps({'commit_count': len(filtered_commits)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'shell_repo_count': 114946, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
