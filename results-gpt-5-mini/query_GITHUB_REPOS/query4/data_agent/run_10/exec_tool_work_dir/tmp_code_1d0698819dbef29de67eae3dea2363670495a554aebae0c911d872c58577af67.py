code = """import json
import re
import pandas as pd
# var_call_51RS7... is a file path to a JSON file containing languages records
languages_path = var_call_51RS7yKx5qvGcwh8QyogCD5K
with open(languages_path, 'r', encoding='utf-8') as f:
    languages_data = json.load(f)
commits_data = var_call_hjoz4dTptJXRXXi7QNyXw40Y

# Build mapping repo_name -> main_language
lang_map = {}
pattern = re.compile(r"([A-Za-z0-9#\+\-\. ]+?) \(([0-9,]+) bytes\)")
for rec in languages_data:
    repo = rec.get('repo_name')
    desc = rec.get('language_description','')
    matches = pattern.findall(desc)
    if matches:
        best_lang = None
        best_bytes = -1
        for lang, byte_str in matches:
            # normalize
            lang_clean = lang.strip()
            try:
                b = int(byte_str.replace(',',''))
            except:
                b = 0
            if b > best_bytes:
                best_bytes = b
                best_lang = lang_clean
        lang_map[repo] = best_lang
    else:
        # try a fallback: look for something like 'mainly written in X' or 'majority of the code is in X'
        m = re.search(r"(mainly written in|majority of the code is in|The codebase includes:|The majority of the code is in)\s*([A-Za-z0-9#\+\-\. ]+)", desc)
        if m:
            lang_map[repo] = m.group(2).strip()
        else:
            lang_map[repo] = None

# Process commits list and filter out Python main language
# commits_data is a list of dicts with repo_name and commit_count (strings)
filtered = []
for rec in commits_data:
    repo = rec.get('repo_name')
    try:
        count = int(rec.get('commit_count'))
    except:
        try:
            count = int(float(rec.get('commit_count')))
        except:
            count = 0
    main_lang = lang_map.get(repo)
    is_python = False
    if main_lang:
        if main_lang.strip().lower() == 'python':
            is_python = True
    # treat None as not Python (include)
    if not is_python:
        filtered.append({'repo_name': repo, 'commit_count': count, 'main_language': main_lang})

# Sort by commit_count desc
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)
# take top 5 repo names
top5 = [r['repo_name'] for r in filtered_sorted[:5]]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_u6M6DwxZidM33ArsfrNQurkd': ['languages', 'repos', 'licenses'], 'var_call_EbKYgJoHvDV4r0dwWDw0fhdB': ['commits', 'contents', 'files'], 'var_call_51RS7yKx5qvGcwh8QyogCD5K': 'file_storage/call_51RS7yKx5qvGcwh8QyogCD5K.json', 'var_call_hjoz4dTptJXRXXi7QNyXw40Y': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
