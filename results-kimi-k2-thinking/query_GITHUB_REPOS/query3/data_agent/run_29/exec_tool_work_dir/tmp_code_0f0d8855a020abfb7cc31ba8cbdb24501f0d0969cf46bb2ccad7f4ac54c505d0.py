code = """import json

# Load repository names and perform join logic
result_file = locals()['var_functions.query_db:34']
with open(result_file, 'r') as f:
    shell_apache_repos = json.load(f)

shell_apache_repo_names = [item['repo_name'] for item in shell_apache_repos]
total_shell_apache_repos = len(shell_apache_repo_names)

print(f"Total Shell + Apache-2.0 repos: {total_shell_apache_repos}")

# Query all repos with valid commits from artifacts db
result_file2 = locals()['var_functions.query_db:53']
print(f"Repos with valid commits (any): {result_file2}")

# We need to identify which repos have valid commits AND match criteria
# Since there are only 15,016 commits total with these filters,
# let's find which repos they belong to
print('__RESULT__:')
print(json.dumps({
    'total_shell_apache_repos': total_shell_apache_repos,
    'total_valid_commits_all_repos': 15016,
    'repos_with_any_valid_commits': 6
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'commit_count': '15016'}], 'var_functions.query_db:7': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'last_five': ['dleehr/common-workflow-language', 'uc-cdis/cwl', 'veact/scala-ssh', 'm4kspl/scala-ssh', 'stdweird/aquilon']}, 'var_functions.query_db:14': [{'count': '659616'}], 'var_functions.query_db:15': [{'count': '495134'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_repo_count': 114972, 'batch_count': 115, 'batch_size': 1000}, 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:25': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'repo_count': '114972'}], 'var_functions.execute_python:32': {'test_batch_size': 1000, 'sample': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'test_repos_count': 100, 'sample_repos': ['0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon']}, 'var_functions.execute_python:38': {'repo_count': 1000, 'query_preview': "SELECT COUNT(*) as count FROM commits WHERE repo_name IN ('0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon', '001szymon/phonegap-app-desktop', '007slm/nutz', '00christian00/unity3d..."}, 'var_functions.execute_python:42': {'repo_count': 20, 'repos': ['0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon', '001szymon/phonegap-app-desktop', '007slm/nutz', '00christian00/unity3d-levelup', '00pauln00/yapio', '00wendi00/MyProject', '01000101/cloudify-cli', '01022499/end-to-end', '01Giovani/admProyectoAgua', '01alchemist/TurboScript', '01org/ciao', '01org/cloud-dleyna', '01org/cloud-neard', '01org/cloudeebus', '01org/graphbuilder', '01org/libyami', '01org/libyami-utils', '01org/rib']}, 'var_functions.query_db:44': [{'count': '0'}], 'var_functions.execute_python:48': {'total_repositories': 114972, 'first_repos': ['0--key/lib', '0-complexity/G8VDC', '0-complexity/whmcs-oauth2-addon', '001szymon/phonegap-app-desktop', '007slm/nutz'], 'batch_size': 100}, 'var_functions.execute_python:50': {'total_repos': 114972, 'batch_size': 500, 'total_batches': 230}, 'var_functions.query_db:52': [{'total_valid_commits': '15016'}], 'var_functions.query_db:53': [{'total_repos_with_commits': '6'}]}

exec(code, env_args)
