code = """# Load the data from files
import json
import os

# Load non-Python repositories
lang_path = locals()['var_functions.query_db:14']
if isinstance(lang_path, str):
    path = lang_path if os.path.exists(lang_path) else '/tmp/data_analyst_agent/' + lang_path
    with open(path, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = lang_path

# Get set of non-Python repositories
non_python_repos = set()
for item in languages_data:
    if 'python' not in item['language_description'].lower():
        non_python_repos.add(item['repo_name'])

# Load README files from contents
readme_path = locals()['var_functions.query_db:32']
if isinstance(readme_path, str):
    path = readme_path if os.path.exists(readme_path) else '/tmp/data_analyst_agent/' + readme_path
    with open(path, 'r') as f:
        readme_data = json.load(f)
else:
    readme_data = readme_path

# Filter README files to only those from non-Python repos
non_python_readmes = []
for item in readme_data:
    # Check if the path looks like a README.md file (not just any file with 'readme' in path)
    path_lower = item['sample_path'].lower()
    if 'readme' in path_lower and (path_lower.endswith('.md') or '/' not in path_lower.replace('readme', '')):
        if item['sample_repo_name'] in non_python_repos:
            non_python_readmes.append(item)

# Count those with copyright information
copyright_count = 0
total_count = len(non_python_readmes)

for readme in non_python_readmes:
    content = readme.get('content', '') or ''
    if 'copyright' in content.lower():
        copyright_count += 1

# Calculate proportion
proportion = copyright_count / total_count if total_count > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "non_python_repos_total": len(non_python_repos),
    "non_python_readme_files": total_count,
    "readmes_with_copyright": copyright_count,
    "proportion": proportion,
    "proportion_percentage": f"{proportion * 100:.2f}%"
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.execute_python:2': 'Sample data loaded', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 38, 'var_functions.list_db:12': ['languages', 'repos', 'licenses'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'type': "<class 'str'>", 'is_string': True, 'value_short': 'file_storage/functions.query_db:14.json', 'file_exists': False}, 'var_functions.execute_python:20': {'status': 'success', 'total_repos': 3325634, 'sample': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}]}, 'var_functions.execute_python:22': 2774729, 'var_functions.list_db:24': ['commits', 'contents', 'files'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_non_python': 2774729, 'total_readme_repos': 191, 'non_python_with_readme': 128}, 'var_functions.execute_python:30': {'total_non_python_with_readme': 131, 'repos_with_copyright': 16, 'proportion': 0.12213740458015267, 'proportion_percentage': '12.21%'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'total_readme_files': '277'}]}

exec(code, env_args)
