code = """import json
import sqlite3
import os

# Load all the repositories that match our criteria
result_file = locals()['var_functions.query_db:34']
with open(result_file, 'r') as f:
    all_repos = json.load(f)

repo_names = [item['repo_name'] for item in all_repos]
total_repos = len(repo_names)

print(f"Total repositories to check: {total_repos}")
print(f"First 5 repos: {repo_names[:5]}")
print(f"Last 5 repos: {repo_names[-5:] if total_repos > 5 else []}")

# We'll need to process these in batches and query the DuckDB
# Let's prepare a query template
query_template = """
SELECT COUNT(*) as count 
FROM commits 
WHERE repo_name IN ({repos})
  AND message IS NOT NULL 
  AND LENGTH(message) < 1000 
  AND LOWER(message) NOT LIKE 'merge%' 
  AND LOWER(message) NOT LIKE 'update%' 
  AND LOWER(message) NOT LIKE 'test%'
"""

# Process first 100 repos as a test batch
batch = repo_names[:100]
batch_str = "', '".join(batch)
test_query = query_template.format(repos=f"'{batch_str}'")

batch_info = {
    'total_repositories': total_repos,
    'test_batch_size': len(batch),
    'query_preview': test_query[:200] + '...'
}

print('__RESULT__:')
print(json.dumps(batch_info))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'commit_count': '15016'}], 'var_functions.query_db:7': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'last_five': ['dleehr/common-workflow-language', 'uc-cdis/cwl', 'veact/scala-ssh', 'm4kspl/scala-ssh', 'stdweird/aquilon']}, 'var_functions.query_db:14': [{'count': '659616'}], 'var_functions.query_db:15': [{'count': '495134'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_repo_count': 114972, 'batch_count': 115, 'batch_size': 1000}, 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:25': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'repo_count': '114972'}], 'var_functions.execute_python:32': {'test_batch_size': 1000, 'sample': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'test_repos_count': 100, 'sample_repos': ['0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon']}, 'var_functions.execute_python:38': {'repo_count': 1000, 'query_preview': "SELECT COUNT(*) as count FROM commits WHERE repo_name IN ('0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon', '001szymon/phonegap-app-desktop', '007slm/nutz', '00christian00/unity3d..."}, 'var_functions.execute_python:42': {'repo_count': 20, 'repos': ['0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon', '001szymon/phonegap-app-desktop', '007slm/nutz', '00christian00/unity3d-levelup', '00pauln00/yapio', '00wendi00/MyProject', '01000101/cloudify-cli', '01022499/end-to-end', '01Giovani/admProyectoAgua', '01alchemist/TurboScript', '01org/ciao', '01org/cloud-dleyna', '01org/cloud-neard', '01org/cloudeebus', '01org/graphbuilder', '01org/libyami', '01org/libyami-utils', '01org/rib']}, 'var_functions.query_db:44': [{'count': '0'}]}

exec(code, env_args)
