code = """# Copyright detection in README files
import json, re, os

file1 = '/tmp/tmpqntf1a1p.json'
with open(file1, 'r') as f:
    non_python_data = json.load(f)
non_python_repos = {repo['repo_name'] for repo in non_python_data}

file2 = '/tmp/tmp4y6j7o3k.json'
with open(file2, 'r') as f:
    readme_data = json.load(f)

filtered_readmes = []
for readme in readme_data:
    if readme['sample_repo_name'] in non_python_repos:
        path = readme['sample_path']
        if path == 'README.md' or path.count('/') <= 1:
            filtered_readmes.append(readme)

patterns = [
    r'\bcopyright\b', r'©', r'\(c\)\s+\d{4}', 
    r'copyrights\b', r'all rights reserved\b', r'rights reserved\b'
]

def has_copyright(content):
    if not content:
        return False
    cl = content.lower()
    for p in patterns:
        if re.search(p, cl):
            return True
    return False

total = 0
copyright = 0
for readme in filtered_readmes:
    total += 1
    if has_copyright(readme.get('content', '')):
        copyright += 1

prop = copyright / total if total > 0 else 0
pct = prop * 100

result = {
    'total_repos': len(non_python_repos),
    'readme_analyzed': total,
    'readme_with_copyright': copyright,
    'readme_without_copyright': total - copyright,
    'proportion': prop,
    'percentage': pct
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'count': 0, 'first_five': []}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
