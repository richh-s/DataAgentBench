code = """import json
import re

# Path to the languages JSON file is in var_call_TjqKuvZN2LsBjy2FbJDTtq5Y
path = var_call_TjqKuvZN2LsBjy2FbJDTtq5Y

# Commits data available as var_call_8vMSvpbaqJRNkYfi3y05xHUi
commits = var_call_8vMSvpbaqJRNkYfi3y05xHUi

# Create a mapping of repo_name -> commit_count (int)
commit_map = {rec['repo_name']: int(rec['commit_count']) for rec in commits}

# We'll search the languages file text for only the repo_names we care about
target_repos = set(commit_map.keys())

# Read file text
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# For each target repo, extract the language_description value using regex
lang_desc_map = {}
for repo in target_repos:
    # Build a regex that finds the object for this repo and captures language_description
    # This assumes JSON with "repo_name": "repo" and "language_description": "..."
    pattern = re.compile(r'"repo_name"\s*:\s*"' + re.escape(repo) + r'"\s*,\s*"language_description"\s*:\s*"(.*?)"', re.DOTALL)
    m = pattern.search(text)
    if m:
        # Unescape potential escaped quotes within the JSON string
        raw = m.group(1)
        # Replace escaped quotes and escaped newlines
        raw = raw.encode('utf-8').decode('unicode_escape')
        lang_desc_map[repo] = raw
    else:
        lang_desc_map[repo] = None

# Function to extract primary language from description
pattern_lang = re.compile(r"([A-Za-z0-9\+\#\. ]+?)\s*\(\s*([0-9,]+)\s*bytes\)", re.IGNORECASE)

def primary_language(desc):
    if not desc:
        return None
    matches = pattern_lang.findall(desc)
    if not matches:
        return None
    best = None
    max_bytes = -1
    for lang, b in matches:
        try:
            num = int(b.replace(',', ''))
        except:
            num = 0
        if num > max_bytes:
            max_bytes = num
            best = lang.strip()
    return best

# Build list of records with repo, commit_count, primary_language
records = []
for repo, cnt in commit_map.items():
    desc = lang_desc_map.get(repo)
    pl = primary_language(desc)
    records.append({'repo_name': repo, 'commit_count': cnt, 'primary_language': pl})

# Filter where primary_language is not Python (case-insensitive) and not None
filtered = [r for r in records if r['primary_language'] and r['primary_language'].lower() != 'python']

# Sort by commit_count desc
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)

# Take top 5 repo_names
top5 = [r['repo_name'] for r in filtered_sorted[:5]]

import json as _json
print("__RESULT__:")
print(_json.dumps(top5))"""

env_args = {'var_call_TjqKuvZN2LsBjy2FbJDTtq5Y': 'file_storage/call_TjqKuvZN2LsBjy2FbJDTtq5Y.json', 'var_call_8vMSvpbaqJRNkYfi3y05xHUi': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
