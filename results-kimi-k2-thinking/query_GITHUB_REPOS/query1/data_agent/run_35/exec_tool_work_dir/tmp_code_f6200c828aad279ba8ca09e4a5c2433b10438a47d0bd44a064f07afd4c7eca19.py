code = """import json
import os
import re

# Read language data
lang_file = locals()['var_functions.query_db:0']
with open(lang_file, 'r') as f:
    languages = json.load(f)

# Read README data
readme_file = locals()['var_functions.query_db:2']
with open(readme_file, 'r') as f:
    readmes = json.load(f)

print(f"Loaded {len(languages)} language records")
print(f"Loaded {len(readmes)} README records")

# Identify repos that do NOT use Python
non_python_repos = []
for lang_record in languages:
    repo_name = lang_record['repo_name']
    lang_desc = lang_record['language_description'].lower()
    # Check if Python is mentioned in the language description
    if 'python' not in lang_desc:
        non_python_repos.append(repo_name)

print(f"Found {len(non_python_repos)} non-Python repositories")

# Filter READMEs for non-Python repos
non_python_readmes = []
for readme in readmes:
    if readme['sample_repo_name'] in non_python_repos:
        non_python_readmes.append(readme)

print(f"Found {len(non_python_readmes)} READMEs from non-Python repos")

# Check for copyright information in README content
copyright_count = 0
total_count = len(non_python_readmes)

copyright_patterns = [
    r'copyright\s+\d{4}',
    r'copyright\s+©\s*\d{4}',
    r'©\s*\d{4}',
    r'copyright\s+holder',
    r'copyright\s+notice',
    r'intellectual\s+property'
]

for readme in non_python_readmes:
    content = readme.get('content', '').lower()
    has_copyright = False
    for pattern in copyright_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            has_copyright = True
            break
    if has_copyright:
        copyright_count += 1

print(f"READMEs with copyright: {copyright_count}/{total_count}")

# Calculate proportion
if total_count > 0:
    proportion = copyright_count / total_count
    percentage = proportion * 100
    result = {
        'non_python_repos': len(non_python_repos),
        'non_python_readmes': total_count,
        'copyright_count': copyright_count,
        'proportion': proportion,
        'percentage': round(percentage, 2)
    }
else:
    result = {
        'non_python_repos': len(non_python_repos),
        'non_python_readmes': 0,
        'copyright_count': 0,
        'proportion': 0,
        'percentage': 0
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
