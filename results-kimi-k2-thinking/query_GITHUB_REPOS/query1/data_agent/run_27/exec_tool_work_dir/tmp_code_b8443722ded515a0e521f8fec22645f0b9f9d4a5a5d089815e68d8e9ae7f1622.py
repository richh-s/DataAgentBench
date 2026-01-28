code = """import json
import re

# Read the languages data from the file
languages_file_key = 'var_functions.query_db:24'
readme_file_key = 'var_functions.query_db:22'

# Check if these are file paths or direct data
if isinstance(locals()[languages_file_key], str):
    with open(locals()[languages_file_key], 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = locals()[languages_file_key]

if isinstance(locals()[readme_file_key], str):
    with open(locals()[readme_file_key], 'r') as f:
        readme_data = json.load(f)
else:
    readme_data = locals()[readme_file_key]

# Step 1: Identify repositories that do not use Python
non_python_repos = []
python_repos = []

for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    if 'Python' in lang_desc or 'python' in lang_desc:
        python_repos.append(repo_name)
    else:
        non_python_repos.append(repo_name)

# Step 2: Filter README files for non-Python repos
non_python_readmes = []
for readme in readme_data:
    repo = readme['sample_repo_name']
    if repo in non_python_repos:
        non_python_readmes.append({
            'repo_name': repo,
            'content': readme['content'],
            'path': readme['sample_path']
        })

# Step 3: Check for copyright information
def has_copyright(content):
    if not content:
        return False
    # Check for various copyright patterns
    patterns = [
        r'copyright',
        r'Copyright',
        r'COPYRIGHT',
        r'\\(c\\)',
        r'©',
        r'All rights reserved'
    ]
    for pattern in patterns:
        if re.search(pattern, content):
            return True
    return False

repos_with_copyright = []
repos_without_copyright = []

for readme in non_python_readmes:
    if has_copyright(readme['content']):
        repos_with_copyright.append(readme['repo_name'])
    else:
        repos_without_copyright.append(readme['repo_name'])

# Step 4: Calculate proportion
total_non_python_repos_with_readme = len(non_python_readmes)
total_repos_with_copyright = len(repos_with_copyright)

if total_non_python_repos_with_readme > 0:
    proportion = total_repos_with_copyright / total_non_python_repos_with_readme
else:
    proportion = 0

# For verification, let's see some stats
result = {
    'total_repos_in_database': len(languages_data),
    'python_repos': len(python_repos),
    'non_python_repos': len(non_python_repos),
    'non_python_repos_with_readme': total_non_python_repos_with_readme,
    'non_python_repos_with_copyright': total_repos_with_copyright,
    'proportion': proportion,
    'sample_python_repos': python_repos[:10],
    'sample_non_python_repos': non_python_repos[:10],
    'sample_repos_with_copyright': repos_with_copyright[:10],
    'sample_repos_without_copyright': repos_without_copyright[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
