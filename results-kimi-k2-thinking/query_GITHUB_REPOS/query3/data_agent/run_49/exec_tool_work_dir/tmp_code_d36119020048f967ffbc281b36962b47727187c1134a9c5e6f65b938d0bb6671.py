code = """import json

# Read all repository names from the previous query
repo_list_path = locals()['var_functions.query_db:2']
with open(repo_list_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]

# Calculate batch size and total batches
batch_size = 200  # Smaller batch size for DuckDB
total_batches = len(repo_names) // batch_size + (1 if len(repo_names) % batch_size > 0 else 0)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'batch_size': batch_size,
    'total_batches': total_batches,
    'sample_repos': repo_names[:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:10': {'repo_names_count': 114972, 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:12': {'repo_count': 114972, 'sample_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts'"}, 'var_functions.query_db:16': [{'commit_count': '15016'}], 'var_functions.execute_python:18': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.query_db:20': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '963'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}], 'var_functions.execute_python:22': {'sample_size': 100, 'in_clause': "('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/...", 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}}

exec(code, env_args)
