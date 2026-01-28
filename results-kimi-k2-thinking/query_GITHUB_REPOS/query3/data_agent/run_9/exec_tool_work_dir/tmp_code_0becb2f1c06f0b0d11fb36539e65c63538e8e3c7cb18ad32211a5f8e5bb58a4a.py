code = """import json

# Read the Apache-2.0 + Shell repos data
apache_shell_data = locals()['var_functions.query_db:6']

# If it's a file path, read from file
if isinstance(apache_shell_data, str) and apache_shell_data.endswith('.json'):
    with open(apache_shell_data, 'r') as f:
        apache_repos = json.load(f)
else:
    apache_repos = apache_shell_data

# Filter repos that contain Shell language
shell_repos = []
for repo in apache_repos:
    lang_desc = repo.get('language_description', '')
    if lang_desc != 'No language information available.' and 'Shell' in lang_desc:
        shell_repos.append(repo['repo_name'])

print(f"Found {len(shell_repos)} Apache-2.0 licensed repositories with Shell language")
print("First 10 repositories:", shell_repos[:10])

# Return just the list of repo names
result_str = json.dumps(shell_repos)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}, {'repo_name': 'gabrielduque/chrome-app-samples', 'license': 'apache-2.0'}, {'repo_name': 'robertwilczynski/Licensor', 'license': 'apache-2.0'}, {'repo_name': 'kinfkong/cordova-plugin-email-composer', 'license': 'apache-2.0'}, {'repo_name': 'EvgeneOskin/hello-love', 'license': 'apache-2.0'}, {'repo_name': 'ProgrammingRobotsStudyGroup/AndroidControl', 'license': 'apache-2.0'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
