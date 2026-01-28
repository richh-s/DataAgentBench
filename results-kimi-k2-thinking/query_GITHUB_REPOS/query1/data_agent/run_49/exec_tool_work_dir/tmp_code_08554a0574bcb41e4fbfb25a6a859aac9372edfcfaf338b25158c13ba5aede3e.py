code = """import json
import re

# Load the repository languages data directly from the file path mentioned in the previous result
languages_file_path = '/tmp/tmpm9n9_8d5.json'
readme_file_path = '/tmp/tmpy3jxy4u8.json'

# Load data
try:
    with open(languages_file_path, 'r') as f:
        languages_data = json.load(f)
    
    with open(readme_file_path, 'r') as f:
        readme_data = json.load(f)
    
    # Analyze which repositories use Python
    non_python_repos = []
    for lang_record in languages_data:
        repo_name = lang_record['repo_name']
        lang_desc = lang_record['language_description']
        # Check if Python is mentioned (case-insensitive)
        if not re.search(r'python', lang_desc, re.IGNORECASE):
            non_python_repos.append(repo_name)
    
    # Find READMEs for non-Python repositories
    non_python_readmes = []
    copyright_repos = []
    
    for readme_record in readme_data:
        repo_name = readme_record['sample_repo_name']
        if repo_name in non_python_repos:
            non_python_readmes.append(repo_name)
            content = readme_record['content'] or ''
            # Check for copyright indicators
            if re.search(r'copyright|\(c\)|\u00a9|all rights reserved', content, re.IGNORECASE):
                copyright_repos.append(repo_name)
    
    # Calculate proportion
    total_non_python_readmes = len(non_python_readmes)
    copyright_count = len(copyright_repos)
    
    proportion = copyright_count / total_non_python_readmes if total_non_python_readmes > 0 else 0
    
    print('__RESULT__:')
    print(json.dumps({
        'total_non_python_repos': len(non_python_repos),
        'non_python_repos_with_readme': total_non_python_readmes,
        'non_python_repos_with_copyright': copyright_count,
        'proportion': proportion,
        'proportion_percentage': f"{proportion:.2%}"
    }))
    
except FileNotFoundError as e:
    print('__RESULT__:')
    print(json.dumps({
        'error': f'File not found: {str(e)}'
    }))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'repo_name': 'Scripted/pandago-ruby', 'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'repo_name': 'wallywest/magnum', 'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'repo_name': 'kuleszaj/chef-an-introduction', 'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client', 'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'repo_name': 'rupakg/lorry', 'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'repo_name': 'rmomogi/validator_ie', 'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'repo_name': 'MailRoute/mailroute_ruby', 'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'repo_name': 'Nordstrom/al_agents', 'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'repo_name': 'enspiresoftware/n_able_rails', 'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (11,276 bytes), with additional code in Shell (131 bytes).'}, {'language_description': 'The majority of the code is in Ruby (184,928 bytes), followed by Shell (146 bytes).'}, {'language_description': 'While most of the project is built in Ruby (12,007 bytes), it also incorporates Shell (179 bytes).'}, {'language_description': 'While most of the project is built in Ruby (51,928 bytes), it also incorporates Shell (3,165 bytes).'}, {'language_description': 'While most of the project is built in Ruby (53,705 bytes), it also incorporates Shell (205 bytes).'}, {'language_description': 'While most of the project is built in Ruby (49,442 bytes), it also incorporates Shell (131 bytes).'}, {'language_description': 'While most of the project is built in Ruby (74,892 bytes), it also incorporates Shell (173 bytes).'}, {'language_description': 'The codebase includes: Ruby (11,538 bytes), Shell (862 bytes).'}, {'language_description': 'The majority of the code is in Ruby (3,705 bytes), followed by Shell (2,867 bytes).'}, {'language_description': 'While most of the project is built in Ruby (4,438 bytes), it also incorporates Shell (131 bytes).'}, {'language_description': 'The codebase includes: Shell (21,286 bytes), Ruby (2,160 bytes).'}, {'language_description': 'While most of the project is built in Ruby (1,881 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (1,314 bytes), Shell (681 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (15,739 bytes), with additional code in Shell (131 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (4,276 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (4,015 bytes), with additional code in Shell (131 bytes).'}, {'language_description': 'The majority of the code is in Ruby (19,238 bytes), followed by Shell (164 bytes).'}, {'language_description': 'The majority of the code is in Ruby (54,423 bytes), followed by Shell (2,392 bytes).'}, {'language_description': 'The majority of the code is in Ruby (111,682 bytes), followed by Shell (131 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (20,232 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (7,266 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (2,385 bytes), followed by Shell (131 bytes).'}, {'language_description': 'The majority of the code is in Ruby (166,544 bytes), followed by Shell (97 bytes).'}, {'language_description': 'While most of the project is built in Ruby (23,000 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (10,355 bytes), followed by Shell (79 bytes).'}, {'language_description': 'The codebase includes: Ruby (10,236 bytes), Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,729 bytes), followed by Shell (65 bytes).'}, {'language_description': 'While most of the project is built in Ruby (4,612 bytes), it also incorporates Shell (2,001 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (19,738 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Shell (3,715 bytes), followed by Ruby (931 bytes).'}, {'language_description': 'While most of the project is built in Ruby (9,838 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (6,783 bytes), it also incorporates Shell (74 bytes).'}, {'language_description': 'The majority of the code is in Ruby (3,890 bytes), followed by Shell (2,968 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (10,068 bytes), with additional code in Shell (197 bytes).'}, {'language_description': 'The codebase includes: Shell (3,278 bytes), Ruby (466 bytes).'}, {'language_description': 'The codebase includes: Ruby (204,117 bytes), Shell (5,424 bytes).'}, {'language_description': 'The codebase includes: Ruby (119,135 bytes), Shell (8,272 bytes).'}, {'language_description': 'While most of the project is built in Ruby (37,356 bytes), it also incorporates Shell (7,719 bytes).'}, {'language_description': 'While most of the project is built in Ruby (40,345 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (198,785 bytes), Shell (428 bytes).'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:26': ['commits', 'contents', 'files']}

exec(code, env_args)
