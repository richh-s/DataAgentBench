code = """import json, re

# Load query results from storage-provided file paths
with open(var_call_gCz7LopCyDQnFGpCrpvfkNVI, 'r') as f:
    languages = json.load(f)
with open(var_call_STflJTcNxawAMDA40KUmbCcd, 'r') as f:
    contents = json.load(f)

# Build mapping of repo -> language_description
lang_map = { rec['repo_name']: rec.get('language_description','') for rec in languages }

# Identify repositories that do NOT use Python (case-insensitive search)
non_python_repos = set()
for repo, desc in lang_map.items():
    if 'python' not in (desc or '').lower():
        non_python_repos.add(repo)

# Filter README-like files from contents (query already limited, but enforce)
readmes = []
for rec in contents:
    path = (rec.get('sample_path') or '').lower()
    if path.endswith('readme.md') or path == 'readme' or path.endswith('/readme'):
        readmes.append(rec)

# Among those, select files belonging to non-Python repos
readmes_non_python = [r for r in readmes if r.get('sample_repo_name') in non_python_repos]

# Function to detect copyright indications
def has_copyright(text):
    if not text:
        return False
    txt = text
    if '©' in txt:
        return True
    if re.search(r'copyright', txt, re.I):
        return True
    if re.search(r'\(c\)', txt, re.I):
        return True
    if re.search(r'&copy;', txt, re.I):
        return True
    # also check for 'all rights reserved' as a fallback
    if re.search(r'all rights reserved', txt, re.I):
        return True
    return False

total = len(readmes_non_python)
with_copyright = 0
for r in readmes_non_python:
    content = r.get('content') or ''
    if has_copyright(content):
        with_copyright += 1

proportion = (with_copyright / total) if total > 0 else None
percentage = (proportion * 100) if proportion is not None else None

result = {
    'total_readme_files_non_python': total,
    'readme_files_with_copyright': with_copyright,
    'proportion': proportion,
    'percentage': percentage
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gCz7LopCyDQnFGpCrpvfkNVI': 'file_storage/call_gCz7LopCyDQnFGpCrpvfkNVI.json', 'var_call_STflJTcNxawAMDA40KUmbCcd': 'file_storage/call_STflJTcNxawAMDA40KUmbCcd.json'}

exec(code, env_args)
