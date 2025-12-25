code = """import pandas as pd
import json
import re

# Load commit counts
commits_data = locals()['var_function-call-13422197844226042283']
df_commits = pd.DataFrame(commits_data)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Load languages
languages_file_path = locals()['var_function-call-18266229880342796841']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)
df_languages = pd.DataFrame(languages_data)

# Function to parse language description and get the main language
def get_main_language(desc):
    if not desc:
        return None
    # Regex to find Language (Bytes bytes)
    # The language name might contain spaces or symbols (e.g. C++, C#), so let's be careful.
    # Pattern: Look for word-like chars or symbols before " (", then digits and commas before " bytes)"
    # Example: Ruby (22,438 bytes)
    # Example: C++ (1,000 bytes)
    matches = re.findall(r'([a-zA-Z0-9+#\.\-\s]+?)\s+\(([\d,]+)\s+bytes\)', desc)
    
    if not matches:
        return None
    
    max_bytes = -1
    main_lang = None
    
    for lang, byte_str in matches:
        byte_count = int(byte_str.replace(',', ''))
        if byte_count > max_bytes:
            max_bytes = byte_count
            main_lang = lang.strip()
            
    return main_lang

df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)

# Merge
df_merged = pd.merge(df_commits, df_languages, on='repo_name', how='inner')

# Filter out Python
df_filtered = df_merged[df_merged['main_language'] != 'Python']

# Sort and top 5
df_top5 = df_filtered.sort_values(by='commit_count', ascending=False).head(5)

result = df_top5['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10029975301841261429': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13422197844226042283': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}], 'var_function-call-18266229880342796841': 'file_storage/function-call-18266229880342796841.json'}

exec(code, env_args)
