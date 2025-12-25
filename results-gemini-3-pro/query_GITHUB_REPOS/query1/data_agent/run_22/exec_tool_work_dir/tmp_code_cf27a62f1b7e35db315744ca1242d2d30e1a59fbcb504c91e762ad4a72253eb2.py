code = """import json

# Load non-python repos
with open(locals()['var_function-call-2179150976695303860'], 'r') as f:
    non_python_repos_list = json.load(f)

# Convert to set for O(1) lookup
non_python_repos = set()
for r in non_python_repos_list:
    non_python_repos.add(r['repo_name'])

# Load readme info
with open(locals()['var_function-call-13431561003676937567'], 'r') as f:
    readme_info = json.load(f)

total_readmes_in_non_python = 0
copyright_in_readmes_non_python = 0

for record in readme_info:
    repo = record['sample_repo_name']
    has_copyright = int(record['has_copyright']) # Convert to int just in case
    
    if repo in non_python_repos:
        total_readmes_in_non_python += 1
        if has_copyright == 1:
            copyright_in_readmes_non_python += 1

if total_readmes_in_non_python == 0:
    result = 0.0
else:
    result = copyright_in_readmes_non_python / total_readmes_in_non_python

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14345973181823531792': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-2706953258355405955': 'file_storage/function-call-2706953258355405955.json', 'var_function-call-2179150976695303860': 'file_storage/function-call-2179150976695303860.json', 'var_function-call-13431561003676937567': 'file_storage/function-call-13431561003676937567.json'}

exec(code, env_args)
