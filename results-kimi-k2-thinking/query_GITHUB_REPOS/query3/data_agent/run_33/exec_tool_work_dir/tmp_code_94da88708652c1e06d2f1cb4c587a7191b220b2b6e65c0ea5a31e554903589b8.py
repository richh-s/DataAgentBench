code = """import json

# Load all repository names
repo_list_file = locals()['var_functions.query_db:12']
with open(repo_list_file, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]
total_repos = len(repo_names)

print(f'Loaded {total_repos} repositories')

# Create a single comprehensive query
# Since we have many repos, we'll process them in the query using a large IN clause
# But first, let's check how many chars our full list would be
all_quoted = [f"'{repo}'" for repo in repo_names]
full_in_clause = ', '.join(all_quoted)
clause_length = len(full_in_clause)

print(f'Full IN clause length: {clause_length} characters')
print(f'Number of repositories: {len(all_quoted)}')

# Check if we can do this in one query or need multiple
# Most databases have query length limits, so let's use batches
batch_size = 1000
total_batches = (total_repos + batch_size - 1) // batch_size

print(f'Will use {total_batches} batches of {batch_size} repositories')

result = {
    'total_repositories': total_repos,
    'in_clause_length': clause_length,
    'batch_size': batch_size,
    'total_batches': total_batches,
    'status': 'ready_for_batch_queries'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:36': {'total_repositories': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:38': [{'commit_count': '0'}], 'var_functions.execute_python:40': {'total_repositories': 114972, 'batch_size': 1000, 'estimated_batches': 115, 'commit_count': 0, 'status': 'ready_for_batch_processing'}, 'var_functions.execute_python:44': {'total_repositories': 114972, 'first_batch_size': 1000, 'in_clause_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:48': {'total_repositories': 114972, 'batch_size': 1000, 'total_batches': 115}, 'var_functions.execute_python:52': {'status': 'ready_to_query_commits', 'total_repos': 114972, 'batches': 115, 'batch_size': 1000, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.execute_python:56': {'total_repositories': 114972, 'batch_size': 1000, 'batches': 115, 'first_batch_preview': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}, 'var_functions.execute_python:58': {'total_batches': 115, 'batch_size': 1000, 'total_repositories': 114972, 'first_batch_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:62': [{'commit_count': '0'}], 'var_functions.execute_python:66': {'batches': 115, 'total_repo': 114972}, 'var_functions.query_db:70': [{'commit_count': '0'}], 'var_functions.query_db:72': [{'total_commits': '0'}], 'var_functions.execute_python:74': {'total_repos': 114972, 'batch_size': 500, 'total_batches': 230, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common']}, 'var_functions.query_db:77': [{'commit_count': '0'}], 'var_functions.query_db:78': [{'total_commits': '14318'}], 'var_functions.execute_python:82': {'total_batches': 230, 'batch_size': 500, 'total_repos': 114972, 'first_batch_in_clause': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/c..."}}

exec(code, env_args)
