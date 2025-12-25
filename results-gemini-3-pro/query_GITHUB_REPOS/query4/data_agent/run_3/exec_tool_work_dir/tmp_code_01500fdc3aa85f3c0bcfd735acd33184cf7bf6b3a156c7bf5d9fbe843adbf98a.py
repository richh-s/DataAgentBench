code = """import json
import re

# Load the languages data
# The key for languages file is var_function-call-2030613790382563005
with open(locals()['var_function-call-2030613790382563005'], 'r') as f:
    languages_data = json.load(f)

# Load the commits data
# The key for commits data is var_function-call-2030613790382560744
commits_data = locals()['var_function-call-2030613790382560744']

# Convert languages_data to a dict for easy lookup
languages_map = {item['repo_name']: item['language_description'] for item in languages_data}

repo_info = []

for item in commits_data:
    repo_name = item['repo_name']
    commit_count = int(item['commit_count'])
    
    lang_desc = languages_map.get(repo_name, "")
    
    # Parse languages
    # Regex to find "Language (Bytes bytes)"
    # Examples: "Ruby (22,438 bytes)", "C++ (1,234 bytes)"
    matches = re.findall(r'([A-Za-z0-9\+\-\#\.]+)\s\((\d[\d,]*)\sbytes\)', lang_desc)
    
    max_bytes = 0
    main_lang = "Unknown"
    
    for lang, byte_str in matches:
        byte_count = int(byte_str.replace(',', ''))
        if byte_count > max_bytes:
            max_bytes = byte_count
            main_lang = lang
            
    repo_info.append({
        "repo_name": repo_name,
        "commit_count": commit_count,
        "main_language": main_lang
    })

# Filter out Python
non_python_repos = [r for r in repo_info if r['main_language'] != "Python"]

# Sort by commit count desc
sorted_repos = sorted(non_python_repos, key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = sorted_repos[:5]

result = [r['repo_name'] for r in top_5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3402374210778915406': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-3402374210778916207': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_function-call-2030613790382563005': 'file_storage/function-call-2030613790382563005.json', 'var_function-call-2030613790382560744': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
