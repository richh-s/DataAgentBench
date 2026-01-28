code = """import json
import pandas as pd
import re

# Load variables from storage (they may be file paths or actual lists)
def load_storage(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

data_nonpy = load_storage(var_call_BGZRABRoDe7TaP3xpk3ni4af)
data_contents = load_storage(var_call_VkIWc3YX8JF3uZMgNyTRSbYq)

df_nonpy = pd.DataFrame(data_nonpy)
df_contents = pd.DataFrame(data_contents)

# Build set of non-python repo names
nonpy_repos = set(df_nonpy['repo_name'].unique())

# Filter contents to README.md files belonging to non-python repos
filtered = df_contents[df_contents['sample_repo_name'].isin(nonpy_repos)].copy()

# Ensure content is string
filtered['content'] = filtered['content'].fillna('').astype(str)

# Regex to detect copyright-like phrases
pattern = re.compile(r"copyright|©|\(c\)|all rights reserved|copyrighted", re.I)

filtered['has_copyright'] = filtered['content'].apply(lambda x: bool(pattern.search(x)))

total_readmes = int(filtered.shape[0])
readmes_with_copyright = int(filtered['has_copyright'].sum())

proportion = None
if total_readmes > 0:
    proportion = readmes_with_copyright / total_readmes

result = {
    'total_readme_files_in_non_python_repos': total_readmes,
    'readme_files_with_copyright': readmes_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BGZRABRoDe7TaP3xpk3ni4af': 'file_storage/call_BGZRABRoDe7TaP3xpk3ni4af.json', 'var_call_VkIWc3YX8JF3uZMgNyTRSbYq': 'file_storage/call_VkIWc3YX8JF3uZMgNyTRSbYq.json'}

exec(code, env_args)
