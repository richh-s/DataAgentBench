code = """import json, re, os

# Load variables from storage (they may be file paths or lists)
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_python = load_var(var_call_LsEy7I1BejX0vnhaXNNt4Ks2)
contents = load_var(var_call_B3jYDjcUBLY451QMU8DkKo30)

non_python_set = set()
for r in non_python:
    # each r expected to be dict with repo_name
    repo = r.get('repo_name') if isinstance(r, dict) else None
    if repo:
        non_python_set.add(repo)

# Filter contents for README.md files in non-Python repos
readme_records = []
for rec in contents:
    path = (rec.get('sample_path') or '')
    repo = rec.get('sample_repo_name')
    if not path or not repo:
        continue
    if repo not in non_python_set:
        continue
    if path.lower().endswith('readme.md'):
        readme_records.append(rec)

# Consider only records with textual content
considered = []
for r in readme_records:
    c = r.get('content')
    if isinstance(c, str):
        s = c.strip()
        if s and s.lower() != 'none':
            considered.append(r)

total_readmes = len(considered)

# Pattern to detect copyright info
pattern = re.compile(r"copyright|\u00A9|\(c\)|all rights reserved", re.IGNORECASE)

readmes_with_copyright = [r for r in considered if pattern.search(r.get('content',''))]
count_with_copyright = len(readmes_with_copyright)

# Also compute repo-level presence (unique repos)
repos_with_readme = set(r['sample_repo_name'] for r in considered)
repos_with_copyright = set(r['sample_repo_name'] for r in readmes_with_copyright)

result = {
    'total_non_python_repos_in_languages_table': len(non_python_set),
    'total_readme_md_files_from_non_python_repos_considered': total_readmes,
    'readme_md_files_with_copyright': count_with_copyright,
    'proportion_readme_files_with_copyright': (count_with_copyright / total_readmes) if total_readmes else None,
    'unique_non_python_repos_with_readme_count': len(repos_with_readme),
    'unique_non_python_repos_with_readme_and_copyright_count': len(repos_with_copyright),
    'proportion_repos_with_readme_having_copyright': (len(repos_with_copyright) / len(repos_with_readme)) if repos_with_readme else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LsEy7I1BejX0vnhaXNNt4Ks2': 'file_storage/call_LsEy7I1BejX0vnhaXNNt4Ks2.json', 'var_call_B3jYDjcUBLY451QMU8DkKo30': 'file_storage/call_B3jYDjcUBLY451QMU8DkKo30.json'}

exec(code, env_args)
