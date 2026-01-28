code = """import json

# Access the variable using locals() as per instructions
lang_result = locals()['var_functions.query_db:7']
print("Type:", type(lang_result))
print("Content preview:", str(lang_result)[:200])

# Parse the result
if isinstance(lang_result, str):
    # It's likely a file path since the preview said it's too large
    if '\n' in lang_result or len(lang_result) < 500:
        # It's likely a string representation of JSON data
        lang_data = json.loads(lang_result)
    else:
        # It's a file path
        with open(lang_result, 'r') as f:
            lang_data = json.load(f)
else:
    lang_data = lang_result

print(f"\nLoaded {len(lang_data)} language records")

# Parse to find non-Python repos
import re

non_python_repos = []
python_count = 0

for item in lang_data:
    desc = item['language_description'].lower()
    # Check if it mentions Python
    if 'python' in desc:
        python_count += 1
    else:
        non_python_repos.append(item['repo_name'])

print(f"Repos with Python: {python_count}")
print(f"Repos without Python: {len(non_python_repos)}")
print(f"First 10 non-Python repos: {non_python_repos[:10]}")

result = {
    'non_python_repo_names': non_python_repos,
    'count_non_python': len(non_python_repos),
    'count_python': python_count,
    'total_repos': len(lang_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
