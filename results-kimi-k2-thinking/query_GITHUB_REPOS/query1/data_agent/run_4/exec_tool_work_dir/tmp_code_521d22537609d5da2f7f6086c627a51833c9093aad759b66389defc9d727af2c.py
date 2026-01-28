code = """# Let's verify our data first
import json
import os

# Load languages data
lang_path = locals()['var_functions.query_db:14']
if isinstance(lang_path, str):
    path = lang_path if os.path.exists(lang_path) else '/tmp/data_analyst_agent/' + lang_path
    with open(path, 'r') as f:
        languages_data = json.load(f)

# Count total Python vs non-Python
python_count = 0
non_python_count = 0

for item in languages_data:
    if 'python' in item['language_description'].lower():
        python_count += 1
    else:
        non_python_count += 1

print("__RESULT__:")
print(json.dumps({
    "total_repos": len(languages_data),
    "python_repos": python_count,
    "non_python_repos": non_python_count,
    "percentage_non_python": f"{(non_python_count / len(languages_data) * 100):.1f}%"
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.execute_python:2': 'Sample data loaded', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 38, 'var_functions.list_db:12': ['languages', 'repos', 'licenses'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'type': "<class 'str'>", 'is_string': True, 'value_short': 'file_storage/functions.query_db:14.json', 'file_exists': False}, 'var_functions.execute_python:20': {'status': 'success', 'total_repos': 3325634, 'sample': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}]}, 'var_functions.execute_python:22': 2774729, 'var_functions.list_db:24': ['commits', 'contents', 'files'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_non_python': 2774729, 'total_readme_repos': 191, 'non_python_with_readme': 128}, 'var_functions.execute_python:30': {'total_non_python_with_readme': 131, 'repos_with_copyright': 16, 'proportion': 0.12213740458015267, 'proportion_percentage': '12.21%'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'total_readme_files': '277'}], 'var_functions.execute_python:36': {'non_python_repos_total': 2774729, 'non_python_readme_files': 10, 'readmes_with_copyright': 1, 'proportion': 0.1, 'proportion_percentage': '10.00%'}}

exec(code, env_args)
