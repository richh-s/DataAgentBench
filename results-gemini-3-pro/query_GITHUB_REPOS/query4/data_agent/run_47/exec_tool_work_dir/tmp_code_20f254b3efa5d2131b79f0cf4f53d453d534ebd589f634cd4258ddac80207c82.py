code = """import json
import re

# Load data
commit_counts = locals()['var_function-call-11906576728718407279'] # list of dicts
languages_file_path = locals()['var_function-call-4293380210525377870'] # file path

with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Create a map of repo_name -> language_description
lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

filtered_repos = []

for item in commit_counts:
    repo = item['repo_name']
    count = int(item['commit_count'])
    
    desc = lang_map.get(repo)
    if not desc:
        # If no language info, assume not Python or handle accordingly. 
        # But usually we should have it. If not, maybe skip?
        # Let's verify if we find language info.
        print(f"Warning: No language info for {repo}")
        continue
        
    # Parse description
    # Regex to find Language (Bytes bytes)
    # Handling commas in numbers
    matches = re.findall(r'([A-Za-z0-9+#\-\.]+) \(([\d,]+) bytes\)', desc)
    
    lang_stats = {}
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        lang_stats[lang] = lang_stats.get(lang, 0) + bytes_val
        
    if not lang_stats:
        print(f"Warning: Could not parse languages for {repo}: {desc}")
        continue
        
    # Find main language
    main_lang = max(lang_stats, key=lang_stats.get)
    
    # Filter
    if main_lang.lower() != 'python':
        filtered_repos.append({
            'repo_name': repo,
            'commit_count': count,
            'main_language': main_lang
        })

# Sort by commit count descending
filtered_repos.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = filtered_repos[:5]
result_names = [r['repo_name'] for r in top_5]

print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_function-call-17360160857345551240': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9380818082236435302': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}], 'var_function-call-4293380210525377870': 'file_storage/function-call-4293380210525377870.json', 'var_function-call-11906576728718407279': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
