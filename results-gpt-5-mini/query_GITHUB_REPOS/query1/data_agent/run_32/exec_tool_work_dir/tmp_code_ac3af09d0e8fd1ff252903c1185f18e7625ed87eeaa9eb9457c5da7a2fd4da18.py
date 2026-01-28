code = """import json
import re
import pandas as pd

# Load query results from previous tool calls (file paths provided in variables)
with open(var_call_3LzZ1k2lNS9iejQgdwsasghj, 'r') as f:
    langs = json.load(f)
with open(var_call_j2tCW4lY3skchB0NjGat7kZA, 'r') as f:
    contents = json.load(f)

# Create DataFrames
df_langs = pd.DataFrame(langs)
df_contents = pd.DataFrame(contents)

# Normalize and detect Python usage in language_description
if 'language_description' in df_langs.columns:
    df_langs['is_python'] = df_langs['language_description'].str.contains('python', case=False, na=False)
else:
    df_langs['is_python'] = False

# Merge contents with languages on repository name
merged = df_contents.merge(df_langs[['repo_name', 'is_python']], left_on='sample_repo_name', right_on='repo_name', how='inner')

# Filter to README files from repos that do NOT use Python
merged_non_py = merged[~merged['is_python']].copy()

# Total README files in non-Python repos
total = int(len(merged_non_py))

# Detect copyright information using common markers
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', flags=re.I)
merged_non_py['has_copyright'] = merged_non_py['content'].fillna('').apply(lambda x: bool(pattern.search(x)))
count_with_copyright = int(merged_non_py['has_copyright'].sum())

proportion = None
if total > 0:
    proportion = count_with_copyright / total

result = {
    'total_readmes': total,
    'readmes_with_copyright': count_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dgWH2mC9yWpVzYjAcnICSSfR': ['languages', 'repos', 'licenses'], 'var_call_lrM9wLO7pkXlpql7UANepPFN': ['commits', 'contents', 'files'], 'var_call_3LzZ1k2lNS9iejQgdwsasghj': 'file_storage/call_3LzZ1k2lNS9iejQgdwsasghj.json', 'var_call_j2tCW4lY3skchB0NjGat7kZA': 'file_storage/call_j2tCW4lY3skchB0NjGat7kZA.json'}

exec(code, env_args)
