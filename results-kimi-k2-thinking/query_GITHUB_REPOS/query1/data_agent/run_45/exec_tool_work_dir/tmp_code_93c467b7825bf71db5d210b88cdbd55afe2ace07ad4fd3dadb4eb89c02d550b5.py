code = """import pandas as pd
import json

# Load the initial query results
languages_data = [
    {"repo_name": "juliandunn/rackspacecloud", "language_description": "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."},
    {"repo_name": "xMarkusSpringerx/coloranalyzer", "language_description": "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."},
    {"repo_name": "michaellihs/gitlab", "language_description": "The codebase includes: Ruby (162,002 bytes), Shell (168 bytes)."},
    {"repo_name": "vyorkin/xftp", "language_description": "The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes)."},
    {"repo_name": "airatshigapov/drophunter", "language_description": "The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes)."},
    {"repo_name": "tombruijn/chef-ruby-install", "language_description": "While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes)."},
    {"repo_name": "SenseTecnic/stsplatform-lib-ruby", "language_description": "While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes)."},
    {"repo_name": "procore/site-reliability-scripts", "language_description": "The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes)."},
    {"repo_name": "tibastral/web_motion", "language_description": "The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes)."},
    {"repo_name": "Haegin/stately", "language_description": "The codebase includes: Ruby (8,171 bytes), Shell (131 bytes)."},
    {"repo_name": "Scripted/pandago-ruby", "language_description": "This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes)."},
    {"repo_name": "wallywest/magnum", "language_description": "The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes)."},
    {"repo_name": "kuleszaj/chef-an-introduction", "language_description": "While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes)."},
    {"repo_name": "ruby-amqp/rabbitmq_http_api_client", "language_description": "While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes)."},
    {"repo_name": "rupakg/lorry", "language_description": "While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes)."},
    {"repo_name": "rmomogi/validator_ie", "language_description": "While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes)."},
    {"repo_name": "MailRoute/mailroute_ruby", "language_description": "While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes)."},
    {"repo_name": "Nordstrom/al_agents", "language_description": "The codebase includes: Ruby (11,538 bytes), Shell (862 bytes)."},
    {"repo_name": "Pixelshifter/My-cloud-PoC-Ansible-Vagrant", "language_description": "The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes)."},
    {"repo_name": "enspiresoftware/n_able_rails", "language_description": "While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes)."}
]

df_languages = pd.DataFrame(languages_data)
print('Total repositories:', len(df_languages))
print('Repositories that do NOT use Python:')
non_python_repos = []
for _, row in df_languages.iterrows():
    if 'ython' not in row['language_description']:
        non_python_repos.append(row['repo_name'])
        print(f"- {row['repo_name']}: {row['language_description']}")

print(f'\nTotal non-Python repositories: {len(non_python_repos)}')

# Check the contents data to see README.md files
print('\n--- Contents data sample ---')
import ast
with open('/tmp/tmp0cwp1z0f.json', 'r') as f:
    contents_data = json.load(f)
    
df_contents = pd.DataFrame(contents_data)
readme_files = df_contents[df_contents['sample_path'].str.contains('README', case=False, na=False)]
print(f'Number of files with README in path: {len(readme_files)}')
if len(readme_files) > 0:
    print('Sample README files:')
    for idx, row in readme_files.head().iterrows():
        print(f"  - {row['sample_path']} in {row['sample_repo_name']}")
        print(f"    Content length: {len(row['content']) if row['content'] else 0}")
        print(f"    Is README.md: {'README.md' in str(row['sample_path']).upper()}")
        
    # Count README.md specifically
    readme_md_files = df_contents[df_contents['sample_path'].str.upper().str.endswith('README.MD')]
    print(f'\nNumber of README.md files: {len(readme_md_files)}')

# Print result
result = {
    'total_non_python_repos': len(non_python_repos),
    'non_python_repos': non_python_repos
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
