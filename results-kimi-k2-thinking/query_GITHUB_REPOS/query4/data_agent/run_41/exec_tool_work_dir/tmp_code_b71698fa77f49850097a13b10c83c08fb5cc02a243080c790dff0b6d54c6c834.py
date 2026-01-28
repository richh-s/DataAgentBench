code = """import pandas as pd
import json
import re
import os

# Debug: list available variables
print('Available variables:')
for var_name in list(locals().keys()):
    if var_name.startswith('var_'):
        print(f'{var_name}: {type(locals()[var_name])}')

# Get the data using the correct variable names
# The previous query results are stored in these variables
languages_result = locals()['var_functions.query_db:10']
commits_result = locals()['var_functions.query_db:34']

# Check if they're file paths or data
languages_data = None
if isinstance(languages_result, str) and os.path.isfile(languages_result):
    with open(languages_result, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = languages_result

commits_data = None  
if isinstance(commits_result, str) and os.path.isfile(commits_result):
    with open(commits_result, 'r') as f:
        commits_data = json.load(f)
else:
    commits_data = commits_result

print(f'Languages data type: {type(languages_data)}, length: {len(languages_data) if languages_data else 0}')
print(f'Commits data type: {type(commits_data)}, length: {len(commits_data) if commits_data else 0}')

if languages_data and commits_data:
    # Create DataFrames
    df_languages = pd.DataFrame(languages_data)
    df_commits = pd.DataFrame(commits_data)
    
    # Convert commit_count to int
    df_commits['commit_count'] = df_commits['commit_count'].astype(int)
    
    # Extract main language
    def get_main_language(desc):
        if pd.isna(desc):
            return None
        matches = re.findall(r'([A-Za-z0-9\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes\)', str(desc))
        if not matches:
            return None
        languages = {}
        for lang, bytes_str in matches:
            try:
                languages[lang] = int(bytes_str.replace(',', ''))
            except:
                continue
        return max(languages, key=languages.get) if languages else None
    
    df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)
    
    # Merge and filter
    merged = pd.merge(df_commits, df_languages[['repo_name', 'main_language']], on='repo_name', how='inner')
    non_python = merged[merged['main_language'] != 'Python']
    top5 = non_python.nlargest(5, 'commit_count')['repo_name'].tolist()
    
    print('Top 5 non-Python repos:', top5)
else:
    print('Could not load data')"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:4': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:16': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:28': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react'], 'var_functions.query_db:34': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
