code = """import json
import os

# Read the full list of repositories from the metadata query
result_file = locals()['var_functions.query_db:16']
with open(result_file, 'r') as f:
    repos = json.load(f)

# Extract all repository names
repo_names = [repo['repo_name'] for repo in repos]

# Process repositories in batches
batch_size = 500
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]

# Create SQL queries for each batch and save them to a file
queries = []
for i, batch in enumerate(batches):
    # Format repository names for SQL IN clause
    formatted_batch = ', '.join([f"'{repo}'" for repo in batch])
    
    # Create query for this batch
    query = f"""
    SELECT COUNT(*) as commit_count 
    FROM commits 
    WHERE repo_name IN ({formatted_batch})
      AND message IS NOT NULL 
      AND message != '' 
      AND LENGTH(message) < 1000 
      AND LOWER(message) NOT LIKE 'merge%' 
      AND LOWER(message) NOT LIKE 'update%' 
      AND LOWER(message) NOT LIKE 'test%'
    """
    
    queries.append(query.strip())

# Save queries to file for execution
output_file = '/tmp/batch_queries.json'
with open(output_file, 'w') as f:
    json.dump(queries, f)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'num_batches': len(batches),
    'batch_size': batch_size,
    'queries_file': output_file,
    'first_query_preview': queries[0][:200] + '...' if queries else 'No queries'
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'commit_count': '15016'}], 'var_functions.execute_python:22': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.query_db:26': [{'commit_count': '0'}], 'var_functions.execute_python:28': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': {'message': 'Loaded 114972 repositories. Ready to process in batches.'}}

exec(code, env_args)
