code = """import json, pandas as pd

# Load full results if they are file paths
from pathlib import Path

def load_result(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x))
    return x

contents = load_result(var_call_pvAQvdImn5NvwnKRwSfK7aBn)
languages = load_result(var_call_0wOSAyeupFEKCOPAkE8Q9d0K)

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Determine repos that do NOT use Python (no 'Python (' substring, case-insensitive) in language_description
mask_no_python = ~languages_df['language_description'].str.contains('python', case=False, na=False)
no_py_repos = languages_df[mask_no_python][['repo_name']].drop_duplicates()

# Filter README.md files and join with repos
readme_df = contents_df[contents_df['sample_path'].str.lower() == 'readme.md'][['sample_repo_name','content']]

merged = readme_df.merge(no_py_repos, left_on='sample_repo_name', right_on='repo_name')

# Among these README files, detect copyright info
copyright_mask = merged['content'].str.contains('copyright', case=False, na=False)

num_total = int(len(merged))
num_with = int(copyright_mask.sum())
prop = float(num_with / num_total) if num_total > 0 else None

result = {
    'num_repos_without_python_with_readme': num_total,
    'num_readmes_with_copyright': num_with,
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_pvAQvdImn5NvwnKRwSfK7aBn': 'file_storage/call_pvAQvdImn5NvwnKRwSfK7aBn.json', 'var_call_0wOSAyeupFEKCOPAkE8Q9d0K': 'file_storage/call_0wOSAyeupFEKCOPAkE8Q9d0K.json'}

exec(code, env_args)
