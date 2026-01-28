code = """import json, re

with open(var_call_OAcMzXQ4h0sAM0j6EdwHTCDR, 'r', encoding='utf-8') as f:
    langs = json.load(f)
with open(var_call_cO61syuiV82JACtoHx9Avdix, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

non_python = set()
for r in langs:
    repo = r.get('repo_name')
    desc = r.get('language_description') or ''
    if isinstance(desc, str) and 'python' not in desc.lower():
        if repo:
            non_python.add(repo)

readme_by_repo = {}
for item in readmes:
    repo = item.get('sample_repo_name')
    if not repo or repo not in non_python:
        continue
    content = item.get('content') or ''
    if repo in readme_by_repo:
        readme_by_repo[repo] += '\n' + content
    else:
        readme_by_repo[repo] = content

pat = re.compile(r'copyright|\(c\)|all rights reserved', re.IGNORECASE)

total = len(readme_by_repo)
matched = 0
matched_list = []
for repo, content in readme_by_repo.items():
    if not content:
        continue
    if pat.search(content) or (chr(169) in content):
        matched += 1
        matched_list.append(repo)

prop = None
if total > 0:
    prop = matched / total

res = {
    'non_python_repos_with_readme_count': total,
    'readmes_with_copyright_count': matched,
    'proportion': prop,
    'matched_repos_sample': matched_list[:20]
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_OAcMzXQ4h0sAM0j6EdwHTCDR': 'file_storage/call_OAcMzXQ4h0sAM0j6EdwHTCDR.json', 'var_call_cO61syuiV82JACtoHx9Avdix': 'file_storage/call_cO61syuiV82JACtoHx9Avdix.json', 'var_call_I56cZOK0Usoxr6EiEjdKPgBb': {'langs_count': 3325634, 'readmes_count': 149}}

exec(code, env_args)
