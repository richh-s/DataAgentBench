code = """import json
import os

# Read all repository names
repo_list_path = locals()['var_functions.query_db:2']
with open(repo_list_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]

# Split into batches
batch_size = 500
batches = [repo_names[i:i + batch_size] for i in range(0, len(repo_names), batch_size)]

# Prepare query template
query_template = """
SELECT COUNT(*) as commit_count FROM commits c 
WHERE c.repo_name IN ({repos}) 
AND c.message IS NOT NULL 
AND LENGTH(c.message) < 1000 
AND LOWER(c.message) NOT LIKE 'merge%' 
AND LOWER(c.message) NOT LIKE 'update%' 
AND LOWER(c.message) NOT LIKE 'test%'
"""

# Generate all batch queries
batch_queries = []
for batch_num, batch in enumerate(batches[:3]):  # Only first 3 batches for now (testing)
    quoted_batch = [f"'{repo}'" for repo in batch]
    in_clause = ", ".join(quoted_batch)
    query = query_template.format(repos=in_clause)
    batch_queries.append({
        'batch_num': batch_num,
        'repo_count': len(batch),
        'sample_repos': batch[:3],
        'query': query
    })

print('__RESULT__:')
print(json.dumps({
    'total_batches': len(batches),
    'first_batch_query': batch_queries[0]['query'] if batch_queries else None,
    'batches_info': batch_queries
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:10': {'repo_names_count': 114972, 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:12': {'repo_count': 114972, 'sample_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts'"}}

exec(code, env_args)
