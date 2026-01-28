code = """import json, re
# load commits data from var_call_Gv88F3PZTlPwD0cZesIq6BIu
commits = var_call_Gv88F3PZTlPwD0cZesIq6BIu
# load languages data from the JSON file path stored in var_call_QnMeCSOQx3KcCjOfatg5HVZb
with open(var_call_QnMeCSOQx3KcCjOfatg5HVZb, 'r') as f:
    languages = json.load(f)
# build map
lang_map = {item['repo_name']: item.get('language_description', '') for item in languages}

def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return ''
    # try to find all language (bytes) patterns
    matches = re.findall(r"([A-Za-z0-9\+\#\.\- ]+?)\s*\(\s*([\d,]+)\s*bytes", desc)
    if matches:
        best = None
        best_bytes = -1
        for lang, num in matches:
            try:
                val = int(num.replace(',', ''))
            except:
                val = 0
            if val > best_bytes:
                best_bytes = val
                best = lang.strip()
        return best
    # fallback patterns
    patterns = [r"mainly written in ([A-Za-z0-9\+\#\.\- ]+)",
                r"majority of the code is in ([A-Za-z0-9\+\#\.\- ]+)",
                r"The codebase includes: ([A-Za-z0-9\+\#\.\- ]+)",
                r"This repository is mainly written in ([A-Za-z0-9\+\#\.\- ]+)"]
    for p in patterns:
        m = re.search(p, desc, re.I)
        if m:
            return m.group(1).strip()
    return ''

# process commits list
rows = []
for r in commits:
    repo = r.get('repo_name')
    try:
        count = int(r.get('commit_count'))
    except:
        # try converting if string with commas
        try:
            count = int(str(r.get('commit_count')).replace(',', ''))
        except:
            count = 0
    desc = lang_map.get(repo, '')
    main_lang = parse_main_language(desc)
    rows.append({'repo_name': repo, 'commit_count': count, 'main_language': main_lang})

# filter out those whose main language is Python
filtered = [r for r in rows if not r['main_language'] or 'python' not in r['main_language'].lower()]
# sort by commit_count desc
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)
# take top 5
top5 = filtered_sorted[:5]
result = [r['repo_name'] for r in top5]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dxkaBEYMukmqo85kCIQRNeoE': ['languages', 'repos', 'licenses'], 'var_call_Xm349qLoNQeP3JJEKCOHJili': ['commits', 'contents', 'files'], 'var_call_QnMeCSOQx3KcCjOfatg5HVZb': 'file_storage/call_QnMeCSOQx3KcCjOfatg5HVZb.json', 'var_call_Kf1B01dDDUbPdCNMzrg5ScPI': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_Gv88F3PZTlPwD0cZesIq6BIu': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
