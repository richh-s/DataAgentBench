code = """import json
import re

# Load the README contents
readme_contents_path = locals()['var_functions.query_db:12']

with open(readme_contents_path, 'r') as f:
    readme_contents = json.load(f)

# Load non-Python repos
non_python_repos_path = locals()['var_functions.query_db:16']

with open(non_python_repos_path, 'r') as f:
    non_python_repos = json.load(f)

non_python_repo_names = set(repo['repo_name'] for repo in non_python_repos)

# Filter to only non-Python repos
non_python_readmes = [
    item for item in readme_contents 
    if item['sample_repo_name'] in non_python_repo_names
]

# Define copyright patterns (case-insensitive)
copyright_patterns = [
    r'copyright',  # copyright word
    r'©',  # copyright symbol
    r'\(c\)',  # (c)
    r'\[c\]',  # [c]
    r'all rights reserved',  # all rights reserved
    r'license:',  # license header
    r'licensed under'  # licensed under
]

# Check each README for copyright
readmes_with_copyright = 0
readmes_without_copyright = 0
results = []

for readme in non_python_readmes:
    content = readme['content'] or ''
    content_lower = content.lower()
    
    has_copyright = False
    for pattern in copyright_patterns:
        if re.search(pattern, content_lower, re.IGNORECASE):
            has_copyright = True
            break
    
    if has_copyright:
        readmes_with_copyright += 1
    else:
        readmes_without_copyright += 1
    
    results.append({
        'repo': readme['sample_repo_name'],
        'has_copyright': has_copyright,
        'content_preview': content[:200] if content else ''
    })

# Calculate proportion
total = len(non_python_readmes)
if total > 0:
    proportion = readmes_with_copyright / total
else:
    proportion = 0

print('__RESULT__:')
print(json.dumps({
    'total_readmes': total,
    'readmes_with_copyright': readmes_with_copyright,
    'readmes_without_copyright': readmes_without_copyright,
    'proportion': proportion,
    'sample_results': results[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 2774729, 'sample_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_readme': '195'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_non_python_repos': 2774729, 'total_readmes_in_non_python': 131}}

exec(code, env_args)
