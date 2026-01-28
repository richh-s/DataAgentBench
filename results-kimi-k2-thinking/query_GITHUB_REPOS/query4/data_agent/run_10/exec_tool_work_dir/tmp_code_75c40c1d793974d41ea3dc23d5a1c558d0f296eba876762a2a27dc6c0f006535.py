code = """import json
import re
import pandas as pd

# Access the languages data directly from the variable
languages_data = var_functions.query_db:8

# Access the commit counts data directly from the variable  
commit_counts = var_functions.query_db:10

# Parse language descriptions to find main language
def parse_main_language(lang_desc):
    """Parse language description and return main language name."""
    if not lang_desc:
        return None
    
    # Extract language names and byte counts
    # Pattern looks like: "Language1 (bytes1 bytes), Language2 (bytes2 bytes)"
    pattern = r'([A-Za-z\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None
    
    # Find language with max bytes
    max_bytes = 0
    main_lang = None
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        if bytes_val > max_bytes:
            max_bytes = bytes_val
            main_lang = lang.strip()
    
    return main_lang

# Create DataFrame with main language
lang_df = pd.DataFrame(languages_data)
lang_df['main_language'] = lang_df['language_description'].apply(parse_main_language)

# Create DataFrame with commit counts
commits_df = pd.DataFrame(commit_counts)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# Merge dataframes
merged_df = pd.merge(lang_df, commits_df, on='repo_name', how='inner')

# Filter out Python repositories
non_python_df = merged_df[merged_df['main_language'] != 'Python']

# Sort by commit count descending and get top 5
top_5 = non_python_df.sort_values('commit_count', ascending=False).head(5)

result = top_5['repo_name'].tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
