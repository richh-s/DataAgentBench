code = """import json
import pandas as pd
import re

# Load results from storage variables
data_pkg_latest = var_call_LexZ7D9ewAeYv1w6hl4D1ztH
data_proj_pkg = var_call_VjHaCoRgGUMmcX1y4bYGiHth
data_proj_info = var_call_aCZiCOiYfZLSIq0xIXC8zUkd

# If the variables are file paths (strings), open them
if isinstance(data_pkg_latest, str):
    with open(data_pkg_latest, 'r', encoding='utf-8') as f:
        data_pkg_latest = json.load(f)
if isinstance(data_proj_pkg, str):
    with open(data_proj_pkg, 'r', encoding='utf-8') as f:
        data_proj_pkg = json.load(f)
if isinstance(data_proj_info, str):
    with open(data_proj_info, 'r', encoding='utf-8') as f:
        data_proj_info = json.load(f)

# Create DataFrames
df_latest = pd.DataFrame(data_pkg_latest)
df_proj_pkg = pd.DataFrame(data_proj_pkg)
df_proj_info = pd.DataFrame(data_proj_info)

# Normalise columns
for df in (df_latest, df_proj_pkg):
    if 'System' not in df.columns:
        df['System'] = 'NPM'

# Extract repo and stars from Project_Information
def extract_repo(text):
    if not isinstance(text, str):
        return None
    # try several patterns
    patterns = [r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',
                r'under the name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',
                r'named\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)']
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            return m.group(1)
    return None

def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'([\d,]+)\s+stars', text, flags=re.IGNORECASE)
    if m:
        s = m.group(1).replace(',', '')
        try:
            return int(s)
        except:
            return None
    return None

# Apply extraction
df_proj_info['Repo'] = df_proj_info['Project_Information'].apply(extract_repo)
df_proj_info['Stars'] = df_proj_info['Project_Information'].apply(extract_stars)

# Drop rows without repo
df_proj_info = df_proj_info.dropna(subset=['Repo'])

# Aggregate to get max stars per repo (in case of duplicates)
df_repo_stars = df_proj_info.groupby('Repo', as_index=False)['Stars'].max()

# Merge latest packages with project_packageversion to get ProjectName
# Ensure columns types match
merge_cols = ['System', 'Name', 'Version']
df_join = pd.merge(df_latest, df_proj_pkg[['System','Name','Version','ProjectName']], on=merge_cols, how='left')

# Keep only rows with a ProjectName
df_join = df_join.dropna(subset=['ProjectName'])

# Merge with repo stars on ProjectName == Repo
df_join = df_join.merge(df_repo_stars, left_on='ProjectName', right_on='Repo', how='left')

# Convert Stars to numeric, fill missing with 0
df_join['Stars'] = pd.to_numeric(df_join['Stars']).fillna(0).astype(int)

# Get top 5 by Stars
df_top5 = df_join.sort_values('Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

# Prepare result list
result = []
for _, row in df_top5.iterrows():
    result.append({
        'Package': row['Name'],
        'Version': row['Version'],
        'ProjectName': row.get('ProjectName', None),
        'Stars': int(row['Stars'])
    })

# Output as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ahqwjozL6QvTYIUbXXnyJbvi': ['packageinfo'], 'var_call_O8NNkifflCK49r0SEgUGADGt': ['project_info', 'project_packageversion'], 'var_call_LexZ7D9ewAeYv1w6hl4D1ztH': 'file_storage/call_LexZ7D9ewAeYv1w6hl4D1ztH.json', 'var_call_VjHaCoRgGUMmcX1y4bYGiHth': 'file_storage/call_VjHaCoRgGUMmcX1y4bYGiHth.json', 'var_call_aCZiCOiYfZLSIq0xIXC8zUkd': 'file_storage/call_aCZiCOiYfZLSIq0xIXC8zUkd.json'}

exec(code, env_args)
