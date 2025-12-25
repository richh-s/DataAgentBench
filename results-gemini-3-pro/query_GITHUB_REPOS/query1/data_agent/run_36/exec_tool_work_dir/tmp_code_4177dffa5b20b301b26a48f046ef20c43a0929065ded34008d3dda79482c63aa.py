code = """import json
import pandas as pd

# Load non-python repos
# The result from query_db is a list of dicts: [{"repo_name": "..."}]
# stored in var_function-call-15221092178194980029
with open(locals()['var_function-call-15221092178194980029'], 'r') as f:
    non_python_repos_data = json.load(f)

# Create a set for faster lookup
non_python_repos = set(item['repo_name'] for item in non_python_repos_data)

# Load READMEs
# The result from query_db is a list of dicts: [{"sample_repo_name": "...", "content": "..."}]
# stored in var_function-call-4320722104742026337
with open(locals()['var_function-call-4320722104742026337'], 'r') as f:
    readmes_data = json.load(f)

# Filter READMEs
target_readmes = []
for item in readmes_data:
    if item['sample_repo_name'] in non_python_repos:
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

env_args = {'var_function-call-8787238762938711609': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15221092178194980029': 'file_storage/function-call-15221092178194980029.json', 'var_function-call-4320722104742026337': 'file_storage/function-call-4320722104742026337.json'}

exec(code, env_args)
