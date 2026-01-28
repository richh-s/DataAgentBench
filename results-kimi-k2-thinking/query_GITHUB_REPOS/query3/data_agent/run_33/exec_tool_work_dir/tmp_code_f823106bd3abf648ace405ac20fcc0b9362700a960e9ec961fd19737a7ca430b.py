code = """import json

# Read the complete repository list
repo_list_file = locals()['var_functions.query_db:12']

with open(repo_list_file, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]
total_repos = len(repo_names)

print(f'Loaded {total_repos} repositories')

# Process repositories in batches to count commits
batch_size = 500
all_commit_counts = []

# We'll build queries for each batch
for i in range(0, total_repos, batch_size):
    batch_repos = repo_names[i:i+batch_size]
    quoted_repos = [f"'{repo}'" for repo in batch_repos]
    in_clause = ', '.join(quoted_repos)
    
    query = f"""
    SELECT COUNT(*) as count 
    FROM commits 
    WHERE repo_name IN ({in_clause})
    AND message IS NOT NULL 
    AND LENGTH(message) < 1000 
    AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%')
    """
    
    all_commit_counts.append({
        'batch_start': i,
        'batch_end': i + len(batch_repos),
        'query': query
    })

result = {
    'total_repositories': total_repos,
    'batch_size': batch_size,
    'total_batches': len(all_commit_counts),
    'sample_query': all_commit_counts[0]['query'][:200] + '...' if all_commit_counts else 'No queries'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:36': {'total_repositories': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:38': [{'commit_count': '0'}], 'var_functions.execute_python:40': {'total_repositories': 114972, 'batch_size': 1000, 'estimated_batches': 115, 'commit_count': 0, 'status': 'ready_for_batch_processing'}}

exec(code, env_args)
