code = """import json
import re

# Load languages data
lang_result = var_functions.query_db_28
if isinstance(lang_result, str) and lang_result.endswith('.json'):
    with open(lang_result, 'r') as f:
        languages = json.load(f)
else:
    languages = lang_result

# Load commit counts data
commit_result = var_functions.query_db_27
if isinstance(commit_result, str) and commit_result.endswith('.json'):
    with open(commit_result, 'r') as f:
        commit_data = json.load(f)
else:
    commit_data = commit_result

# Find main language for each repository
repo_languages = {}
for lang_info in languages:
    repo_name = lang_info['repo_name']
    lang_desc = lang_info['language_description']
    
    # Parse language bytes using regex
    lang_matches = re.findall(r'(\w+)\s*\(([\d,]+)\s*bytes?\)', lang_desc)
    lang_sizes = {}
    for lang_name, byte_count in lang_matches:
        lang_sizes[lang_name] = int(byte_count.replace(',', ''))
    
    if lang_sizes:
        main_lang = max(lang_sizes, key=lang_sizes.get)
        repo_languages[repo_name] = main_lang

# Filter repositories where main language is not Python
valid_repos = {}
for repo, lang in repo_languages.items():
    if lang != 'Python':
        valid_repos[repo] = lang

# Join with commit counts
combined = []
for commit_info in commit_data:
    repo_name = commit_info['repo_name']
    if repo_name in valid_repos:
        combined.append({
            'name': repo_name,
            'commits': int(commit_info['commit_count']),
            'language': valid_repos[repo_name]
        })

# Sort by commits descending and get top 5
combined.sort(key=lambda x: x['commits'], reverse=True)
top5 = combined[:5]

# Build final answer
result_parts = []
for i, repo in enumerate(top5, 1):
    part = '%d. %s (Main language: %s, Commits: %d)' % (
        i, repo['name'], repo['language'], repo['commits']
    )
    result_parts.append(part)

final_answer = '\n'.join(result_parts)
print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:27': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
