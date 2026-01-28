code = """import json
import re

# Load languages data from the provided file path variable
languages_file_path = var_call_cdPqWvZrxsWTFwWKUnAXaWpQ
with open(languages_file_path, 'r', encoding='utf-8') as f:
    languages_data = json.load(f)

# Load commits data
commits_data = var_call_bq3ARzjgsIqAq0Zo6c5RKS2v

# Build mapping of repo_name -> primary language
lang_pattern = re.compile(r"([A-Za-z0-9\+\#\.-]+(?: [A-Za-z0-9\+\#\.-]+)*) \(([\d,]+) bytes\)")
primary_language_map = {}
for rec in languages_data:
    repo = rec.get('repo_name')
    desc = rec.get('language_description', '')
    matches = lang_pattern.findall(desc)
    if not matches:
        continue
    # matches is list of tuples (language, bytes_str)
    best_lang = None
    best_bytes = -1
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        if bytes_val > best_bytes:
            best_bytes = bytes_val
            best_lang = lang
    if best_lang:
        primary_language_map[repo] = best_lang

# Process commits and order by commit_count desc
commit_records = []
for rec in commits_data:
    repo = rec.get('repo_name')
    try:
        count = int(rec.get('commit_count'))
    except:
        # try if it's already int
        try:
            count = int(rec.get('commit_count', 0))
        except:
            count = 0
    commit_records.append({'repo_name': repo, 'commit_count': count})

commit_records.sort(key=lambda x: x['commit_count'], reverse=True)

# Select top five whose primary language is not Python
result_repos = []
for rec in commit_records:
    if len(result_repos) >= 5:
        break
    repo = rec['repo_name']
    primary = primary_language_map.get(repo)
    if primary and primary.lower() == 'python':
        continue
    # If primary is unknown, conservatively include (since we can't confirm Python)
    result_repos.append(repo)

# Prepare JSON string
output = json.dumps(result_repos)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_9J1jwzVhOA3R3RhP0EV0u4Wf': ['languages', 'repos', 'licenses'], 'var_call_W858NWA60loBM8wNFa5q4pNc': ['commits', 'contents', 'files'], 'var_call_bq3ARzjgsIqAq0Zo6c5RKS2v': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}], 'var_call_cdPqWvZrxsWTFwWKUnAXaWpQ': 'file_storage/call_cdPqWvZrxsWTFwWKUnAXaWpQ.json'}

exec(code, env_args)
