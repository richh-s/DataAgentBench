code = """import json

# Load data from previous tool calls (may be file paths or lists)
try:
    data_non_py = var_call_woJXaZF8Zno5kfYTGtJHZyCb
except NameError:
    data_non_py = None
try:
    data_readmes = var_call_dKzaVAenpnXWJFE0a2eg50Cm
except NameError:
    data_readmes = None

# Helper to load if variable is a filepath
def load_maybe_filepath(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

records_non_py = load_maybe_filepath(data_non_py)
records_readmes = load_maybe_filepath(data_readmes)

# Build set of non-python repo names
non_py_repos = set(r['repo_name'] for r in records_non_py)

# Filter readme records for repos in non_py_repos
readme_records = [r for r in records_readmes if r.get('sample_repo_name') in non_py_repos]

# Function to detect copyright-like phrases
import re
pattern = re.compile(r"copyright|©|all rights reserved", re.IGNORECASE)

file_count = len(readme_records)
file_with_copyright = 0

# Track per-repo
repos_with_readme = {}

for r in readme_records:
    repo = r.get('sample_repo_name')
    content = r.get('content') or ''
    has = bool(pattern.search(content))
    if repo not in repos_with_readme:
        repos_with_readme[repo] = {'total_files': 0, 'has_copyright': False}
    repos_with_readme[repo]['total_files'] += 1
    if has:
        file_with_copyright += 1
        repos_with_readme[repo]['has_copyright'] = True

repos_with_readme_count = len(repos_with_readme)
repos_with_copyright = sum(1 for v in repos_with_readme.values() if v['has_copyright'])

# Prepare results
result = {
    'total_non_python_repos_in_metadata': len(non_py_repos),
    'total_readme_files_for_non_python_repos': file_count,
    'readme_files_with_copyright': file_with_copyright,
    'proportion_readme_files_with_copyright': None,
    'repos_with_at_least_one_readme': repos_with_readme_count,
    'repos_with_readme_having_copyright': repos_with_copyright,
    'proportion_repos_with_readme_having_copyright': None
}

if file_count > 0:
    result['proportion_readme_files_with_copyright'] = file_with_copyright / file_count
if repos_with_readme_count > 0:
    result['proportion_repos_with_readme_having_copyright'] = repos_with_copyright / repos_with_readme_count

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_woJXaZF8Zno5kfYTGtJHZyCb': 'file_storage/call_woJXaZF8Zno5kfYTGtJHZyCb.json', 'var_call_dKzaVAenpnXWJFE0a2eg50Cm': 'file_storage/call_dKzaVAenpnXWJFE0a2eg50Cm.json'}

exec(code, env_args)
