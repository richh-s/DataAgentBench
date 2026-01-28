code = """import json
import re

# Load languages data
languages_file = locals()['var_functions.query_db:2']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Load commits data
commits_data = locals()['var_functions.query_db:5']

# Create commits dict for easy lookup
commits_dict = {item['repo_name']: int(item['commit_count']) for item in commits_data}

# Parse primary languages
non_python_langs = []
count = 0
python_only_count = 0
processed_count = 0

for rec in languages_data:
    desc = rec['language_description']
    repo = rec['repo_name']
    
    # Find primary language name
    primary_lang = None
    
    # Common patterns that indicate primary language
    patterns = [
        r"This repository is mainly written in ([A-Za-z\+#]+)",
        r"The majority of the code is in ([A-Za-z\+#]+)",
        r"While most of the project is built in ([A-Za-z\+#]+)",
        r"The codebase includes: ([A-Za-z\+#]+) \\(",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, desc)
        if match:
            primary_lang = match.group(1)
            break
    
    # If none of the patterns matched, parse language-byte pairs
    if not primary_lang:
        lang_bytes = re.findall(r'([A-Za-z\+#]+) \\((\\d+(?:,\\d+)*) bytes?\\)', desc)
        if lang_bytes:
            max_bytes = 0
            for lang, bytes_str in lang_bytes:
                try:
                    bytes_val = int(bytes_str.replace(',', ''))
                    if bytes_val > max_bytes:
                        max_bytes = bytes_val
                        primary_lang = lang
                except:
                    pass
    
    if primary_lang and primary_lang != 'Python':
        # Check if this repo has commit data
        if repo in commits_dict:
            non_python_langs.append({
                'repo_name': repo,
                'primary_language': primary_lang,
                'commit_count': commits_dict[repo]
            })
    
    processed_count += 1
    if processed_count % 100000 == 0:
        print(f"Processed {processed_count}")

# Sort by commit count descending
non_python_langs.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = non_python_langs[:5]

print(f"Found {len(non_python_langs)} non-Python repos with commit data")
print(f"Top 5: {top_5}")

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': {'loaded': 3325634}}

exec(code, env_args)
