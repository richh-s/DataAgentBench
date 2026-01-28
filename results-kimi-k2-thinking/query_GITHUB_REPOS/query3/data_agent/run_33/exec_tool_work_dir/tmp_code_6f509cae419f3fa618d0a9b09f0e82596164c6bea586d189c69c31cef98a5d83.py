code = """import json

# Get the repository list file path
repo_list_file = 'var_functions.query_db:12'
print('Repository list file key:', repo_list_file)

# The variable is stored in locals()
all_vars = locals()
repo_data = None
for key, value in all_vars.items():
    if 'query_db:12' in key:
        repo_data = value
        break

print('Found repo data type:', type(repo_data))

# Read repository list from file
import json
with open(repo_data, 'r') as f:
    repos = json.load(f)

print(f'Total repositories found: {len(repos)}')

# Extract repository names
repo_names = [r['repo_name'] for r in repos]
print(f'Sample repo names: {repo_names[:5]}')

# Let's create a batched approach since we have many repositories
# First, let's just get a count of commits matching criteria for a small batch
test_batch = repo_names[:100]  # Test with first 100 repos
print(f'Test batch size: {len(test_batch)}')

# Create the query for DuckDB
quoted_repos = [f"'{name}'" for name in test_batch]
in_clause = ', '.join(quoted_repos)
query = f"""
SELECT COUNT(*) as total_commits 
FROM commits 
WHERE repo_name IN ({in_clause}) 
AND message IS NOT NULL 
AND LENGTH(message) < 1000 
AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%')
"""

print('Sample query for first 100 repos:', query[:300] + '...')

__RESULT__: json.dumps({'total_repos': len(repo_names), 'test_batch_size': len(test_batch), 'sample_query': query[:200]})"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
