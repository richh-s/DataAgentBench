code = """import json
# Load the list of repositories from the metadata query
repo_file = locals()['var_functions.query_db:2']
with open(repo_file, 'r') as f:
    repo_data = json.load(f)

# Create a list of repository names for the query
repo_list = [item['repo_name'] for item in repo_data]

# Process in batches
batch_size = 500
all_results = []

for i in range(0, len(repo_list), batch_size):
    batch = repo_list[i:i+batch_size]
    # Create a comma-separated list of quoted repository names
    repo_string = ', '.join(f"'{repo}'" for repo in batch)
    
    query = f"""
    SELECT COUNT(commit) as batch_count 
    FROM commits 
    WHERE repo_name IN ({repo_string})
    AND message IS NOT NULL 
    AND LENGTH(message) < 1000 
    AND LOWER(message) NOT LIKE 'merge%' 
    AND LOWER(message) NOT LIKE 'update%' 
    AND LOWER(message) NOT LIKE 'test%'
    """
    
    # Store the query for execution
    all_results.append({
        'batch_start': i,
        'batch_end': min(i + batch_size, len(repo_list)),
        'query': query
    })

print('__RESULT__:')
print(json.dumps({
    'total_batches': len(all_results),
    'batch_size': batch_size,
    'total_repos': len(repo_list),
    'sample_query': all_results[0]['query'][:200] + '...' if len(all_results) > 0 else ''
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.execute_python:8': {'total_repos': 114972, 'batches': 575}, 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:12': {'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'total_count': 114972}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.execute_python:20': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}}

exec(code, env_args)
