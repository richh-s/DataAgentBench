code = """import json
import re

# Load languages data from the provided file path variable
languages_file_path = var_call_SrkCWxqzavFu1yAMrxN45vdl
with open(languages_file_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Load commits data from storage variable
commits = var_call_hByYdvT1MQOs0DQMsWzORGlM

# Build dict of repo -> commit_count (int)
commit_counts = {}
for r in commits:
    repo = r.get('repo_name')
    cnt = r.get('commit_count')
    try:
        commit_counts[repo] = int(cnt)
    except Exception:
        # fallback if not int
        try:
            commit_counts[repo] = int(str(cnt))
        except Exception:
            commit_counts[repo] = 0

# Parse languages to determine main language
# Pattern to capture entries like 'Ruby (22,438 bytes)'
pat = re.compile(r"([^,(]+?)\s*\(([\d,]+)\s*bytes\)", re.IGNORECASE)

main_language = {}
for entry in languages:
    repo = entry.get('repo_name')
    desc = entry.get('language_description') or ''
    matches = pat.findall(desc)
    best_lang = None
    best_bytes = -1
    for m in matches:
        lang = m[0].strip()
        try:
            b = int(m[1].replace(',', ''))
        except:
            b = 0
        if b > best_bytes:
            best_bytes = b
            best_lang = lang
    # If no matches, try to infer single language words like 'This repository is mainly written in Ruby'
    if best_lang is None:
        # try simple word match for common languages
        common = ['Python','JavaScript','Java','C++','C#','C','Ruby','Go','Shell','TypeScript','PHP','Objective-C','Swift']
        for lang in common:
            if re.search(fr"\b{re.escape(lang)}\b", desc, re.IGNORECASE):
                best_lang = lang
                break
    if best_lang:
        main_language[repo] = best_lang

# Combine commit counts with main language, filter out Python main language
combined = []
for repo, cnt in commit_counts.items():
    lang = main_language.get(repo)
    if lang is None:
        # If language unknown, treat as not Python (can't assume Python), include
        is_python = False
    else:
        is_python = (lang.strip().lower() == 'python')
    if not is_python:
        combined.append({'repo_name': repo, 'commit_count': cnt, 'main_language': lang})

# Sort by commit_count desc and take top 5
combined_sorted = sorted(combined, key=lambda x: x['commit_count'], reverse=True)
top5 = [r['repo_name'] for r in combined_sorted[:5]]

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_SrkCWxqzavFu1yAMrxN45vdl': 'file_storage/call_SrkCWxqzavFu1yAMrxN45vdl.json', 'var_call_hByYdvT1MQOs0DQMsWzORGlM': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
