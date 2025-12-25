code = """import json

# Load data
with open(locals()['var_function-call-17316050141868196047'], 'r') as f:
    repos_list = json.load(f)

with open(locals()['var_function-call-3366446698735946739'], 'r') as f:
    readme_files = json.load(f)

with open(locals()['var_function-call-8828968465635628992'], 'r') as f:
    contents_list = json.load(f)

non_python_repos = set(item['repo_name'] for item in repos_list)
readme_repo_names = set(item['repo_name'] for item in readme_files)
contents_ids = set(item['id'] for item in contents_list)
readme_ids = set(item['id'] for item in readme_files)

print("__RESULT__:")
print(json.dumps({
    "count_non_python_repos": len(non_python_repos),
    "count_readme_files_entries": len(readme_files),
    "count_unique_readme_repos": len(readme_repo_names),
    "count_contents": len(contents_list),
    "overlap_repos_non_python_and_readmes": len(non_python_repos.intersection(readme_repo_names)),
    "overlap_ids_readmes_and_contents": len(readme_ids.intersection(contents_ids))
}))"""

env_args = {'var_function-call-2607864808049419873': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-8444357205340828073': 'file_storage/function-call-8444357205340828073.json', 'var_function-call-10172226988217569572': [{'count_star()': '524077'}], 'var_function-call-10205520039209315791': [{'count_star()': '24286'}], 'var_function-call-17316050141868196047': 'file_storage/function-call-17316050141868196047.json', 'var_function-call-3366446698735946739': 'file_storage/function-call-3366446698735946739.json', 'var_function-call-8828968465635628992': 'file_storage/function-call-8828968465635628992.json', 'var_function-call-14718236509941954687': {'total_readmes_checked': 3, 'copyright_readmes': 1, 'proportion': 0.3333333333333333}}

exec(code, env_args)
