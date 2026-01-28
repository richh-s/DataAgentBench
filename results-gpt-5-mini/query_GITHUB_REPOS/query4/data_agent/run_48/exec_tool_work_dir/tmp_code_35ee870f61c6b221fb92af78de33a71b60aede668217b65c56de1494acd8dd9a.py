code = """import json, re

# variables from storage:
# var_call_2OLOOa3qdF3nbLVNj7j94Atk -> path to JSON file with languages data
# var_call_OJK9SLtjBYyckyKeqLcD983O -> list of commit counts

languages_path = var_call_2OLOOa3qdF3nbLVNj7j94Atk
with open(languages_path, 'r', encoding='utf-8') as f:
    languages_data = json.load(f)

# build mapping repo_name -> main language
main_lang = {}
pattern = re.compile(r"([A-Za-z0-9#\+\-_. ]+)\s*\(\s*([\d,]+)\s*bytes", re.IGNORECASE)
for rec in languages_data:
    repo = rec.get('repo_name')
    desc = rec.get('language_description', '')
    matches = pattern.findall(desc)
    if matches:
        # matches is list of (lang, bytes_str)
        lang_bytes = []
        for lang, bstr in matches:
            # clean
            lang_clean = lang.strip()
            bytes_int = int(bstr.replace(',', ''))
            lang_bytes.append((lang_clean, bytes_int))
        # pick max by bytes
        lang_bytes.sort(key=lambda x: x[1], reverse=True)
        main_lang[repo] = lang_bytes[0][0]
    else:
        # fallback: try simpler pattern like 'mainly written in Ruby (1,897 bytes)'
        m = re.search(r"written in ([A-Za-z0-9#\+\-_. ]+)", desc, re.IGNORECASE)
        if m:
            main_lang[repo] = m.group(1).strip()
        else:
            # leave absent
            pass

# Now process commits data
commits = var_call_OJK9SLtjBYyckyKeqLcD983O
results = []
for rec in commits:
    repo = rec.get('repo_name')
    cnt = rec.get('commit_count')
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(str(cnt).replace(',', ''))
        except:
            continue
    lang = main_lang.get(repo)
    if lang is None:
        # if language unknown, skip (conservative)
        continue
    # consider not Python (case-insensitive)
    if str(lang).strip().lower() != 'python':
        results.append({'repo_name': repo, 'commit_count': cnt_int, 'main_language': lang})

# sort by commit_count desc and take top 5
results.sort(key=lambda x: x['commit_count'], reverse=True)
top5 = [r['repo_name'] for r in results[:5]]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_hyjN2iLMg8GCH6ElsHUiiz1h': ['languages', 'repos', 'licenses'], 'var_call_VoFx5iRJanlmyZl5ytYqhwEQ': ['commits', 'contents', 'files'], 'var_call_OJK9SLtjBYyckyKeqLcD983O': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_2OLOOa3qdF3nbLVNj7j94Atk': 'file_storage/call_2OLOOa3qdF3nbLVNj7j94Atk.json'}

exec(code, env_args)
