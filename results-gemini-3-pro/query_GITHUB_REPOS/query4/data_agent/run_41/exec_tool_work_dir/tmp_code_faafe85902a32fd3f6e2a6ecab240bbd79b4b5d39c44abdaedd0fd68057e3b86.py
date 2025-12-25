code = """import json
import re

# Load commit counts
commits_data = locals()['var_function-call-10377723215053125974']
# commits_data is a list of dicts, e.g., [{"repo_name": "...", "commit_count": "..."}]

# Load languages data
languages_file = locals()['var_function-call-8032836620763171585']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Helper function to parse language description and get main language
def get_main_language(description):
    # Regex to find Language (Bytes bytes)
    # Allowing spaces in language names.
    # The byte count has commas, e.g. "22,438".
    matches = re.findall(r"([a-zA-Z0-9\+\-\#\.\s]+)\s\((\d{1,3}(?:,\d{3})*|\d+)\sbytes\)", description)
    
    if not matches:
        return None
    
    lang_bytes = {}
    for lang, bytes_str in matches:
        # Clean up language name (trim whitespace)
        lang = lang.strip()
        # Remove commas from bytes and convert to int
        bytes_count = int(bytes_str.replace(',', ''))
        lang_bytes[lang] = bytes_count
    
    # Return the language with max bytes
    if not lang_bytes:
        return None
    
    return max(lang_bytes, key=lang_bytes.get)

# Process languages
repo_main_langs = {}
for entry in languages_data:
    repo = entry['repo_name']
    desc = entry['language_description']
    main_lang = get_main_language(desc)
    if main_lang:
        repo_main_langs[repo] = main_lang

# Filter commit counts
filtered_commits = []
for entry in commits_data:
    repo = entry['repo_name']
    count = int(entry['commit_count'])
    
    # Check if we have language info
    if repo in repo_main_langs:
        main_lang = repo_main_langs[repo]
        # Check if main language is NOT Python
        if main_lang.lower() != 'python':
            filtered_commits.append({
                'repo_name': repo,
                'commit_count': count,
                'main_language': main_lang
            })

# Sort by commit count descending
filtered_commits.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = filtered_commits[:5]
top_5_repos = [x['repo_name'] for x in top_5]

print("__RESULT__:")
print(json.dumps(top_5_repos))"""

env_args = {'var_function-call-3505896804156068645': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-10377723215053125974': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-8032836620763171585': 'file_storage/function-call-8032836620763171585.json'}

exec(code, env_args)
