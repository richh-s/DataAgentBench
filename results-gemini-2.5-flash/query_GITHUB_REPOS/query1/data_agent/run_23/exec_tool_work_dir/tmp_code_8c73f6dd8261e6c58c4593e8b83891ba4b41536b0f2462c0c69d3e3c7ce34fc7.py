code = """import json
import pandas as pd

# Load non-Python repositories
with open(locals()['var_function-call-8588576884841636071'], 'r') as f:
    non_python_repos_data = json.load(f)
non_python_repos = {repo['repo_name'] for repo in non_python_repos_data}

# Load README.md contents
with open(locals()['var_function-call-7341639197380326101'], 'r') as f:
    readme_contents_data = json.load(f)

# Filter README.md files to only include those from non-Python repositories
filtered_readmes = [
    item for item in readme_contents_data 
    if item['sample_repo_name'] in non_python_repos
]

# Count README.md files that contain copyright information
copyright_count = 0
for readme in filtered_readmes:
    if 'content' in readme and isinstance(readme['content'], str):
        if 'copyright' in readme['content'].lower():
            copyright_count += 1

# Calculate the proportion
total_filtered_readmes = len(filtered_readmes)
proportion = copyright_count / total_filtered_readmes if total_filtered_readmes > 0 else 0

print("__RESULT__:")
print(json.dumps({'proportion_with_copyright': proportion}))"""

env_args = {'var_function-call-8588576884841636071': 'file_storage/function-call-8588576884841636071.json', 'var_function-call-5747517209964925963': {'repo_names_count': 2774729, 'first_10_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_function-call-7341639197380326101': 'file_storage/function-call-7341639197380326101.json'}

exec(code, env_args)
