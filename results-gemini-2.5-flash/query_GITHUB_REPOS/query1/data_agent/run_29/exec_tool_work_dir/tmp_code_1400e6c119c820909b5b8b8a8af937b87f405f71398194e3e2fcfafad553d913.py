code = """import json
import pandas as pd

# Load non-Python repo names
with open(locals()['var_function-call-14000370119027926666'], 'r') as f:
    non_python_repo_names = json.load(f)

# Load all README contents
with open(locals()['var_function-call-14706481381448526615'], 'r') as f:
    all_readme_contents = json.load(f)

non_python_repos_set = set(non_python_repo_names)

# Filter READMEs for non-Python repositories
non_python_readmes = []
for entry in all_readme_contents:
    if entry['sample_repo_name'] in non_python_repos_set:
        non_python_readmes.append(entry)


# Count READMEs with copyright information
copyright_count = 0
for readme in non_python_readmes:
    if readme['content'] and "copyright" in readme['content'].lower():
        copyright_count += 1

total_non_python_readmes = len(non_python_readmes)

if total_non_python_readmes > 0:
    proportion = copyright_count / total_non_python_readmes
else:
    proportion = 0.0

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-13488805173218297358': 'file_storage/function-call-13488805173218297358.json', 'var_function-call-14000370119027926666': 'file_storage/function-call-14000370119027926666.json', 'var_function-call-15179744626608783060': "SELECT sample_repo_name, content FROM contents WHERE LOWER(sample_path) IN ('readme.md', 'readme') AND sample_repo_name IN ('f', 'i', 'l', 'e', '_', 's', 't', 'o', 'r', 'a', 'g', 'e', '/', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', '-', 'c', 'a', 'l', 'l', '-', '1', '4', '0', '0', '0', '3', '7', '0', '1', '1', '9', '0', '2', '7', '9', '2', '6', '6', '6', '6', '.', 'j', 's', 'o', 'n');", 'var_function-call-459493572836622866': 'file_storage/function-call-459493572836622866.json', 'var_function-call-9595831252955057211': 'file_storage/function-call-9595831252955057211.json', 'var_function-call-14706481381448526615': 'file_storage/function-call-14706481381448526615.json'}

exec(code, env_args)
