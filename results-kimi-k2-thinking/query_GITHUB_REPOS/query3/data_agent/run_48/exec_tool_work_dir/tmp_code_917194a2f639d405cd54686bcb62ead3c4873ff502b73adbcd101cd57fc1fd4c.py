code = """import json

# Read the repository list from file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    repo_data = json.load(f)

# Create the repository list
repo_names = [repo['repo_name'] for repo in repo_data]

# Let's create a batch query strategy
# First, let's test with a single batch of 200 repos
batch_0 = repo_names[:200]

# Format the repo names for SQL IN clause
formatted_batch = "'" + "','".join(batch_0) + "'"

# Create the query
query = f"""
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN ({formatted_batch})
  AND message IS NOT NULL 
  AND LENGTH(message) < 1000 
  AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%')
"""

print('__RESULT__:')
print(json.dumps({
    'query': query,
    'batch_size': len(batch_0),
    'first_few_repos_in_batch': batch_0[:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.execute_python:12': {'repo_count': 114972, 'repo_list_sample': "'jitsi/jipopro','NuGet/json-ld.net','virtualcoinclub/common','pydev/jmx_exporter','eskatos/qi4j-dev-scripts','doximity/docker-redis','raghavkarol/dotfiles','Microsoft/TypeScript','romelperez/conky-com"}, 'var_functions.execute_python:16': {'total_repos': 114972, 'num_batches': 230, 'batch_size': 500}, 'var_functions.execute_python:18': {'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.execute_python:8', 'var_functions.execute_python:12', 'var_functions.execute_python:16', '__builtins__', 'json', 'storage_key']}, 'var_functions.execute_python:20': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:22': {'repo_count': 114972, 'num_batches': 1150, 'batch_size': 100, 'batch_0_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.execute_python:26': {'total_matching_repos': 114972, 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 575, 'batch_size': 200}}

exec(code, env_args)
