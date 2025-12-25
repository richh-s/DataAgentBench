code = """import json
import re
import pandas as pd

# Load languages
languages_file = locals()['var_function-call-9238785432583005607']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Load commits
commits_data = locals()['var_function-call-7775631221890929950']

# Convert to DataFrames
df_langs = pd.DataFrame(languages_data)
df_commits = pd.DataFrame(commits_data)

# Parse language description
def get_main_language(desc):
    if not isinstance(desc, str):
        return None
    # Regex to find "Language (Bytes bytes)"
    # Handles numbers with commas
    matches = re.findall(r'([A-Za-z0-9\+\#\-\.\s]+)\s\((\d[\d,]*)\sbytes\)', desc)
    if not matches:
        return None
    
    lang_stats = {}
    for lang, bytes_str in matches:
        lang = lang.strip()
        bytes_count = int(bytes_str.replace(',', ''))
        lang_stats[lang] = bytes_count
        
    if not lang_stats:
        return None
        
    # Find language with max bytes
    main_lang = max(lang_stats, key=lang_stats.get)
    return main_lang

df_langs['main_language'] = df_langs['language_description'].apply(get_main_language)

# Merge
# Note: repo_name is the key
# Ensure repo_name matches in both
df_merged = pd.merge(df_commits, df_langs, on='repo_name', how='inner')

# Filter out Python
# Case insensitive check might be good, but usually it's "Python"
df_filtered = df_merged[df_merged['main_language'] != 'Python']

# Sort by commit_count
df_filtered['commit_count'] = df_filtered['commit_count'].astype(int)
df_sorted = df_filtered.sort_values(by='commit_count', ascending=False)

# Get top 5
top_5 = df_sorted[['repo_name', 'main_language', 'commit_count']].head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-14608336121037298857': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-7775631221890929950': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-9238785432583005607': 'file_storage/function-call-9238785432583005607.json'}

exec(code, env_args)
