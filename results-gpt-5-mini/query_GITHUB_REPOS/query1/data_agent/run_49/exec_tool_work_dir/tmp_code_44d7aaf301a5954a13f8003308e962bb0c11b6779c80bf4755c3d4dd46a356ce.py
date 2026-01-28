code = """import json
import re
# Load results from previous query_db calls
path_nonpy = var_call_kFyZiUm3gZcpoLsbXZmXcdmm
path_readmes = var_call_IuOajdZtjTeNvaR1OjxBarfT
with open(path_nonpy, 'r', encoding='utf-8') as f:
    nonpy = json.load(f)
with open(path_readmes, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# Extract sets and map
nonpy_repos = set(r['repo_name'] for r in nonpy)
# Filter readmes to only those repos
filtered = [r for r in readmes if r.get('sample_repo_name') in nonpy_repos]

# For each, check presence of copyright info
pattern = re.compile(r'copyright|\u00A9|\(c\)', re.IGNORECASE)

results = []
for r in filtered:
    content = r.get('content') or ''
    has_copyright = bool(pattern.search(content))
    results.append({
        'repo': r.get('sample_repo_name'),
        'has_readme': True,
        'has_copyright_in_readme': bool(has_copyright)
    })

# Some repos may have multiple README.md entries; deduplicate by repo preferring True for copyright
from collections import defaultdict
agg = defaultdict(lambda: {'has_readme': False, 'has_copyright_in_readme': False})
for item in results:
    repo = item['repo']
    agg[repo]['has_readme'] = True
    if item['has_copyright_in_readme']:
        agg[repo]['has_copyright_in_readme'] = True

# Compute counts
denominator = sum(1 for v in agg.values() if v['has_readme'])
numerator = sum(1 for v in agg.values() if v['has_readme'] and v['has_copyright_in_readme'])
proportion = (numerator / denominator) if denominator > 0 else None

output = {
    'numerator': numerator,
    'denominator': denominator,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_kFyZiUm3gZcpoLsbXZmXcdmm': 'file_storage/call_kFyZiUm3gZcpoLsbXZmXcdmm.json', 'var_call_IuOajdZtjTeNvaR1OjxBarfT': 'file_storage/call_IuOajdZtjTeNvaR1OjxBarfT.json'}

exec(code, env_args)
