code = """import json

# Read the shell repos list
shell_repos_data = locals()['var_functions.query_db:18']

# If it's a file path, read from file
if isinstance(shell_repos_data, str) and shell_repos_data.endswith('.json'):
    with open(shell_repos_data, 'r') as f:
        shell_repos_list = json.load(f)
else:
    shell_repos_list = shell_repos_data

# Extract repo names
shell_repos = [repo['repo_name'] for repo in shell_repos_list]
print(f"Total repos: {len(shell_repos)}")

# Build query with proper escaping
repo_list = ", ".join(["'" + repo.replace("'", "''") + "'" for repo in shell_repos])
query = "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN (" + repo_list + ") AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%'"

result_str = json.dumps(query)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}, {'repo_name': 'gabrielduque/chrome-app-samples', 'license': 'apache-2.0'}, {'repo_name': 'robertwilczynski/Licensor', 'license': 'apache-2.0'}, {'repo_name': 'kinfkong/cordova-plugin-email-composer', 'license': 'apache-2.0'}, {'repo_name': 'EvgeneOskin/hello-love', 'license': 'apache-2.0'}, {'repo_name': 'ProgrammingRobotsStudyGroup/AndroidControl', 'license': 'apache-2.0'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': "SELECT repo_name, message FROM commits WHERE repo_name IN ('jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts') LIMIT 20", 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
