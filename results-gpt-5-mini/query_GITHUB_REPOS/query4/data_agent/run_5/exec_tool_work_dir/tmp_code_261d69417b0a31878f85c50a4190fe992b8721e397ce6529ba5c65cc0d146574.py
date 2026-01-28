code = """import json
import re
import pandas as pd

# Load languages data from file path stored in var_call_nNal9OREDp007BMcY0uTZ0kl
languages_path = var_call_nNal9OREDp007BMcY0uTZ0kl
with open(languages_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Load commits aggregation result
commits = var_call_YuX2j5G6opeVFbgP7wjHIO9K

# Build repo -> main language mapping
lang_pattern = re.compile(r"([A-Za-z0-9\+#\. ]+?)\s*\(([\d,]+)\s*bytes\)")
repo_main_lang = {}
for rec in languages:
    repo = rec.get('repo_name')
    desc = rec.get('language_description','')
    matches = lang_pattern.findall(desc)
    best_lang = None
    best_bytes = -1
    for m in matches:
        lang = m[0].strip()
        num = int(m[1].replace(',',''))
        if num > best_bytes:
            best_bytes = num
            best_lang = lang
    repo_main_lang[repo] = best_lang

# Combine with commits, convert commit_count to int
combined = []
for rec in commits:
    repo = rec.get('repo_name')
    cnt = rec.get('commit_count')
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(str(cnt).replace(',',''))
        except:
            cnt_int = 0
    main_lang = repo_main_lang.get(repo)
    combined.append({'repo_name': repo, 'commit_count': cnt_int, 'main_language': main_lang})

# Filter out repos whose main language is Python (case-insensitive)
filtered = [r for r in combined if not (r['main_language'] and r['main_language'].strip().lower()=='python')]

# Sort by commit_count desc and take top 5
sorted_repos = sorted(filtered, key=lambda r: r['commit_count'], reverse=True)
top5 = [r['repo_name'] for r in sorted_repos[:5]]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_gmzDRL6QggudruYF9qMDxmh9': ['languages', 'repos', 'licenses'], 'var_call_v0kVivwLpizgrZBKgwC68WUa': ['commits', 'contents', 'files'], 'var_call_nNal9OREDp007BMcY0uTZ0kl': 'file_storage/call_nNal9OREDp007BMcY0uTZ0kl.json', 'var_call_YuX2j5G6opeVFbgP7wjHIO9K': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
