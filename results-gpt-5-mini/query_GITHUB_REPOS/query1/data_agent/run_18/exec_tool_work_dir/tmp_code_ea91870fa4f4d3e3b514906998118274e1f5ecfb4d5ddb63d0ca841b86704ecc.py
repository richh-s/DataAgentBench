code = """import json, os, re

# Load storage variables from file path if needed
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8', errors='replace') as f:
            return json.load(f)
    return v

records_not_python = load_var(var_call_LM3tvya7aOMgQs8YKYzKm8YV)
records_readmes = load_var(var_call_9JPe2QYsMLtUbCP1E5AsAkEn)

# Build set of non-python repo names
non_python_repos = set()
if isinstance(records_not_python, list):
    for r in records_not_python:
        if isinstance(r, dict) and 'repo_name' in r:
            non_python_repos.add(r['repo_name'])

# Filter README.md files among contents
readme_files = []
if isinstance(records_readmes, list):
    for r in records_readmes:
        if not isinstance(r, dict):
            continue
        path = r.get('sample_path')
        if path and path.lower().endswith('readme.md'):
            readme_files.append(r)

# Further filter to those in non-python repos
readme_non_python = [r for r in readme_files if r.get('sample_repo_name') in non_python_repos]

# Define textual check and copyright detection
def is_textual(content):
    if content is None:
        return False
    if not isinstance(content, str):
        return False
    s = content.strip()
    if s == '' or s.lower() == 'none':
        return False
    if '\x00' in s:
        return False
    return True

copyright_patterns = [r'copyright', r'\u00a9', r'\(c\)', r'©']
pat = re.compile('|'.join(copyright_patterns), flags=re.IGNORECASE)

count_text = 0
count_copyright = 0
for r in readme_non_python:
    content = r.get('content')
    if is_textual(content):
        count_text += 1
        if pat.search(content):
            count_copyright += 1

result = {
    'total_readme_md_files_in_non_python_repos': count_text,
    'readme_md_files_with_copyright': count_copyright,
}
if count_text > 0:
    result['proportion'] = count_copyright / count_text
    result['percentage'] = (count_copyright / count_text) * 100
else:
    result['proportion'] = None
    result['percentage'] = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LM3tvya7aOMgQs8YKYzKm8YV': 'file_storage/call_LM3tvya7aOMgQs8YKYzKm8YV.json', 'var_call_9JPe2QYsMLtUbCP1E5AsAkEn': 'file_storage/call_9JPe2QYsMLtUbCP1E5AsAkEn.json', 'var_call_ujleLBsycHOXQnXq3165Ttf1': {'test': 1}}

exec(code, env_args)
