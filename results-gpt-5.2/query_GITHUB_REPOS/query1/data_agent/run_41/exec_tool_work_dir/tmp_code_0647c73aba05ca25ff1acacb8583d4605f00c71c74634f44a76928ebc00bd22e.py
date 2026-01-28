code = """import json, pandas as pd

# Load non-python repos
non_python_path = var_call_Wg2GJzKBorJOSzfmg9s84N4f
with open(non_python_path, 'r', encoding='utf-8') as f:
    non_python = json.load(f)
non_python_set = set(r['repo_name'] for r in non_python)

# README contents query came back empty
readmes = var_call_IwwpWgG5V0tXyyfadjwuZM4U

# compute
num_repos = len(non_python_set)
num_with_readme = 0
num_with_copyright = 0

copyright_patterns = [
    'copyright',
    '(c)',
    نشان := None
]

# simple detection
for r in readmes:
    repo = r.get('repo_name')
    if repo not in non_python_set:
        continue
    content = (r.get('content') or '')
    num_with_readme += 1
    if 'copyright' in content.lower() or '(c)' in content.lower() or '©' in content:
        num_with_copyright += 1

result = {
    'non_python_repo_count': num_repos,
    'non_python_repos_with_readme_md_count': num_with_readme,
    'non_python_readme_md_with_copyright_count': num_with_copyright,
    'proportion_among_non_python_repos_with_readme_md': (num_with_copyright/num_with_readme) if num_with_readme else None,
    'note': 'README.md sample query returned 0 rows; proportion cannot be computed.'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Wg2GJzKBorJOSzfmg9s84N4f': 'file_storage/call_Wg2GJzKBorJOSzfmg9s84N4f.json', 'var_call_IwwpWgG5V0tXyyfadjwuZM4U': []}

exec(code, env_args)
