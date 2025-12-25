code = """import json
import re

# Load commit counts
commits_data = locals()['var_function-call-5940384259695713329']
# commits_data is a list of dicts: [{"repo_name": "...", "commit_count": "..."}]

# Load languages data
with open(locals()['var_function-call-569409992441780536'], 'r') as f:
    languages_data = json.load(f)

# Convert languages_data to a dict for easy lookup
languages_map = {item['repo_name']: item['language_description'] for item in languages_data}

repo_stats = []

for item in commits_data:
    repo_name = item['repo_name']
    commit_count = int(item['commit_count'])
    
    lang_desc = languages_map.get(repo_name)
    
    main_language = None
    if lang_desc:
        # Extract all matches of "Language (Bytes bytes)"
        # Regex needs to handle commas in numbers, e.g. "22,438"
        matches = re.findall(r'([a-zA-Z0-9#+]+) \(([\d,]+) bytes\)', lang_desc)
        
        max_bytes = -1
        for lang, bytes_str in matches:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_language = lang
    
    repo_stats.append({
        'repo_name': repo_name,
        'commit_count': commit_count,
        'main_language': main_language
    })

# Filter out Python
non_python_repos = [r for r in repo_stats if r['main_language'] != 'Python']

# Sort by commit count desc
non_python_repos.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = [r['repo_name'] for r in non_python_repos[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-1883824803817585683': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-5940384259695713329': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}], 'var_function-call-569409992441780536': 'file_storage/function-call-569409992441780536.json'}

exec(code, env_args)
