code = """import json
import os

result_file = locals()['var_functions.query_db:16']
with open(result_file, 'r') as f:
    repos = json.load(f)

repo_names = [repo['repo_name'] for repo in repos]

batch_size = 500
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]

queries = []
for batch in batches:
    formatted_batch = ', '.join(["'" + repo + "'" for repo in batch])
    query = "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN (" + formatted_batch + ") AND message IS NOT NULL AND message != '' AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'"
    queries.append(query.strip())

output_file = 'batch_queries.json'
with open(output_file, 'w') as f:
    json.dump({'queries': queries, 'count': len(queries)}, f)

print('__RESULT__:')
result = {
    'total_repos': len(repo_names),
    'num_batches': len(batches),
    'batch_size': batch_size,
    'queries_file': output_file,
    'first_query_preview': queries[0][:200] + '...' if queries else 'No queries'
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'commit_count': '15016'}], 'var_functions.execute_python:22': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.query_db:26': [{'commit_count': '0'}], 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'message': 'Loaded 114972 repositories. Ready to process in batches.'}}

exec(code, env_args)
