code = """import json

# Load non-python repos
with open(locals()['var_function-call-501958023560472879'], 'r') as f:
    non_python_repos_list = json.load(f)

# Create a set for faster lookup
non_python_repos = set()
for item in non_python_repos_list:
    non_python_repos.add(item['repo_name'])

# Load READMEs
with open(locals()['var_function-call-11153495764214467863'], 'r') as f:
    readmes = json.load(f)

total_readmes_in_non_python = 0
copyright_readmes_in_non_python = 0

for entry in readmes:
    repo_name = entry.get('sample_repo_name')
    content = entry.get('content')
    
    if repo_name in non_python_repos:
        total_readmes_in_non_python += 1
        if content and 'copyright' in content.lower():
            copyright_readmes_in_non_python += 1

if total_readmes_in_non_python == 0:
    result = 0.0
else:
    result = copyright_readmes_in_non_python / total_readmes_in_non_python

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7605414092250511720': ['languages', 'repos', 'licenses'], 'var_function-call-4416803740327317322': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-6089557288090344957': ['commits', 'contents', 'files'], 'var_function-call-501958023560472879': 'file_storage/function-call-501958023560472879.json', 'var_function-call-5644032705799933883': [{'count_star()': '128'}], 'var_function-call-11153495764214467863': 'file_storage/function-call-11153495764214467863.json'}

exec(code, env_args)
