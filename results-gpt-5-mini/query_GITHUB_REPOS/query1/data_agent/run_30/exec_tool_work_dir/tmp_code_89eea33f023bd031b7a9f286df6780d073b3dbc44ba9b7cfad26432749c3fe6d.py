code = """import json
import pandas as pd
import os

# Load the query results from the stored json files
with open(var_call_CbGBqUOMOHOYadJyHrHrcjHc, 'r') as f:
    langs = json.load(f)
with open(var_call_8uXua690a94TDn4MPnQ2MxKW, 'r') as f:
    contents = json.load(f)

# Create DataFrames
df_langs = pd.DataFrame(langs)
df_contents = pd.DataFrame(contents)

# Normalize column names
# Select README.md files (case-insensitive) by basename
import ntpath

def basename(path):
    try:
        return ntpath.basename(path or '')
    except Exception:
        return ''

df_contents['basename'] = df_contents['sample_path'].apply(basename)

# Filter for README.md (case-insensitive)
mask_readme_md = df_contents['basename'].str.lower() == 'readme.md'
df_readmes = df_contents[mask_readme_md].copy()

# Merge with languages on repo name
df_merged = df_readmes.merge(df_langs, how='left', left_on='sample_repo_name', right_on='repo_name')

# Keep only rows where we have a language_description and it does NOT contain 'python'
mask_lang_present = df_merged['language_description'].notnull()
mask_no_python = ~df_merged['language_description'].str.lower().str.contains('python')

df_no_python = df_merged[mask_lang_present & mask_no_python].copy()

# Function to detect copyright markers
import re
pattern = re.compile(r'copyright|\u00A9|\(c\)', re.IGNORECASE)

def has_copyright(content):
    if content is None:
        return False
    try:
        s = str(content)
    except Exception:
        return False
    if s.strip() == '' or s.strip().lower() == 'none':
        return False
    return bool(pattern.search(s))

# Apply detection
if df_no_python.empty:
    total = 0
    with_copy = 0
else:
    df_no_python['has_copy'] = df_no_python['content'].apply(has_copyright)
    total = int(len(df_no_python))
    with_copy = int(df_no_python['has_copy'].sum())

proportion = None
if total > 0:
    proportion = with_copy / total

result = {
    'total_readme_files_no_python': total,
    'readme_with_copyright': with_copy,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CbGBqUOMOHOYadJyHrHrcjHc': 'file_storage/call_CbGBqUOMOHOYadJyHrHrcjHc.json', 'var_call_8uXua690a94TDn4MPnQ2MxKW': 'file_storage/call_8uXua690a94TDn4MPnQ2MxKW.json'}

exec(code, env_args)
