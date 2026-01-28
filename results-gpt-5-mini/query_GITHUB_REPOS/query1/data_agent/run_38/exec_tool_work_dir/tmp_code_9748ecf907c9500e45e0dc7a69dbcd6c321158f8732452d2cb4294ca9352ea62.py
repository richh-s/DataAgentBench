code = """import json
from pathlib import Path

# Load variables from storage file paths
# var_call_a3z8KpRfKzAlnER35OLEQ9K2 and var_call_upmwMQ9CWnRB2NZNgNRUj13l are provided by the tool storage

p1 = Path(var_call_a3z8KpRfKzAlnER35OLEQ9K2)
with p1.open('r', encoding='utf-8') as f:
    non_python_records = json.load(f)

p2 = Path(var_call_upmwMQ9CWnRB2NZNgNRUj13l)
with p2.open('r', encoding='utf-8') as f:
    readme_records = json.load(f)

# Build set of non-python repo names
non_python_set = set(r['repo_name'] for r in non_python_records)

# Filter README records to those belonging to non-python repos
filtered = [r for r in readme_records if r.get('sample_repo_name') in non_python_set]

# For each repo, check if any of its README contents contains copyright info
import re

def has_copyright(text):
    if not isinstance(text, str):
        return False
    low = text.lower()
    if 'copyright' in low:
        return True
    if '©' in text:
        return True
    if 'all rights reserved' in low:
        return True
    # also check common copyright patterns like (c) or c) 1999
    if re.search(r"\(c\)", low):
        return True
    if re.search(r"\bc\)\s*\d{4}", low):
        return True
    return False

# Map repo -> list of readme contents
from collections import defaultdict
repo_readmes = defaultdict(list)
for r in filtered:
    repo = r.get('sample_repo_name')
    content = r.get('content')
    repo_readmes[repo].append(content)

repos_with_readme = set(repo_readmes.keys())
repos_with_copyright = set()
for repo, contents in repo_readmes.items():
    for c in contents:
        if c and copyright := (copyright if False else None):
            pass
    # simpler loop
    found = any((has_copyright(c) for c in contents if c))
    if found:
        repos_with_copyright.add(repo)

num_repos_with_readme = len(repos_with_readme)
num_repos_with_copyright = len(repos_with_copyright)
proportion = None
if num_repos_with_readme > 0:
    proportion = num_repos_with_copyright / num_repos_with_readme
else:
    proportion = 0.0

result = {
    'non_python_repos_with_readme': num_repos_with_readme,
    'non_python_repos_with_copyright': num_repos_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_a3z8KpRfKzAlnER35OLEQ9K2': 'file_storage/call_a3z8KpRfKzAlnER35OLEQ9K2.json', 'var_call_upmwMQ9CWnRB2NZNgNRUj13l': 'file_storage/call_upmwMQ9CWnRB2NZNgNRUj13l.json'}

exec(code, env_args)
