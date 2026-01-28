code = """import json, re

# Load languages data
if isinstance(var_call_OAcMzXQ4h0sAM0j6EdwHTCDR, str):
    with open(var_call_OAcMzXQ4h0sAM0j6EdwHTCDR, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = var_call_OAcMzXQ4h0sAM0j6EdwHTCDR

# Load README contents data
if isinstance(var_call_cO61syuiV82JACtoHx9Avdix, str):
    with open(var_call_cO61syuiV82JACtoHx9Avdix, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = var_call_cO61syuiV82JACtoHx9Avdix

# Build set of repos that do NOT mention Python in their language_description
non_python_repos = set()
for r in langs:
    desc = (r.get('language_description') or '')
    if 'python' not in desc.lower():
        repo = r.get('repo_name')
        if repo:
            non_python_repos.add(repo)

# Aggregate README contents per repo
readme_by_repo = {}
for item in readmes:
    repo = item.get('sample_repo_name')
    if not repo:
        continue
    if repo in non_python_repos:
        content = item.get('content') or ''
        # normalize to string
        if not isinstance(content, str):
            try:
                content = str(content)
            except Exception:
                content = ''
        if repo in readme_by_repo and readme_by_repo[repo]:
            readme_by_repo[repo] += '\n' + content
        else:
            readme_by_repo[repo] = content

# Pattern to detect copyright-like phrases (avoid non-ascii literals)
pattern = re.compile(r'copyright|\(c\)|all rights reserved', re.IGNORECASE)

total = len(readme_by_repo)
matched = 0
matched_repos = []
for repo, content in readme_by_repo.items():
    if not content:
        continue
    if pattern.search(content) or (chr(169) in content):
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

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OAcMzXQ4h0sAM0j6EdwHTCDR': 'file_storage/call_OAcMzXQ4h0sAM0j6EdwHTCDR.json', 'var_call_cO61syuiV82JACtoHx9Avdix': 'file_storage/call_cO61syuiV82JACtoHx9Avdix.json'}

exec(code, env_args)
