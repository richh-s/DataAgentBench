code = """import json
import pandas as pd
import re

# Load previous tool results from storage variables

def load_var(v):
    # If storage provided a filepath (string), load the JSON; otherwise return as-is
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

nonpy = load_var(var_call_crCamGmsZEo5mr37CbbkIoVc)
readmes = load_var(var_call_OTNojtO3mEe2thmU6IyUg6Fx)

# DataFrames
df_nonpy = pd.DataFrame(nonpy)
df_readmes = pd.DataFrame(readmes)

# Set of repositories that do not use Python
nonpy_repos = set(df_nonpy['repo_name'].dropna().unique())

# Filter README entries belonging to those repositories
# Consider files where sample_path contains 'readme' (case-insensitive) already ensured by query,
# but we trust the provided results.

df_filtered = df_readmes[df_readmes['sample_repo_name'].isin(nonpy_repos)].copy()

total = int(len(df_filtered))

# Define pattern to detect copyright information
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', re.I)

# Ensure content field exists
if 'content' not in df_filtered.columns:
    df_filtered['content'] = ''
else:
    df_filtered['content'] = df_filtered['content'].fillna('')

# Compute boolean flag
df_filtered['has_copyright'] = df_filtered['content'].apply(lambda s: bool(pattern.search(s)))

count_with = int(df_filtered['has_copyright'].sum())
proportion = (count_with / total) if total > 0 else None

result = {
    'count_with': count_with,
    'total': total,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_crCamGmsZEo5mr37CbbkIoVc': 'file_storage/call_crCamGmsZEo5mr37CbbkIoVc.json', 'var_call_OTNojtO3mEe2thmU6IyUg6Fx': 'file_storage/call_OTNojtO3mEe2thmU6IyUg6Fx.json'}

exec(code, env_args)
