code = """import json, pandas as pd, re

# Load non-python repos
nonpy_path = var_call_rfwd47V8nzbBPpyFmfxrENZS
with open(nonpy_path, 'r', encoding='utf-8') as f:
    nonpy = json.load(f)
nonpy_repos = set(r['repo_name'] for r in nonpy)

# Load readmes
readme_path = var_call_UG4Z23ZVBrJypxJm9VFbz81z
with open(readme_path, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# Filter to non-python repos, and de-duplicate per repo (in case multiple refs)
repo_to_content = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo in nonpy_repos and repo not in repo_to_content:
        repo_to_content[repo] = r.get('content') or ''

# Define copyright detection
pat = re.compile(r'(?:\bcopyright\b|\bcopy\s*right\b|\(c\)|©)', re.IGNORECASE)

num_readmes = len(repo_to_content)
num_with_c = sum(1 for c in repo_to_content.values() if pat.search(c or ''))
prop = (num_with_c / num_readmes) if num_readmes else None

out = {
    'non_python_repos_with_readme_md': num_readmes,
    'readme_md_with_copyright': num_with_c,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rfwd47V8nzbBPpyFmfxrENZS': 'file_storage/call_rfwd47V8nzbBPpyFmfxrENZS.json', 'var_call_UG4Z23ZVBrJypxJm9VFbz81z': 'file_storage/call_UG4Z23ZVBrJypxJm9VFbz81z.json'}

exec(code, env_args)
