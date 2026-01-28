code = """import json, re

# Load language data
lang_result = var_functions.query_db_8
if isinstance(lang_result, str) and lang_result.endswith('.json'):
    with open(lang_result, 'r') as f:
        languages = json.load(f)
else:
    languages = var_functions.query_db_8

# Load commit data
commit_result = var_functions.query_db_27
if isinstance(commit_result, str) and commit_result.endswith('.json'):
    with open(commit_result, 'r') as f:
        commit_counts = json.load(f)
else:
    commit_counts = var_functions.query_db_27

# Parse main languages
repo_main_lang = {}
for lang in languages:
    repo = lang['repo_name']
    desc = lang['language_description']
    matches = re.findall(r'(\w+)\s*\(([\d,]+)\s*bytes?\)', desc)
    lang_bytes = {}
    for name, byte_str in matches:
        lang_bytes[name] = int(byte_str.replace(',', ''))
    if lang_bytes:
        repo_main_lang[repo] = max(lang_bytes, key=lang_bytes.get)

# Filter non-Python repos
non_python = {}
for repo, lang in repo_main_lang.items():
    if lang != 'Python':
        non_python[repo] = lang

# Join with commits
joined = []
for commit in commit_counts:
    repo = commit['repo_name']
    if repo in non_python:
        joined.append({
            'repo': repo,
            'commits': int(commit['commit_count']),
            'lang': non_python[repo]
        })

# Get top 5
top5 = sorted(joined, key=lambda x: x['commits'], reverse=True)[:5]

# Build answer string
lines = []
for i in range(len(top5)):
    item = top5[i]
    line = str(i+1) + '. ' + item['repo'] + ' (Main language: ' + item['lang'] + ', Commits: ' + str(item['commits']) + ')'
    lines.append(line)

answer = '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:27': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
