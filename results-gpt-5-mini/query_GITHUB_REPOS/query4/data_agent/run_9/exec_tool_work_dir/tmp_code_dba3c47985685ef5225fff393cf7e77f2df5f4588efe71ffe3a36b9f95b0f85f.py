code = """import json
import re

# Load the large languages result from the stored JSON file path
languages_file = var_call_37oivPXvbyFi6yaBpcUQl15b
with open(languages_file, 'r', encoding='utf-8') as f:
    languages_data = json.load(f)

# commits result is available as var_call_gHUxg4p977HFIACjR4H6Udxx
commits_data = var_call_gHUxg4p977HFIACjR4H6Udxx

# Build a mapping from repo_name to language_description
lang_map = {rec['repo_name']: rec.get('language_description', '') for rec in languages_data}

# Function to parse the main language from language_description
def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    # Find patterns like: LanguageName (12,345 bytes)
    pattern = re.compile(r"([A-Za-z0-9\+\#\- ]+?)\s*\(\s*([0-9,]+)\s*bytes\)")
    matches = pattern.findall(desc)
    if matches:
        best_lang = None
        best_bytes = -1
        for lang, bytes_str in matches:
            num = int(bytes_str.replace(',', ''))
            lang_clean = lang.strip()
            if num > best_bytes:
                best_bytes = num
                best_lang = lang_clean
        return best_lang
    # Fallback: try to find a single language mentioned without bytes
    # e.g., "This repository is mainly written in Ruby"
    m = re.search(r"mainly written in ([A-Za-z0-9\+\#\- ]+)", desc, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

# Build main language map for repos of interest (from commits_data)
main_lang_for_repo = {}
for rec in commits_data:
    rn = rec.get('repo_name')
    desc = lang_map.get(rn, '')
    main = parse_main_language(desc)
    main_lang_for_repo[rn] = main

# Filter commits where main language is not Python
filtered = []
for rec in commits_data:
    rn = rec.get('repo_name')
    try:
        count = int(rec.get('commit_count'))
    except:
        # if commit_count cannot be parsed, skip
        continue
    main = main_lang_for_repo.get(rn)
    if main is None:
        # If we don't have language info, skip the repo since we can't confirm it's not Python
        continue
    if main.lower() != 'python':
        filtered.append({'repo_name': rn, 'commit_count': count, 'main_language': main})

# Sort by commit_count desc and take top 5
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)[:5]
result_list = [r['repo_name'] for r in filtered_sorted]

import json as _json
print("__RESULT__:")
print(_json.dumps(result_list))"""

env_args = {'var_call_31OkCYRJpc2hPeWGZ88LNM6r': ['languages', 'repos', 'licenses'], 'var_call_1dqQAtFHM2YL0xbY1oRZIzit': ['commits', 'contents', 'files'], 'var_call_37oivPXvbyFi6yaBpcUQl15b': 'file_storage/call_37oivPXvbyFi6yaBpcUQl15b.json', 'var_call_gHUxg4p977HFIACjR4H6Udxx': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
