code = """import json

# Load the repository list
repo_list_file = locals()['var_functions.query_db:24']
with open(repo_list_file, 'r') as f:
    repositories = json.load(f)

repo_names = [repo['repo_name'] for repo in repositories]
total_repos = len(repo_names)
batch_size = 200
num_batches = (total_repos + batch_size - 1) // batch_size

# Create a temporary table in DuckDB to store the target repository names
# This approach avoids large IN clauses
print('__RESULT__:')
print(json.dumps({
    "action": "create_temp_table",
    "total_repos": total_repos,
    "message": "Will create a temporary table to store target repositories"
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 114972, 'var_functions.execute_python:6': {'total_repos': 114972, 'num_batches': 115, 'first_batch_size': 1000}, 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': {'total_repos': 114972, 'batch_size': 50, 'num_batches': 2300}, 'var_functions.query_db:14': [{'total_commits': '15016'}], 'var_functions.execute_python:16': {'first_batch_size': 50, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts'], 'in_clause_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:18': {'total_repos': 114972, 'batch_size': 100, 'num_batches': 1150, 'message': 'Will process 114972 repositories in 1150 batches of 100 each'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_repos': 114972, 'batch_size': 1000, 'num_batches': 115, 'message': 'Processing 114972 repositories in 115 batches of up to 1000 each'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_repos': 114972, 'batch_size': 200, 'num_batches': 575, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}}

exec(code, env_args)
