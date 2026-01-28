code = """import json

# Check what repositories from metadata_database are actually in artifacts_database
repo_list_path = locals()['var_functions.query_db:2']
with open(repo_list_path, 'r') as f:
    repo_data = json.load(f)

metadata_repos = [item['repo_name'] for item in repo_data]

# Check available repos in artifacts_database
available_repos_result = locals()['var_functions.query_db:38']
available_repos = [item['repo_name'] for item in available_repos_result]

# Find intersection
common_repos = set(metadata_repos) & set(available_repos)

print('__RESULT__:')
print(json.dumps({
    'metadata_repos_count': len(metadata_repos),
    'available_repos_count': len(available_repos), 
    'common_repos_count': len(common_repos),
    'common_repos': list(common_repos)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:10': {'repo_names_count': 114972, 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:12': {'repo_count': 114972, 'sample_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts'"}, 'var_functions.query_db:16': [{'commit_count': '15016'}], 'var_functions.execute_python:18': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.query_db:20': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '963'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}], 'var_functions.execute_python:22': {'sample_size': 100, 'in_clause': "('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/...", 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:24': {'total_repos': 114972, 'batch_size': 200, 'total_batches': 575, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:28': {'batch_size': 50, 'first_batch_count': 50, 'query_preview': "SELECT COUNT(*) as commit_count FROM commits c WHERE c.repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/h..."}, 'var_functions.execute_python:30': {'total_repos': 114972, 'batch_size': 100, 'total_batches': 1150}, 'var_functions.query_db:32': [{'commit_count': '0'}], 'var_functions.query_db:34': [{'total_commits': '0'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': [{'repo_name': 'torvalds/linux', 'total': '16061'}, {'repo_name': 'apple/swift', 'total': '1051'}, {'repo_name': 'twbs/bootstrap', 'total': '340'}, {'repo_name': 'Microsoft/vscode', 'total': '190'}, {'repo_name': 'facebook/react', 'total': '178'}, {'repo_name': 'tensorflow/tensorflow', 'total': '156'}]}

exec(code, env_args)
