code = """import json

# Read repository names
repo_list_path = locals()['var_functions.query_db:2']
with open(repo_list_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]
batch_size = 50
all_batches = []

for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    quoted_batch = [f"'" + repo.replace("'", "''") + "'" for repo in batch]
    in_clause = ", ".join(quoted_batch)
    all_batches.append({
        'start_idx': i,
        'end_idx': min(i+batch_size, len(repo_names)),
        'in_clause': f"({in_clause})"
    })

# Use first batch for testing
first_batch = all_batches[0]
test_query = f"""
SELECT COUNT(*) as commit_count 
FROM commits c 
WHERE c.repo_name IN {first_batch['in_clause']}
AND c.message IS NOT NULL 
AND LENGTH(c.message) < 1000 
AND LOWER(c.message) NOT LIKE 'merge%' 
AND LOWER(c.message) NOT LIKE 'update%' 
AND LOWER(c.message) NOT LIKE 'test%'
"""

print('__RESULT__:')
print(json.dumps({
    'total_batches': len(all_batches),
    'first_batch': {
        'range': f"{first_batch['start_idx']} to {first_batch['end_idx']}",
        'sample_repos': repo_names[:3],
        'query_preview': test_query[:300] + "..." if len(test_query) > 300 else test_query
    }
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:10': {'repo_names_count': 114972, 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:12': {'repo_count': 114972, 'sample_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts'"}, 'var_functions.query_db:16': [{'commit_count': '15016'}], 'var_functions.execute_python:18': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}, 'var_functions.query_db:20': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '963'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}], 'var_functions.execute_python:22': {'sample_size': 100, 'in_clause': "('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/...", 'first_few_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.execute_python:24': {'total_repos': 114972, 'batch_size': 200, 'total_batches': 575, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}}

exec(code, env_args)
