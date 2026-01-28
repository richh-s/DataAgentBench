code = """import json
import pandas as pd
import re

# Load tool results from storage variables
# var_call_xWR0YjOjNCjsuZa2bhSrTLtn and var_call_IVakraamcYmoXrMFLTITnV6D

def load_var(v):
    if isinstance(v, str):
        # it's a file path to JSON
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

data_nonpy = load_var(var_call_xWR0YjOjNCjsuZa2bhSrTLtn)
data_contents = load_var(var_call_IVakraamcYmoXrMFLTITnV6D)

# DataFrames
df_nonpy = pd.DataFrame(data_nonpy)
if df_nonpy.empty:
    nonpy_set = set()
else:
    nonpy_set = set(df_nonpy['repo_name'].astype(str).tolist())

df_contents = pd.DataFrame(data_contents)
# Ensure columns exist
if 'sample_repo_name' not in df_contents.columns:
    df_contents['sample_repo_name'] = ''
if 'sample_path' not in df_contents.columns:
    df_contents['sample_path'] = ''
if 'content' not in df_contents.columns:
    df_contents['content'] = ''

# Filter to README.md files (case-insensitive basename == 'readme.md')

def is_readme_md(path):
    if not isinstance(path, str):
        return False
    basename = path.split('/')[-1].lower()
    return basename == 'readme.md'

mask_readme = df_contents['sample_path'].apply(is_readme_md)
df_readmes = df_contents[mask_readme].copy()

# Filter to repos that do not use Python
mask_nonpy = df_readmes['sample_repo_name'].isin(nonpy_set)
df_readmes_nonpy = df_readmes[mask_nonpy].copy()

# Total README.md files for non-python repos
total_readmes = len(df_readmes_nonpy)

# Function to detect copyright info
pattern = re.compile(r"copyright|©|all rights reserved", re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

# Apply
if total_readmes > 0:
    df_readmes_nonpy['has_copyright'] = df_readmes_nonpy['content'].apply(has_copyright)
    readmes_with_copyright = int(df_readmes_nonpy['has_copyright'].sum())
    proportion = readmes_with_copyright / total_readmes
else:
    readmes_with_copyright = 0
    proportion = None

result = {
    'total_readmes': total_readmes,
    'readmes_with_copyright': readmes_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xWR0YjOjNCjsuZa2bhSrTLtn': 'file_storage/call_xWR0YjOjNCjsuZa2bhSrTLtn.json', 'var_call_IVakraamcYmoXrMFLTITnV6D': 'file_storage/call_IVakraamcYmoXrMFLTITnV6D.json'}

exec(code, env_args)
