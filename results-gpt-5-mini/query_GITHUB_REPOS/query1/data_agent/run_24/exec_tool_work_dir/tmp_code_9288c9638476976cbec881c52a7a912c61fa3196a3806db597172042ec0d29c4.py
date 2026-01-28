code = """import json
import re
import pandas as pd

# Load the results from previous tool calls (they are stored as file paths for large results)
with open(var_call_AhfyurCY13EdUppkfcGO736C, 'r', encoding='utf-8') as f:
    nonpy = json.load(f)
with open(var_call_UCv5gQtvvYZYyq7jQUGN0gUt, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# Create DataFrames
df_nonpy = pd.DataFrame(nonpy)
df_readmes = pd.DataFrame(readmes)

# Normalize column names
if 'repo_name' in df_nonpy.columns:
    nonpy_repos = set(df_nonpy['repo_name'].dropna().astype(str).str.strip())
else:
    nonpy_repos = set()

# Filter readmes to those belonging to non-Python repos
# sample_repo_name column in readmes
if 'sample_repo_name' in df_readmes.columns and 'content' in df_readmes.columns:
    df_readmes['sample_repo_name'] = df_readmes['sample_repo_name'].astype(str).str.strip()
    df_readmes['content'] = df_readmes['content'].astype(str)
    df_nonpy_readmes = df_readmes[df_readmes['sample_repo_name'].isin(nonpy_repos)].copy()
else:
    df_nonpy_readmes = pd.DataFrame(columns=df_readmes.columns)

# Consider only README files (already queried with readme.md but ensure)
if 'sample_path' in df_nonpy_readmes.columns:
    df_nonpy_readmes = df_nonpy_readmes[df_nonpy_readmes['sample_path'].str.lower().str.contains('readme')]

# Detection pattern for copyright info
pattern = re.compile(r"copyright|\u00A9|©|all rights reserved", flags=re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

# Apply detection
if not df_nonpy_readmes.empty:
    df_nonpy_readmes['has_copyright'] = df_nonpy_readmes['content'].apply(has_copyright)
    total_readmes = int(len(df_nonpy_readmes))
    copyright_count = int(df_nonpy_readmes['has_copyright'].sum())
    proportion = copyright_count / total_readmes if total_readmes > 0 else None
else:
    total_readmes = 0
    copyright_count = 0
    proportion = None

result = {
    'non_python_readme_count': total_readmes,
    'readmes_with_copyright': copyright_count,
    'proportion': proportion,
    'percentage': (proportion * 100) if proportion is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AhfyurCY13EdUppkfcGO736C': 'file_storage/call_AhfyurCY13EdUppkfcGO736C.json', 'var_call_UCv5gQtvvYZYyq7jQUGN0gUt': 'file_storage/call_UCv5gQtvvYZYyq7jQUGN0gUt.json'}

exec(code, env_args)
