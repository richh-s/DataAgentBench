code = """import pandas as pd
import json
import re
import os

# Get the data
languages_data = locals()['var_functions.query_db:10']
commits_data = locals()['var_functions.query_db:16']

# Handle file paths
if isinstance(languages_data, str) and os.path.isfile(languages_data):
    with open(languages_data, 'r') as f:
        languages_data = json.load(f)
if isinstance(commits_data, str) and os.path.isfile(commits_data):
    with open(commits_data, 'r') as f:
        commits_data = json.load(f)

# Create DataFrames
df_languages = pd.DataFrame(languages_data)
df_commits = pd.DataFrame(commits_data)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Check top commits
print('Top 6 repos by commits:')
print(df_commits.head(6))
print('\nLanguages dataset size:', len(df_languages))

# Function to extract main language
def get_main_language(desc):
    if pd.isna(desc):
        return None
    pattern = r'([A-Za-z0-9\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes\)'
    matches = re.findall(pattern, str(desc))
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

# Merge and get all matches
merged = pd.merge(df_commits, df_languages[['repo_name', 'main_language']], on='repo_name', how='inner')
print('\nMerged records:', len(merged))
print('Merged data:')
print(merged)

# Filter out Python and get top 5
non_python = merged[merged['main_language'] != 'Python']
print('\nNon-Python records:', len(non_python))
top5 = non_python.sort_values('commit_count', ascending=False).head(5)
print('\nTop 5 non-Python:')
print(top5)

# Get repository names
result = top5['repo_name'].tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:4': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:16': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:28': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react']}

exec(code, env_args)
