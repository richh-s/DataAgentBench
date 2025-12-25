code = """import json
import pandas as pd

# Load non-python repos
with open(locals()['var_function-call-15221092178194980029'], 'r') as f:
    non_python_repos_data = json.load(f)
# Normalize repo names
non_python_repos = set(item['repo_name'].strip().lower() for item in non_python_repos_data)

# Load READMEs
with open(locals()['var_function-call-11663374526765219291'], 'r') as f:
    readmes_data = json.load(f)

# Filter READMEs
target_readmes = []
for item in readmes_data:
    rname = item['sample_repo_name'].strip().lower()
    if rname in non_python_repos:
        target_readmes.append(item['content'])

total_readmes = len(target_readmes)
copyright_count = 0

for content in target_readmes:
    if content and 'copyright' in content.lower():
        copyright_count += 1

proportion = 0
if total_readmes > 0:
    proportion = copyright_count / total_readmes

print("__RESULT__:")
print(json.dumps({
    "total_readmes": total_readmes,
    "copyright_count": copyright_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-8787238762938711609': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15221092178194980029': 'file_storage/function-call-15221092178194980029.json', 'var_function-call-4320722104742026337': 'file_storage/function-call-4320722104742026337.json', 'var_function-call-16789664860533402074': {'total_readmes': 131, 'copyright_count': 16, 'proportion': 0.12213740458015267}, 'var_function-call-4204752993235869674': [{'count(*)': '3325634'}], 'var_function-call-8184908415150830109': [{'count_star()': '24286'}], 'var_function-call-18445668282830058306': [{'count_star()': '195'}], 'var_function-call-6296645524194485244': [{'count_star()': '204'}], 'var_function-call-11663374526765219291': 'file_storage/function-call-11663374526765219291.json', 'var_function-call-16679090194567199143': {'total_readmes': 138, 'copyright_count': 17, 'proportion': 0.12318840579710146}, 'var_function-call-4086291351933775746': [{'count(*)': '0'}]}

exec(code, env_args)
