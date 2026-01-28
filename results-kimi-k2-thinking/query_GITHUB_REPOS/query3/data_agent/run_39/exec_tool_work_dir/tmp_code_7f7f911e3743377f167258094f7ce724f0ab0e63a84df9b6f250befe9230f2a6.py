code = """# Load the commits and filter them to our target repositories
import json

# Load commits that meet the message criteria
commits_file_path = "file_storage/functions.query_db:42.json"
with open(commits_file_path, 'r') as f:
    commits = json.load(f)

# Load the repositories that use Shell and have Apache-2.0 license
with open("file_storage/functions.query_db:30.json", 'r') as f:
    common_repos = json.load(f)

# Create a set of common repo names for fast lookup
common_repo_names = {repo['repo_name'] for repo in common_repos}

# Filter commits to only those from common repositories
filtered_commits = []
for commit in commits:
    if commit['repo_name'] in common_repo_names:
        filtered_commits.append(commit)

print("__RESULT__:")
result = {
    'total_commits_filtered': len(commits),
    'target_commits_count': len(filtered_commits),
    'sample_commits': filtered_commits[:3] if filtered_commits else []
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}, {'repo_name': 'gabrielduque/chrome-app-samples', 'license': 'apache-2.0'}, {'repo_name': 'robertwilczynski/Licensor', 'license': 'apache-2.0'}, {'repo_name': 'kinfkong/cordova-plugin-email-composer', 'license': 'apache-2.0'}, {'repo_name': 'EvgeneOskin/hello-love', 'license': 'apache-2.0'}, {'repo_name': 'ProgrammingRobotsStudyGroup/AndroidControl', 'license': 'apache-2.0'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:4', 'var_functions.query_db:6', 'var_functions.query_db:8'], 'key_info': {'var_functions.query_db:0': {'type': 'list', 'length': 10, 'first_item': {'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}}, 'var_functions.query_db:2': {'type': 'list', 'length': 10, 'first_item': {'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}}, 'var_functions.query_db:4': {'type': 'str', 'preview': 'file_storage/functions.query_db:4.json'}, 'var_functions.query_db:6': {'type': 'str', 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': 'str', 'preview': 'file_storage/functions.query_db:8.json'}}}, 'var_functions.execute_python:18': {'apache_repos_count': 495134, 'shell_repos_count': 659616, 'apache_preview': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}], 'shell_preview': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'common_repos_count': 114972, 'first_few_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:38': {'total_repos': 114972, 'batch_size': 500, 'total_batches': 230}, 'var_functions.query_db:40': [{'total': '15019'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
