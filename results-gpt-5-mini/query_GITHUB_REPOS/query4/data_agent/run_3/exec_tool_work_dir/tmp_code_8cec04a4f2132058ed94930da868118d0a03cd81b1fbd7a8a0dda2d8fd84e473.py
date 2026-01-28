code = """import json
import re

# Load the large languages result from the JSON file path stored in var_call_2p9XtuMlyLw1aHvn5ru8kSLs
with open(var_call_2p9XtuMlyLw1aHvn5ru8kSLs, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Commits data is available directly in var_call_nmDbB7XVG8HysBCQY7252yad
commits = var_call_nmDbB7XVG8HysBCQY7252yad

# Helper to extract main language from language_description
lang_pattern = re.compile(r"([A-Za-z0-9\+\#\.\- ]+?) \(([\d,]+) bytes\)")

main_lang_by_repo = {}
for rec in languages:
    repo = rec.get('repo_name')
    desc = rec.get('language_description') or ''
    matches = lang_pattern.findall(desc)
    if matches:
        # matches is list of tuples (lang, bytes_str)
        max_lang = None
        max_bytes = -1
        for lang, bytes_str in matches:
            try:
                b = int(bytes_str.replace(',', ''))
            except:
                b = 0
            if b > max_bytes:
                max_bytes = b
                max_lang = lang.strip()
        if max_lang:
            main_lang_by_repo[repo] = max_lang

# Build list of commits entries with commit_count as int
commit_list = []
for rec in commits:
    repo = rec.get('repo_name')
    cc = rec.get('commit_count')
    try:
        count = int(cc)
    except:
        try:
            count = int(str(cc).replace(',', ''))
        except:
            count = 0
    commit_list.append({'repo_name': repo, 'commit_count': count})

# Filter out repos whose main language is Python (case-insensitive)
filtered = []
for rec in commit_list:
    repo = rec['repo_name']
    main_lang = main_lang_by_repo.get(repo)
    if main_lang is None:
        # If we don't have language info, skip
        continue
    if main_lang.lower() == 'python':
        continue
    filtered.append(rec)

# Sort by commit_count desc and take top 5
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)
top5 = [r['repo_name'] for r in filtered_sorted[:5]]

import json as _json
print("__RESULT__:")
print(_json.dumps(top5))"""

env_args = {'var_call_Nz2nivxBl23R4zvfdF8SWTaJ': ['languages', 'repos', 'licenses'], 'var_call_eKqUR1JIU7cuvHjdPCamNQd7': ['commits', 'contents', 'files'], 'var_call_2p9XtuMlyLw1aHvn5ru8kSLs': 'file_storage/call_2p9XtuMlyLw1aHvn5ru8kSLs.json', 'var_call_nmDbB7XVG8HysBCQY7252yad': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
