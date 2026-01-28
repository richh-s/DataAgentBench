code = """import json
import re

# Get the data from storage
languages_data = var_functions.query_db:10
readme_data = var_functions.query_db:16

# Count Python vs non-Python repos
python_repo_names = set()
non_python_repo_names = set()

for item in languages_data:
    repo_name = item.get('repo_name', '')
    lang_desc = item.get('language_description', '').lower()
    
    if 'python' in lang_desc:
        if repo_name:
            python_repo_names.add(repo_name)
    else:
        if repo_name:
            non_python_repo_names.add(repo_name)

python_repos = len(python_repo_names)
non_python_repos = len(non_python_repo_names)

# Now analyze README files for copyright
non_python_readmes = []
copyright_count = 0

copyright_patterns = [
    r'copyright\s+[©\(c\)]',
    r'©\s*\d{4}',
    r'\(c\)\s*\d{4}',
    r'copyright\s+\d{4}',
    r'all rights reserved'
]

for readme in readme_data:
    repo_name = readme.get('sample_repo_name', '')
    content = readme.get('content', '') or ''
    
    if repo_name in non_python_repo_names:
        non_python_readmes.append(repo_name)
        content_lower = content.lower()
        has_copyright = any(re.search(pattern, content_lower) for pattern in copyright_patterns)
        if has_copyright:
            copyright_count += 1

# Calculate proportion
total_non_python_readmes = len(non_python_readmes)
proportion = copyright_count / total_non_python_readmes if total_non_python_readmes > 0 else 0

result = {
    'total_repos': len(languages_data),
    'python_repos': python_repos,
    'non_python_repos': non_python_repos,
    'non_python_readmes_found': total_non_python_readmes,
    'non_python_readmes_with_copyright': copyright_count,
    'proportion': proportion
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}]}

exec(code, env_args)
