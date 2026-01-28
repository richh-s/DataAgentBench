code = """import json
import pandas as pd
import os

# Load data from previous query results stored in files or variables
# Variables available: var_call_LM3tvya7aOMgQs8YKYzKm8YV, var_call_9JPe2QYsMLtUbCP1E5AsAkEn

def load_var(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

records_not_python = load_var(var_call_LM3tvya7aOMgQs8YKYzKm8YV)
records_readmes = load_var(var_call_9JPe2QYsMLtUbCP1E5AsAkEn)

# Build set of non-python repo names
non_python_repos = set(r['repo_name'] for r in records_not_python)

# Filter README.md files among contents
readme_files = [r for r in records_readmes if r.get('sample_path') and r['sample_path'].lower().endswith('readme.md')]

# Further filter to those in non-python repos
readme_non_python = [r for r in readme_files if r.get('sample_repo_name') in non_python_repos]

# Define function to check if content is textual and contains copyright info
import re

def is_textual(content):
    if content is None:
        return False
    if isinstance(content, str):
        s = content.strip()
        if s == '' or s.lower() == 'none':
            return False
        # if looks like binary placeholder
        if len(s) < 10000 and re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', s):
            return False
        return True
    return False

copyright_patterns = [r'copyright', r'\u00a9', r'\(c\)', r'©']
pattern = re.compile('|'.join(copyright_patterns), flags=re.IGNORECASE)

count_text_readmes = 0
count_with_copyright = 0

for r in readme_non_python:
    content = r.get('content')
    if is_textual(content):
        count_text_readmes += 1
        if pattern.search(content):
            count_with_copyright += 1

# Prepare results
result = {
    'total_readme_md_files_in_non_python_repos': count_text_readmes,
    'readme_md_files_with_copyright': count_with_copyright,
}

# Compute proportion; handle division by zero
if count_text_readmes == 0:
    proportion = None
else:
    proportion = count_with_copyright / count_text_readmes
    # also percentage
    percent = proportion * 100
    result['proportion'] = proportion
    result['percentage'] = percent

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LM3tvya7aOMgQs8YKYzKm8YV': 'file_storage/call_LM3tvya7aOMgQs8YKYzKm8YV.json', 'var_call_9JPe2QYsMLtUbCP1E5AsAkEn': 'file_storage/call_9JPe2QYsMLtUbCP1E5AsAkEn.json'}

exec(code, env_args)
