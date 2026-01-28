code = """import json
import re
import pandas as pd

# Load previous tool results from storage file paths
with open(var_call_cd0AzoTK3xg0WTKlMmrTskNE, 'r', encoding='utf-8') as f:
    nonpy_list = json.load(f)
with open(var_call_unnv5UNz3QL1lyPzTTtXjJ68, 'r', encoding='utf-8') as f:
    contents = json.load(f)

# Create set of non-Python repo names
nonpy_repos = set([r['repo_name'] for r in nonpy_list if 'repo_name' in r])

# Build DataFrame for contents
df = pd.DataFrame(contents)
# Normalize column names
if 'sample_repo_name' not in df.columns:
    df.rename(columns={df.columns[0]: 'sample_repo_name', df.columns[1]: 'sample_path', df.columns[2]: 'content'}, inplace=True)

# Filter to README.md files (case-insensitive) and repos in nonpy list
mask_readme_md = df['sample_path'].fillna('').str.lower().str.endswith('readme.md')
mask_repo = df['sample_repo_name'].isin(nonpy_repos)
readme_df = df[mask_readme_md & mask_repo].copy()

# Function to detect copyright in content
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', flags=re.IGNORECASE)

def has_copyright(text):
    if text is None:
        return False
    if isinstance(text, str):
        if text.strip() == '' or text.strip().lower() == 'none':
            return False
        return bool(pattern.search(text))
    return False

# Group by repo and determine if any README.md in that repo contains copyright info
if readme_df.empty:
    total_repos_with_readme = 0
    repos_with_copyright = 0
else:
    grouped = readme_df.groupby('sample_repo_name')['content'].apply(list).reset_index()
    grouped['has_copyright'] = grouped['content'].apply(lambda lst: any(has_copyright(x) for x in lst))
    total_repos_with_readme = int(len(grouped))
    repos_with_copyright = int(grouped['has_copyright'].sum())

proportion = (repos_with_copyright / total_repos_with_readme) if total_repos_with_readme > 0 else None

result = {
    'total_nonpython_repos_with_readme_md': total_repos_with_readme,
    'nonpython_readme_with_copyright': repos_with_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cd0AzoTK3xg0WTKlMmrTskNE': 'file_storage/call_cd0AzoTK3xg0WTKlMmrTskNE.json', 'var_call_unnv5UNz3QL1lyPzTTtXjJ68': 'file_storage/call_unnv5UNz3QL1lyPzTTtXjJ68.json'}

exec(code, env_args)
