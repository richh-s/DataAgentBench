code = """import json

# Load non-python repos list
with open(locals()['var_function-call-17316050141868196047'], 'r') as f:
    repos_list = json.load(f)

# Load contents list (READMEs from contents table)
with open(locals()['var_function-call-6106559980529225804'], 'r') as f:
    readme_contents = json.load(f)

non_python_repos = set(item['repo_name'] for item in repos_list)

total_readmes = 0
copyright_readmes = 0

for item in readme_contents:
    repo = item['sample_repo_name']
    has_copyright_val = item['has_copyright']
    
    # Check if repo is non-python
    # If repo is not in non_python_repos, it means it either uses Python OR it's not in the metadata db at all.
    # If it's not in metadata db, we can't determine if it uses Python.
    # However, usually we assume the metadata db covers the relevant universe.
    # If a repo is in artifacts but not metadata, we should probably exclude it or assume it's unknown.
    # Given the prompt "Among repositories that do not use Python...", we strictly look for repos KNOWN to not use Python.
    if repo in non_python_repos:
        total_readmes += 1
        # Check copyright
        # DuckDB bools in JSON might be true/false (bool) or "true"/"false" (str)
        if str(has_copyright_val).lower() == 'true':
            copyright_readmes += 1

proportion = 0.0
if total_readmes > 0:
    proportion = copyright_readmes / total_readmes

print("__RESULT__:")
print(json.dumps({
    "total_readmes": total_readmes,
    "copyright_readmes": copyright_readmes,
    "proportion": proportion
}))"""

env_args = {'var_function-call-2607864808049419873': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-8444357205340828073': 'file_storage/function-call-8444357205340828073.json', 'var_function-call-10172226988217569572': [{'count_star()': '524077'}], 'var_function-call-10205520039209315791': [{'count_star()': '24286'}], 'var_function-call-17316050141868196047': 'file_storage/function-call-17316050141868196047.json', 'var_function-call-3366446698735946739': 'file_storage/function-call-3366446698735946739.json', 'var_function-call-8828968465635628992': 'file_storage/function-call-8828968465635628992.json', 'var_function-call-14718236509941954687': {'total_readmes_checked': 3, 'copyright_readmes': 1, 'proportion': 0.3333333333333333}, 'var_function-call-15731274694683841460': {'count_non_python_repos': 2774729, 'count_readme_files_entries': 3086, 'count_unique_readme_repos': 2279, 'count_contents': 24286, 'overlap_repos_non_python_and_readmes': 1644, 'overlap_ids_readmes_and_contents': 4}, 'var_function-call-11405700522118054398': [{'count_star()': '204'}], 'var_function-call-6106559980529225804': 'file_storage/function-call-6106559980529225804.json'}

exec(code, env_args)
