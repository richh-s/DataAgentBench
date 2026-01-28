code = """import json
import os

# Load the commit data
commits_data = var_functions.query_db:10

# Load the language data - check if it's a file path or direct data
languages_data = var_functions.query_db:8
# If languages_data is a string (file path), load it
if isinstance(languages_data, str):
    with open(languages_data, 'r') as f:
        languages_data = json.load(f)

# Debug: print type and sample
print(f"Type of commits_data: {type(commits_data)}")
print(f"Type of languages_data: {type(languages_data)}")
print(f"Sample commits_data: {commits_data[:3] if commits_data else 'Empty'}")
print(f"Sample languages_data: {languages_data[:3] if languages_data else 'Empty'}")

# Convert to DataFrames
import pandas as pd

commits_df = pd.DataFrame(commits_data)
languages_df = pd.DataFrame(languages_data)

print(f"Commits dataframe shape: {commits_df.shape}")
print(f"Languages dataframe shape: {languages_df.shape}")

# Display sample data
print("Sample commits data:")
print(commits_df.head())
print("\nSample languages data:")
print(languages_df.head())

# Parse language descriptions to find primary language (language with most bytes)
import re

def extract_primary_language(lang_desc):
    """Extract the primary language from language_description field."""
    if not lang_desc:
        return None
    
    # Look for patterns like "Ruby (22,438 bytes)" or "Shell (465 bytes)"
    # The primary language should have the highest byte count
    matches = re.findall(r'([A-Za-z\+#]+)\s*\(([\d,]+)\s+bytes\)', lang_desc)
    
    if not matches:
        return None
    
    # Convert to dict and find max by byte count
    lang_bytes = {}
    for lang, bytes_str in matches:
        try:
            byte_count = int(bytes_str.replace(',', ''))
            lang_bytes[lang] = byte_count
        except:
            continue
    
    if not lang_bytes:
        return None
    
    # Return language with max bytes
    primary_lang = max(lang_bytes, key=lang_bytes.get)
    return primary_lang

# Apply to languages_df
languages_df['primary_language'] = languages_df['language_description'].apply(extract_primary_language)

print("\nLanguages with primary language extracted:")
print(languages_df[['repo_name', 'language_description', 'primary_language']].head(10))

# Merge commits with languages
merged_df = commits_df.merge(languages_df[['repo_name', 'primary_language']], on='repo_name', how='left')

print(f"\nMerged dataframe shape: {merged_df.shape}")
print("Sample merged data:")
print(merged_df.head())

# Filter out repos where primary_language is Python
non_python_df = merged_df[merged_df['primary_language'] != 'Python']

print(f"\nNon-Python repos count: {len(non_python_df)}")

# Order by commit_count descending and take top 5
top_5_repos = non_python_df.sort_values('commit_count', ascending=False).head(5)

print("\nTop 5 non-Python repos by commit count:")
print(top_5_repos[['repo_name', 'commit_count', 'primary_language']])

# Get just the repo names
result_repos = top_5_repos['repo_name'].tolist()

# Prepare final result
result_json = json.dumps(result_repos)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
