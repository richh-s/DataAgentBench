code = """import json

# Load metadata repositories
metadata_file = locals()['var_functions.query_db:16']
with open(metadata_file, 'r') as f:
    metadata_repos = json.load(f)

metadata_repo_set = set([repo['repo_name'] for repo in metadata_repos])

# Artifact repos from the previous query
artifact_repos = locals()['var_functions.query_db:64']
artifact_repo_set = set([repo['repo_name'] for repo in artifact_repos])

# Find intersection
intersection = metadata_repo_set.intersection(artifact_repo_set)

print('__RESULT__:')
print(json.dumps({
    'metadata_repos': len(metadata_repo_set),
    'artifact_repos': len(artifact_repo_set),
    'intersection': len(intersection),
    'intersection_repos': list(intersection)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'commit_count': '15016'}], 'var_functions.execute_python:22': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.query_db:26': [{'commit_count': '0'}], 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'message': 'Loaded 114972 repositories. Ready to process in batches.'}, 'var_functions.execute_python:36': {'total_repos': 114972, 'num_batches': 230, 'batch_size': 500, 'queries_file': 'batch_queries.json', 'first_query_preview': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redi..."}, 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:44': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}], 'var_functions.execute_python:48': {'test_query': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor') AND message IS NOT NULL AND message != '' AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'", 'test_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.query_db:50': [{'commit_count': '0'}], 'var_functions.query_db:52': [{'commit_count': '0'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': {'metadata_repo_count': 114972, 'sample_metadata_repos': ['sdygt/sdygt.github.io', 'slavizh/Get-SCOMManagementPacks', 'frolv/bloaty', 'vjache/elips', 'martinmiranda14/Digitales', 'GoogleCloudPlatform/google-cloud-iot-arduino', 'Banno/graphite-setup', 'ncface/baustelle', 'suited/suited.js', 'codevilleacademy/codevilleacademy.github.com']}, 'var_functions.query_db:58': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}], 'var_functions.execute_python:60': {'message': 'Need to find intersection between metadata repos and artifacts repos'}, 'var_functions.query_db:62': [], 'var_functions.query_db:64': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}], 'var_functions.query_db:66': [{'repo_name': 'tensorflow/tensorflow'}]}

exec(code, env_args)
