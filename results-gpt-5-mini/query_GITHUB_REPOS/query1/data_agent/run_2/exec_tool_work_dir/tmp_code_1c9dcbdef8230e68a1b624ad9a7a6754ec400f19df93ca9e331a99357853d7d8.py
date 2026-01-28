code = """import json, re

# Load languages data from storage key
langs_path = var_call_OAcMzXQ4h0sAM0j6EdwHTCDR
with open(langs_path, 'r', encoding='utf-8') as f:
    langs = json.load(f)

# Load readmes data
readmes_path = var_call_cO61syuiV82JACtoHx9Avdix
with open(readmes_path, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# Build set of repos that do NOT mention Python in their language_description
non_python_repos = set()
for r in langs:
    repo = r.get('repo_name')
    desc = (r.get('language_description') or '')
    if isinstance(desc, str) and 'python' not in desc.lower():
        if repo:
            non_python_repos.add(repo)

# Aggregate README contents per repo for repos in non_python_repos
readme_by_repo = {}
for item in readmes:
    repo = item.get('sample_repo_name')
    if not repo:
        continue
    if repo in non_python_repos:
        content = item.get('content') or ''
        if not isinstance(content, str):
            try:
                content = str(content)
            except Exception:
                content = ''
        if repo in readme_by_repo and readme_by_repo[repo]:
            readme_by_repo[repo] += '\n' + content
        else:
            readme_by_repo[repo] = content

# Prepare pattern
pattern = re.compile(r'copyright|\(c\)|all rights reserved', re.IGNORECASE)

# Count matches
total = len(readme_by_repo)
matched = 0
matched_repos = []
for repo, content in readme_by_repo.items():
    if not content:
        continue
    if pattern.search(content) or ('\u00A9' in content) or (chr(169) in content):
        matched += 1
        matched_repos.append(repo)

proportion = None
if total > 0:
    proportion = matched / total

result = {
    'non_python_repos_with_readme_count': total,
    'readmes_with_copyright_count': matched,
    'proportion': proportion,
    'matched_repos_sample': matched_repos[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OAcMzXQ4h0sAM0j6EdwHTCDR': 'file_storage/call_OAcMzXQ4h0sAM0j6EdwHTCDR.json', 'var_call_cO61syuiV82JACtoHx9Avdix': 'file_storage/call_cO61syuiV82JACtoHx9Avdix.json', 'var_call_I56cZOK0Usoxr6EiEjdKPgBb': {'langs_count': 3325634, 'readmes_count': 149}}

exec(code, env_args)
