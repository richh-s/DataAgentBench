code = """import json

# Read the full list of repositories that match the criteria
result_file = locals()['var_functions.query_db:16']
with open(result_file, 'r') as f:
    repos = json.load(f)

# Extract all repository names
repo_names = [repo['repo_name'] for repo in repos]

# Process in batches of 500 to be safe
batch_size = 500
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]

# Create string representations of batches for SQL IN clauses
batch_queries = []
for i, batch in enumerate(batches):
    # Format: ('repo1', 'repo2', ...)
    formatted_batch = ', '.join([f"'{repo}'" for repo in batch])
    batch_queries.append(f"({formatted_batch})")

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names), 
    'num_batches': len(batches),
    'batch_size': batch_size,
    'first_batch': batch_queries[0] if batch_queries else "()",
    'last_batch_size': len(batches[-1]) if batches else 0
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'commit_count': '15016'}], 'var_functions.execute_python:22': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.query_db:26': [{'commit_count': '0'}], 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}}

exec(code, env_args)
