code = """import json

# Read the repository list from file
repo_data_file = '/tmp/tmp0q1w9l4h.json'
print('Reading repository list from file...')

with open(repo_data_file, 'r') as f:
    repos = json.load(f)

print(f'Total repositories with Shell and Apache-2.0 license: {len(repos)}')
print('Sample repositories:', repos[:3])

# Extract repository names
repo_names = [r['repo_name'] for r in repos]
print(f'First few repository names: {repo_names[:5]}')

# To avoid query length limits, let's process in batches
# Calculate how many batches we need
batch_size = 500  # Process 500 repos at a time
total_batches = (len(repo_names) + batch_size - 1) // batch_size
print(f'Will process in {total_batches} batches of {batch_size} repos each')

# Create batched queries
batches = []
for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    quoted_batch = [f"'{name}'" for name in batch]
    in_clause = ', '.join(quoted_batch)
    batches.append(in_clause)

print(f'Created {len(batches)} batches')
print('First batch in clause (first 200 chars):', batches[0][:200] + '...' if len(batches[0]) > 200 else batches[0])

output = {
    'total_repos': len(repo_names),
    'batch_size': batch_size,
    'total_batches': len(batches),
    'batch_preview': batches[0][:100] if batches else ''
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'repo_count': '114972'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
