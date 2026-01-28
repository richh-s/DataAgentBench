code = """import pandas as pd
import json
import re

# Get the full languages data
languages_path = var_functions.query_db:2
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

# Parse language_description to extract primary language
lang_list = []
for row in languages_data:
    desc = row['language_description']
    repo = row['repo_name']
    
    # Find language names with byte counts
    # Pattern looks for: language (bytes,)
    # Different patterns to match various formats
    patterns = [
        r"The majority of the code is in ([A-Za-z\+#]+) ",
        r"The codebase includes: ([A-Za-z\+#]+) ",
        r"While most of the project is built in ([A-Za-z\+#]+) ",
        r"This repository is mainly written in ([A-Za-z\+#]+) "
    ]
    
    primary_lang = None
    for pattern in patterns:
        match = re.search(pattern, desc)
        if match:
            primary_lang = match.group(1)
            break
    
    # Fallback: search for language with largest byte count
    if not primary_lang:
        # Extract all language-byte pairs
        lang_bytes = re.findall(r'([A-Za-z\+#]+) \((\d+(?:,\d+)*) bytes?\)', desc)
        if lang_bytes:
            # Find the one with max bytes
            max_bytes = 0
            for lang, bytes_str in lang_bytes:
                # Remove commas and convert to int
                try:
                    bytes_val = int(bytes_str.replace(',', ''))
                    if bytes_val > max_bytes:
                        max_bytes = bytes_val
                        primary_lang = lang
                except:
                    pass
    
    if primary_lang:
        lang_list.append({
            'repo_name': repo,
            'primary_language': primary_lang
        })

print('__RESULT__:')
print(json.dumps(lang_list[:5]))  # Just preview first 5"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
