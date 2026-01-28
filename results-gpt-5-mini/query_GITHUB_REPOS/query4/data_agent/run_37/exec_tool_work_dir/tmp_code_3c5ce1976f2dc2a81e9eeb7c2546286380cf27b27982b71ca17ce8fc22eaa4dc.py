code = """import json, re, pandas as pd

# Load languages data from the stored JSON file path
with open(var_call_0tdBMIAk0osdqoyVn7UVcQ8H, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Commits data is available directly as a variable
commits = var_call_sutN8KVvW5lre2FeXXJYOr2S

# Build a mapping from repo_name to language_description
lang_map = {row['repo_name']: row['language_description'] for row in languages}

# Function to parse main language from language_description
def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    # Find patterns like 'Ruby (22,438 bytes)'
    matches = re.findall(r"([A-Za-z0-9+\#_.\- ]+?) \(([0-9,]+) bytes\)", desc)
    if matches:
        # Clean and pick max by bytes
        parsed = [(m[0].strip(), int(m[1].replace(',', ''))) for m in matches]
        parsed.sort(key=lambda x: x[1], reverse=True)
        return parsed[0][0]
    # Fallback patterns like 'mainly written in Ruby' or 'The majority of the code is in Ruby'
    m = re.search(r"written in ([A-Za-z0-9+#_.\- ]+)", desc)
    if m:
        return m.group(1).strip()
    m = re.search(r"majority of the code is in ([A-Za-z0-9+#_.\- ]+)", desc)
    if m:
        return m.group(1).strip()
    m = re.search(r"The codebase includes: ([A-Za-z0-9+#_.\- ]+)", desc)
    if m:
        return m.group(1).strip()
    return None

results = []
for c in commits:
    repo = c['repo_name']
    try:
        commit_count = int(str(c['commit_count']).replace(',', ''))
    except:
        # if not parseable, skip
        continue
    desc = lang_map.get(repo)
    main_lang = parse_main_language(desc) if desc is not None else None
    results.append({'repo_name': repo, 'commit_count': commit_count, 'main_language': main_lang})

# Filter out repositories whose main language is Python (case-insensitive contains 'python')
filtered = [r for r in results if not (r['main_language'] and 'python' in r['main_language'].lower())]

# Sort by commit_count desc and take top five
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)[:5]

top_repo_names = [r['repo_name'] for r in filtered_sorted]

import json
print("__RESULT__:")
print(json.dumps(top_repo_names))"""

env_args = {'var_call_lvIiEhhB2Kki3Jhc3U2mqiL8': ['languages', 'repos', 'licenses'], 'var_call_2PdZ4zAg6YE3ZKH0htwcfupQ': ['commits', 'contents', 'files'], 'var_call_0tdBMIAk0osdqoyVn7UVcQ8H': 'file_storage/call_0tdBMIAk0osdqoyVn7UVcQ8H.json', 'var_call_sutN8KVvW5lre2FeXXJYOr2S': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}]}

exec(code, env_args)
