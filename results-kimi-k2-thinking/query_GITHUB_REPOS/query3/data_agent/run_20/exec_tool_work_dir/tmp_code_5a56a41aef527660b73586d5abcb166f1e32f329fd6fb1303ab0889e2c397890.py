code = """import json

# Load the repository names
result_file = locals()['var_functions.query_db:16']
with open(result_file, 'r') as f:
    repos = json.load(f)

repo_names = [repo['repo_name'] for repo in repos]

# Create a single query using a large IN clause
# Format: ('repo1', 'repo2', ...)
formatted_repos = ', '.join([f"'{repo}'" for repo in repo_names])

query = f"""
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN ({formatted_repos})
  AND message IS NOT NULL 
  AND message != '' 
  AND LENGTH(message) < 1000 
  AND LOWER(message) NOT LIKE 'merge%' 
  AND LOWER(message) NOT LIKE 'update%' 
  AND LOWER(message) NOT LIKE 'test%'
"""

print('__RESULT__:')
print(json.dumps({'query': query.strip(), 'total_repos_in_query': len(repo_names)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'commit_count': '15016'}], 'var_functions.execute_python:22': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.query_db:26': [{'commit_count': '0'}], 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'message': 'Loaded 114972 repositories. Ready to process in batches.'}, 'var_functions.execute_python:36': {'total_repos': 114972, 'num_batches': 230, 'batch_size': 500, 'queries_file': 'batch_queries.json', 'first_query_preview': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redi..."}, 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
