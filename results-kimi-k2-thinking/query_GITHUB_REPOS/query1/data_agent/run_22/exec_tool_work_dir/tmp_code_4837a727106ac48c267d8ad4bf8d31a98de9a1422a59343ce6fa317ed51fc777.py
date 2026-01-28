code = """import json, os

# Access variables directly by their keys
readme_key = 'var_functions.query_db:50'
non_python_key = 'var_functions.query_db:52'
total_repos_key = 'var_functions.query_db:54'

# Load README data
readme_file = locals()[readme_key].strip()
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Load non-Python repo data
non_python_file = locals()[non_python_key].strip()
with open(non_python_file, 'r') as f:
    non_python_data = json.load(f)

# Get total repos
total_repos = int(locals()[total_repos_key][0]['total_repos'])

print("README records:", len(readme_data))
print("Non-Python repos:", len(non_python_data))
print("Total repos:", total_repos)

# Extract repo names
readme_repos = [item['sample_repo_name'] for item in readme_data]
non_python_repo_names = set([item['repo_name'] for item in non_python_data])

# Find non-Python repos with READMEs
non_python_readme_repos = [repo for repo in readme_repos if repo in non_python_repo_names]
print("Non-Python repos with READMEs:", len(non_python_readme_repos))

# Check for copyright in READMEs
copyright_keywords = ['copyright', 'Copyright', '(c)', '(C)', '©']
repos_with_copyright = []

for item in readme_data:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repo_names:
        content = item['content']
        has_copyright = any(keyword in content for keyword in copyright_keywords)
        if has_copyright:
            repos_with_copyright.append(repo_name)

copyright_count = len(repos_with_copyright)
readme_count = len(non_python_readme_repos)

proportion = 0.0
if readme_count > 0:
    proportion = copyright_count / readme_count

print("Copyright count:", copyright_count)
print("README count:", readme_count)
print("Proportion:", proportion)

result = {
    "copyright_count": copyright_count,
    "readme_count": readme_count,
    "proportion": proportion,
    "proportion_percentage": round(proportion * 100, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': [{'total_repos': '3325634'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'readme_count': '195'}], 'var_functions.query_db:32': [{'non_python_count': '2774729'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.list_db:36': ['commits', 'contents', 'files'], 'var_functions.query_db:38': [{'total_count': '550905'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': [{'COUNT(*)': '550905'}], 'var_functions.execute_python:46': {'step': 'initialization', 'status': 'ready to query databases'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'total_repos': '3325634'}]}

exec(code, env_args)
