code = """import json

# Load all repository names
repo_list_file = locals()['var_functions.query_db:12']
with open(repo_list_file, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]
print(f'Total repositories to check: {len(repo_names)}')

# Process in larger batches to reduce number of queries
batch_size = 2000
total_batches = (len(repo_names) + batch_size - 1) // batch_size

print(f'Will process in {total_batches} batches of {batch_size} repositories each')

# Create batch queries
batch_queries = []
for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    quoted_batch = [f"'{repo}'" for repo in batch]
    in_clause = ', '.join(quoted_batch)
    
    # Note: DuckDB uses LENGTH, SQLite uses LEN or LENGTH depending on version
    # Using standard SQL LENGTH which should work
    query = f"""
    SELECT COUNT(*) as count 
    FROM commits 
    WHERE repo_name IN ({in_clause})
      AND message IS NOT NULL 
      AND LENGTH(message) < 1000 
      AND LOWER(message) NOT LIKE 'merge%'
      AND LOWER(message) NOT LIKE 'update%'
      AND LOWER(message) NOT LIKE 'test%'
    """
    
    batch_queries.append({
        'start_idx': i,
        'end_idx': min(i + batch_size, len(repo_names)),
        'repo_count': len(batch),
        'query': query
    })

result = {
    'total_batches': len(batch_queries),
    'batch_size': batch_size,
    'total_repos': len(repo_names),
    'first_query_preview': batch_queries[0]['query'][:250] + '...' if batch_queries else 'No queries'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:36': {'total_repositories': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:38': [{'commit_count': '0'}], 'var_functions.execute_python:40': {'total_repositories': 114972, 'batch_size': 1000, 'estimated_batches': 115, 'commit_count': 0, 'status': 'ready_for_batch_processing'}, 'var_functions.execute_python:44': {'total_repositories': 114972, 'first_batch_size': 1000, 'in_clause_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:48': {'total_repositories': 114972, 'batch_size': 1000, 'total_batches': 115}, 'var_functions.execute_python:52': {'status': 'ready_to_query_commits', 'total_repos': 114972, 'batches': 115, 'batch_size': 1000, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.execute_python:56': {'total_repositories': 114972, 'batch_size': 1000, 'batches': 115, 'first_batch_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:58': {'total_batches': 115, 'batch_size': 1000, 'total_repositories': 114972, 'first_batch_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:62': [{'commit_count': '0'}], 'var_functions.execute_python:66': {'batches': 115, 'total_repo': 114972}, 'var_functions.query_db:70': [{'commit_count': '0'}], 'var_functions.query_db:72': [{'total_commits': '0'}], 'var_functions.execute_python:74': {'total_repos': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:77': [{'commit_count': '0'}], 'var_functions.query_db:78': [{'total_commits': '14318'}]}

exec(code, env_args)
