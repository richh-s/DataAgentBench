code = """import json, re
from collections import defaultdict

# Load variables stored by previous tool calls. They may be file paths (strings) or Python objects.
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_var(var_call_03Y88WMpH37tDYAhsDGUk7yk)
contents = load_var(var_call_fF3bIDUqn9wh3d4t1XTfVssa)

# Identify repositories that do NOT mention Python in their language_description
non_python_repos = set()
for r in langs:
    desc = (r.get('language_description') or '').lower()
    if 'python' not in desc:
        non_python_repos.add(r.get('repo_name'))

# Filter README files from contents that belong to non-Python repositories
# The contents query already targeted README paths, but double-check sample_path
readmes = [c for c in contents if c.get('sample_repo_name') in non_python_repos]

# Define pattern for copyright indicators
pattern = re.compile(r'copyright|©|\(c\)', re.I)

# File-level counts
total_files = len(readmes)
files_with_copyright = 0
for c in readmes:
    cont = c.get('content') or ''
    if pattern.search(cont):
        files_with_copyright += 1

# Repo-level counts: count repos (among non-Python repos) that have at least one README in dataset,
# and how many of those repos have a README that matches the pattern
repo_to_files = defaultdict(list)
for c in readmes:
    repo_to_files[c.get('sample_repo_name')].append(c)

total_repos_with_readme = len(repo_to_files)
repos_with_copyright = 0
for repo, fls in repo_to_files.items():
    if any(pattern.search((f.get('content') or '')) for f in fls):
        repos_with_copyright += 1

# Compute fractions (as floats, None if denominator is zero)
file_fraction = None
repo_fraction = None
if total_files > 0:
    file_fraction = files_with_copyright / total_files
if total_repos_with_readme > 0:
    repo_fraction = repos_with_copyright / total_repos_with_readme

# Prepare result
result = {
    'non_python_readme_files_count': total_files,
    'readme_files_with_copyright_count': files_with_copyright,
    'readme_files_with_copyright_fraction': round(file_fraction, 4) if file_fraction is not None else None,
    'non_python_repos_with_readme_count': total_repos_with_readme,
    'repos_with_readme_with_copyright_count': repos_with_copyright,
    'repo_fraction_with_copyright_in_readme': round(repo_fraction, 4) if repo_fraction is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_03Y88WMpH37tDYAhsDGUk7yk': 'file_storage/call_03Y88WMpH37tDYAhsDGUk7yk.json', 'var_call_fF3bIDUqn9wh3d4t1XTfVssa': 'file_storage/call_fF3bIDUqn9wh3d4t1XTfVssa.json'}

exec(code, env_args)
