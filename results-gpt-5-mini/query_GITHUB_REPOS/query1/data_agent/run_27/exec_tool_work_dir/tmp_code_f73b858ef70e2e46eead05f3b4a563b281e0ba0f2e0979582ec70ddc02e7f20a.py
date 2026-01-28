code = """import json
from pathlib import Path

# Load data from storage-provided file paths
p1 = Path(var_call_zmEqjcompvqNCFdxeXMQ8LFn)
p2 = Path(var_call_s5o6RXbpSfUObNebTMNy9P56)

with p1.open('r', encoding='utf-8') as f:
    non_python_list = json.load(f)
with p2.open('r', encoding='utf-8') as f:
    readmes = json.load(f)

# Extract set of non-python repo names
non_python_repos = set(r['repo_name'] for r in non_python_list if r.get('repo_name'))

# Filter README.md files (case-insensitive) and belonging to non-python repos
readme_files = [r for r in readmes if r.get('sample_path') and r.get('sample_repo_name') and r['sample_repo_name'] in non_python_repos and r['sample_path'].lower().endswith('readme.md')]

# Helper to check copyright
import re
pattern = re.compile(r'copyright|\u00A9', re.IGNORECASE)

def has_copyright(content):
    if not content:
        return False
    # content may be the string 'None' to indicate missing
    if isinstance(content, str) and content.strip().lower() == 'none':
        return False
    return bool(pattern.search(content))


total_readme_files = len(readme_files)
files_with_copyright = sum(1 for r in readme_files if has_copyright(r.get('content')))

# Per-repo aggregation
repos_with_readme = {}
for r in readme_files:
    repo = r['sample_repo_name']
    repos_with_readme.setdefault(repo, []).append(r)

unique_repos_with_readme = len(repos_with_readme)
repos_with_any_copyright = 0
for repo, files in repos_with_readme.items():
    if any(has_copyright(f.get('content')) for f in files):
        repos_with_any_copyright += 1

# Prepare results
result = {
    'readme_files_non_python_total': total_readme_files,
    'readme_files_with_copyright': files_with_copyright,
    'proportion_readme_files': (files_with_copyright / total_readme_files) if total_readme_files else None,
    'unique_repos_with_readme_non_python': unique_repos_with_readme,
    'repos_with_any_readme_copyright': repos_with_any_copyright,
    'proportion_repos_with_copyright': (repos_with_any_copyright / unique_repos_with_readme) if unique_repos_with_readme else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zmEqjcompvqNCFdxeXMQ8LFn': 'file_storage/call_zmEqjcompvqNCFdxeXMQ8LFn.json', 'var_call_udXTBaI4DpjhdK1sxcGNi0j5': 'file_storage/call_udXTBaI4DpjhdK1sxcGNi0j5.json', 'var_call_s5o6RXbpSfUObNebTMNy9P56': 'file_storage/call_s5o6RXbpSfUObNebTMNy9P56.json'}

exec(code, env_args)
