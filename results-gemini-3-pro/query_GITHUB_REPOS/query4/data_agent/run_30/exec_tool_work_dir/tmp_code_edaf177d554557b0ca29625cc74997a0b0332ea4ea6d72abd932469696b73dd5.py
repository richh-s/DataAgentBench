code = """import json
import re

# Load languages
with open(locals()['var_function-call-13484576814427699800'], 'r') as f:
    languages_data = json.load(f)

# Load commit counts
commits_data = locals()['var_function-call-13484576814427699867']

# Convert languages to a dict for easy lookup
repo_languages = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(description):
    if not description:
        return None
    # Regex to find Language (Bytes)
    # The language name can contain spaces, +, # (e.g., C++, C#)
    # The byte count has commas
    matches = re.findall(r'([A-Za-z0-9\+\#\-\.\s]+)\s\((\d[\d,]*) bytes\)', description)
    
    if not matches:
        return None
        
    parsed = []
    for lang, bytes_str in matches:
        # clean lang name (trim whitespace)
        lang = lang.strip()
        # parse bytes
        bytes_count = int(bytes_str.replace(',', ''))
        parsed.append((lang, bytes_count))
    
    if not parsed:
        return None
        
    # Sort by bytes desc
    parsed.sort(key=lambda x: x[1], reverse=True)
    return parsed[0][0]

results = []

for commit_info in commits_data:
    repo_name = commit_info['repo_name']
    commit_count = int(commit_info['commit_count'])
    
    lang_desc = repo_languages.get(repo_name)
    main_lang = get_main_language(lang_desc)
    
    # We want main language NOT Python
    # Be careful with case sensitivity, though usually it's "Python"
    if main_lang and main_lang.lower() != 'python':
        results.append({
            'repo_name': repo_name,
            'commit_count': commit_count,
            'main_language': main_lang
        })

# Sort by commit count desc
results.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = [r['repo_name'] for r in results[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-11742302900551546422': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11742302900551545127': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_function-call-13484576814427699800': 'file_storage/function-call-13484576814427699800.json', 'var_function-call-13484576814427699867': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'facebook/react', 'commit_count': '178'}]}

exec(code, env_args)
