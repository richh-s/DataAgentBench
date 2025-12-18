code = """import pandas as pd
import json
import re

# Load the full results from the files
with open(locals()['var_function-call-5291993335761117457'], 'r') as f:
    non_python_repos_list = json.load(f)

with open(locals()['var_function-call-11616350880604223891'], 'r') as f:
    readme_contents_data = json.load(f)

non_python_repo_names = {repo['repo_name'] for repo in non_python_repos_list}
readme_contents_df = pd.DataFrame(readme_contents_data)

# Filter README contents to include only non-Python repositories
non_python_readme_df = readme_contents_df[readme_contents_df['sample_repo_name'].isin(non_python_repo_names)]

# Function to check for copyright information
def contains_copyright(text):
    if text is None:
        return False
    # Case-insensitive search for 'copyright' or '©'
    return bool(re.search(r'copyright|©', text, re.IGNORECASE))

# Apply the function to the content column
non_python_readme_df['has_copyright'] = non_python_readme_df['content'].apply(contains_copyright)

# Calculate the proportion
total_non_python_readmes = len(non_python_readme_df)
readmes_with_copyright = non_python_readme_df['has_copyright'].sum()

if total_non_python_readmes > 0:
    proportion = readmes_with_copyright / total_non_python_readmes
else:
    proportion = 0

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-3076225314897708197': 'file_storage/function-call-3076225314897708197.json', 'var_function-call-16408120266186584692': 'file_storage/function-call-16408120266186584692.json', 'var_function-call-5291993335761117457': 'file_storage/function-call-5291993335761117457.json', 'var_function-call-11616350880604223891': 'file_storage/function-call-11616350880604223891.json'}

exec(code, env_args)
