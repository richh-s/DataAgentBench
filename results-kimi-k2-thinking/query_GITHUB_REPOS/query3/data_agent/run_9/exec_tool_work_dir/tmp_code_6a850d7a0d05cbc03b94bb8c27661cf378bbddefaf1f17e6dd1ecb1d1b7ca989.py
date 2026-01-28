code = """# We have 114,972 Apache-2.0 repos with Shell. Now we need to find which ones have commit data.
# Let's batch the queries more intelligently.

import json

# Read shell repos list
shell_repos_data = locals()['var_functions.query_db:18']
if isinstance(shell_repos_data, str) and shell_repos_data.endswith('.json'):
    with open(shell_repos_data, 'r') as f:
        shell_repos_list = json.load(f)
else:
    shell_repos_list = shell_repos_data

shell_repos = [repo['repo_name'] for repo in shell_repos_list]
print(f"Total Apache-2.0 Shell repos: {len(shell_repos)}")
print(f"Sample: {shell_repos[:10]}")

# Check if any of our repos have commits by taking a small sample of 100 repos
sample_repos = shell_repos[:100]
repo_list_str = ", ".join([f"'{repo}'" for repo in sample_repos])

# Build query for sample
query = f"SELECT repo_name, COUNT(*) as total FROM commits WHERE repo_name IN ({repo_list_str}) GROUP BY repo_name LIMIT 20"
result_str = json.dumps(query)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}, {'repo_name': 'gabrielduque/chrome-app-samples', 'license': 'apache-2.0'}, {'repo_name': 'robertwilczynski/Licensor', 'license': 'apache-2.0'}, {'repo_name': 'kinfkong/cordova-plugin-email-composer', 'license': 'apache-2.0'}, {'repo_name': 'EvgeneOskin/hello-love', 'license': 'apache-2.0'}, {'repo_name': 'ProgrammingRobotsStudyGroup/AndroidControl', 'license': 'apache-2.0'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': "SELECT repo_name, message FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts') LIMIT 20", 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:26': [{'count': '0'}], 'var_functions.query_db:28': [{'count': '0'}], 'var_functions.list_db:30': ['commits', 'contents', 'files'], 'var_functions.query_db:32': [{'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'facebook/react'}], 'var_functions.query_db:34': [], 'var_functions.query_db:36': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}], 'var_functions.execute_python:38': ['tensorflow/tensorflow', 'Microsoft/TypeScript', 'apache/maven', 'lxc/lxd', 'doximity/docker-redis'], 'var_functions.query_db:40': [{'repo_name': 'tensorflow/tensorflow', 'count': '156'}]}

exec(code, env_args)
