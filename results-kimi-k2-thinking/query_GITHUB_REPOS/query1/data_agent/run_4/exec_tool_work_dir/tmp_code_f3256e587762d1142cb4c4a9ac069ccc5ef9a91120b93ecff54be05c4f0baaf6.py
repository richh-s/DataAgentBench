code = """# Read both datasets
readme_content = locals()['var_functions.query_db:26']
languages_data = locals()['var_functions.query_db:14']
import json
import os

# Load README data
if isinstance(readme_content, str):
    file_path = readme_content
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            readme_data = json.load(f)
    else:
        path = '/tmp/data_analyst_agent/' + file_path
        with open(path, 'r') as f:
            readme_data = json.load(f)
else:
    readme_data = readme_content

# Load languages data
if isinstance(languages_data, str):
    file_path = languages_data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            languages_data = json.load(f)
    else:
        path = '/tmp/data_analyst_agent/' + file_path
        with open(path, 'r') as f:
            languages_data = json.load(f)

# Get non-Python repository names
non_python_repos = set()
for lang in languages_data:
    if 'python' not in lang['language_description'].lower():
        non_python_repos.add(lang['repo_name'])

# Count READMEs with copyright information among non-Python repos
repos_with_copyright = []
total_non_python_with_readme = 0

for readme in readme_data:
    repo = readme['sample_repo_name']
    if repo in non_python_repos:
        total_non_python_with_readme += 1
        content = readme['content'] or ''
        if 'copyright' in content.lower():
            repos_with_copyright.append(repo)

# Calculate proportion
proportion = len(repos_with_copyright) / total_non_python_with_readme if total_non_python_with_readme > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total_non_python_with_readme": total_non_python_with_readme,
    "repos_with_copyright": len(repos_with_copyright),
    "proportion": proportion,
    "proportion_percentage": f"{proportion * 100:.2f}%"
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.execute_python:2': 'Sample data loaded', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 38, 'var_functions.list_db:12': ['languages', 'repos', 'licenses'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'type': "<class 'str'>", 'is_string': True, 'value_short': 'file_storage/functions.query_db:14.json', 'file_exists': False}, 'var_functions.execute_python:20': {'status': 'success', 'total_repos': 3325634, 'sample': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}]}, 'var_functions.execute_python:22': 2774729, 'var_functions.list_db:24': ['commits', 'contents', 'files'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_non_python': 2774729, 'total_readme_repos': 191, 'non_python_with_readme': 128}}

exec(code, env_args)
