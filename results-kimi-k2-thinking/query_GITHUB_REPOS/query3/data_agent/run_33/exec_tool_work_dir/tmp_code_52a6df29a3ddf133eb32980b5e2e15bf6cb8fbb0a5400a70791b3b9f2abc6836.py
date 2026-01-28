code = """import json

# Read repository list
repo_list_file = locals()['var_functions.query_db:12']
with open(repo_list_file, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]
total_repos = len(repo_names)
print(f'Loaded {total_repos} repositories')

# Let's run queries for the first few batches to test if we get results
batch_size = 1000
first_few_batches = []

# Process first 5 batches (5000 repositories)
for batch_num in range(5):
    start = batch_num * batch_size
    end = min(start + batch_size, total_repos)
    batch = repo_names[start:end]
    
    quoted_batch = [f"'{repo}'" for repo in batch]
    in_clause = ', '.join(quoted_batch)
    
    query = f"SELECT COUNT(*) as count FROM commits WHERE repo_name IN ({in_clause}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'"
    
    first_few_batches.append({
        'batch_num': batch_num + 1,
        'start_idx': start,
        'end_idx': end,
        'repo_count': len(batch),
        'query': query
    })

result = {
    'batches_prepared': len(first_few_batches),
    'total_repos_in_batches': sum(b['repo_count'] for b in first_few_batches),
    'first_query_preview': first_few_batches[0]['query'][:200] + '...'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:36': {'total_repositories': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:38': [{'commit_count': '0'}], 'var_functions.execute_python:40': {'total_repositories': 114972, 'batch_size': 1000, 'estimated_batches': 115, 'commit_count': 0, 'status': 'ready_for_batch_processing'}, 'var_functions.execute_python:44': {'total_repositories': 114972, 'first_batch_size': 1000, 'in_clause_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:48': {'total_repositories': 114972, 'batch_size': 1000, 'total_batches': 115}, 'var_functions.execute_python:52': {'status': 'ready_to_query_commits', 'total_repos': 114972, 'batches': 115, 'batch_size': 1000, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.execute_python:56': {'total_repositories': 114972, 'batch_size': 1000, 'batches': 115, 'first_batch_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:58': {'total_batches': 115, 'batch_size': 1000, 'total_repositories': 114972, 'first_batch_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:62': [{'commit_count': '0'}], 'var_functions.execute_python:66': {'batches': 115, 'total_repo': 114972}, 'var_functions.query_db:70': [{'commit_count': '0'}], 'var_functions.query_db:72': [{'total_commits': '0'}], 'var_functions.execute_python:74': {'total_repos': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:77': [{'commit_count': '0'}], 'var_functions.query_db:78': [{'total_commits': '14318'}], 'var_functions.execute_python:82': {'total_batches': 230, 'batch_size': 500, 'total_repos': 114972, 'first_batch_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:86': {'total_repositories': 114972, 'in_clause_length': 3021681, 'batch_size': 1000, 'total_batches': 115, 'status': 'ready_for_batch_queries'}, 'var_functions.execute_python:88': {'total_queries': 115, 'batch_size': 1000, 'first_query_preview': "SELECT COUNT(*) FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol..."}, 'var_functions.execute_python:90': {'queries_generated': 10, 'batches_covered': 10, 'first_query': "SELECT COUNT(*) as count FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'ra...", 'last_query': "SELECT COUNT(*) as count FROM commits WHERE repo_name IN ('stanleyxu2005/docker-kafka', 'kivio/PerfKitBenchmarker', 'pallavagarwal07/sandboxfs', 'mheon/cri-o', 'chadmv/plow', 'dagolden/perlweb', 'BBN-..."}, 'var_functions.execute_python:94': {'first_batch_size': 1000, 'first_batch_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common'], 'in_clause_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-..."}, 'var_functions.execute_python:98': {'batches': 115, 'status': 'ready'}, 'var_functions.execute_python:100': 'file_storage/functions.execute_python:100.json'}

exec(code, env_args)
