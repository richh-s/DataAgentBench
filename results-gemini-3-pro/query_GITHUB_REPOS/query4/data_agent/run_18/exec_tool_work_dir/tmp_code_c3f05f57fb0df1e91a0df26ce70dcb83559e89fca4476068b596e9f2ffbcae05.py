code = """import json
import re

# Load commit counts
commits_data = locals()['var_function-call-993125701442150257']

# Parse and sort commits
repos_sorted = []
for entry in commits_data:
    try:
        r = entry['repo_name']
        c = int(entry['commit_count'])
        repos_sorted.append((r, c))
    except:
        continue

repos_sorted.sort(key=lambda x: x[1], reverse=True)

# Load languages data
languages_file_path = locals()['var_function-call-17748333109832134525']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Convert languages to a dict for fast lookup
# This might be memory intensive but should be fast enough if it fits
lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

# Regex
pattern = re.compile(r'([A-Za-z0-9\+\-\.# ]+?)\s+\(([\d,]+)\s+bytes\)')
stop_words = {'in', 'includes', 'built', 'written', 'incorporates', 'code', 'of', 'the', 'majority', 'followed', 'by', 'and', 'also', 'main', 'project', 'is', 'mostly', 'mainly', 'repository', 'with', 'additional', 'part', 'codebase', 'this'}

def is_not_python(desc):
    if not desc:
        return False
        
    matches = pattern.findall(desc)
    languages = {}
    for lang_str, bytes_str in matches:
        clean_lang = lang_str.strip()
        words = clean_lang.split()
        valid_words = []
        for w in words:
            w_clean = w.replace(':', '')
            if w_clean.lower() not in stop_words:
                valid_words.append(w_clean)
        
        if not valid_words:
            continue
            
        final_lang_name = " ".join(valid_words)
        
        try:
            bytes_count = int(bytes_str.replace(',', ''))
            languages[final_lang_name] = bytes_count
        except ValueError:
            continue
            
    if not languages:
        return False
        
    main_lang = max(languages, key=languages.get)
    return main_lang.lower() != 'python'

# Iterate through sorted repos and find top 5 non-python
results = []
for repo, count in repos_sorted:
    if repo in lang_map:
        desc = lang_map[repo]
        if is_not_python(desc):
            results.append(repo)
            if len(results) >= 5:
                break

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-14089913042029323930': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-993125701442150257': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17748333109832134525': 'file_storage/function-call-17748333109832134525.json'}

exec(code, env_args)
