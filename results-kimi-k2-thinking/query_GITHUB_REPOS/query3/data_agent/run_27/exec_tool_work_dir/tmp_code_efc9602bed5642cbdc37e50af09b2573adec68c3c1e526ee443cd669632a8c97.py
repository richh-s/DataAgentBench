code = """import json

# Read the repos list from the file
with open('file_storage/functions.query_db:10.json', 'r') as f:
    repos_data = json.load(f)

# Extract repo names
repo_names = [repo['repo_name'] for repo in repos_data]

# Create batched queries - let's start with a few repos to test
import math

# Let's batch in groups of 1000 repos
batch_size = 1000
batches = []
for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    # Create the IN clause for this batch
    batch_str = ', '.join([f"'{repo.replace("'", "''")}'" for repo in batch])
    batches.append(batch_str)

print('__RESULT__:')
print(json.dumps({
    'total_batches': len(batches),
    'first_batch': batches[0] if batches else '',
    'sample_repos': repo_names[:3]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'repo_count': 114972, 'first_5_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:20': [{'total_commits': '17976'}]}

exec(code, env_args)
