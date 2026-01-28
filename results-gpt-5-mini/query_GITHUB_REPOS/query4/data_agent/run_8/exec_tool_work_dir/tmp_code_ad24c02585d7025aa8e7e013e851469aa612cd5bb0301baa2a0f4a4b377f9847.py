code = """import json
import re
from collections import Counter

# Load the languages data
path_lang = var_call_SOqt504ASuySNIhvmaYFZbP7
if isinstance(path_lang, str):
    with open(path_lang, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = path_lang

# Load the commits data
path_commits = var_call_uFxuNfHvKa9AVBNmCsxAcqaB
if isinstance(path_commits, str):
    with open(path_commits, 'r', encoding='utf-8') as f:
        commits = json.load(f)
else:
    commits = path_commits

# Parse primary language for each repo
lang_primary = {}
pattern = re.compile(r'([A-Za-z0-9\+\#\._\- ]+) \(([\d,]+) bytes\)')
for rec in langs:
    repo = rec.get('repo_name')
    desc = rec.get('language_description','')
    matches = pattern.findall(desc)
    # matches: list of (language, bytes)
    if matches:
        # convert bytes and pick max
        parsed = []
        for m in matches:
            lang = m[0].strip()
            num = int(m[1].replace(',',''))
            parsed.append((lang,num))
        # choose language with max bytes
        primary = max(parsed, key=lambda x: x[1])[0]
        lang_primary[repo] = primary

# Count commits per repo
counter = Counter()
for rec in commits:
    rn = rec.get('repo_name')
    if rn:
        counter[rn] += 1

# Filter repos that have a known primary language and primary language not Python
filtered = []
for repo, cnt in counter.items():
    primary = lang_primary.get(repo)
    if primary and 'python' not in primary.lower():
        filtered.append((repo, cnt))

# Sort by commit count descending and take top 5
top5 = sorted(filtered, key=lambda x: x[1], reverse=True)[:5]
result = [r for r,c in top5]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SOqt504ASuySNIhvmaYFZbP7': 'file_storage/call_SOqt504ASuySNIhvmaYFZbP7.json', 'var_call_uFxuNfHvKa9AVBNmCsxAcqaB': 'file_storage/call_uFxuNfHvKa9AVBNmCsxAcqaB.json'}

exec(code, env_args)
