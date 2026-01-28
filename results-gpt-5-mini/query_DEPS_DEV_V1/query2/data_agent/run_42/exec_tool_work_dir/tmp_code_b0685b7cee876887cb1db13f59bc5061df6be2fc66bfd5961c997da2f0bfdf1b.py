code = """import json
import pandas as pd
import re

# Load data from storage variables (file paths or direct lists)
def load_storage(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkgs = load_storage(var_call_q8IhPYIbKTQcSErterjq4d5n)
ppv = load_storage(var_call_EPqBtSQnfGDAjiONyg2HTIYm)
pinfo = load_storage(var_call_TIeUihCrO14cUJE95FPxLJkg)

# DataFrames
df_pkgs = pd.DataFrame(pkgs)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)

# Merge packageinfo filtered results with project_packageversion on System, Name, Version
# Ensure columns exist
for col in ['System','Name','Version']:
    if col not in df_pkgs.columns or col not in df_ppv.columns:
        raise ValueError(f"Missing column {col} in dataframes")

merged = df_pkgs.merge(df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Keep unique project names
project_names = merged['ProjectName'].dropna().unique().tolist()

# Prepare project_info: extract repo (owner/repo) and forks count and normalize licenses

def extract_repo(s):
    if not isinstance(s, str):
        return None
    # common patterns: "The project owner/repo" or "The GitHub project owner/repo" etc.
    m = re.search(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b", s)
    if m:
        return m.group(1)
    return None

# Extract forks using several heuristics
fork_patterns = [
    re.compile(r"([0-9][0-9,]*)\s*(?=forks)", re.IGNORECASE),
    re.compile(r"forks count of\s*([0-9][0-9,]*)", re.IGNORECASE),
    re.compile(r"forks, and\s*([0-9][0-9,]*)", re.IGNORECASE),
    re.compile(r"and\s*([0-9][0-9,]*)\s*forks", re.IGNORECASE),
]

def extract_forks(s):
    if not isinstance(s, str):
        return None
    for pat in fork_patterns:
        m = pat.search(s)
        if m:
            num = m.group(1).replace(',','')
            try:
                return int(num)
            except:
                continue
    return None

# Apply extraction
df_pinfo['repo_extracted'] = df_pinfo['Project_Information'].apply(extract_repo)
df_pinfo['forks_extracted'] = df_pinfo['Project_Information'].apply(extract_forks)

# Normalize Licenses to simple string
df_pinfo['Licenses_str'] = df_pinfo['Licenses'].astype(str)

# Filter project_info to those with repo in our project_names and license contains MIT
candidates = df_pinfo[df_pinfo['repo_extracted'].isin(project_names) & df_pinfo['Licenses_str'].str.contains('MIT', na=False)]

# Build mapping from repo -> forks (take max if multiple entries)
repo_forks = {}
for _, row in candidates.iterrows():
    repo = row['repo_extracted']
    forks = row['forks_extracted']
    if forks is None:
        continue
    if repo not in repo_forks or forks > repo_forks[repo]:
        repo_forks[repo] = forks

# Prepare result list
result_list = [{'ProjectName': repo, 'Forks': cnt} for repo, cnt in repo_forks.items()]
# Sort by forks desc and take top 5
result_list = sorted(result_list, key=lambda x: x['Forks'], reverse=True)[:5]

# Output JSON
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_q8IhPYIbKTQcSErterjq4d5n': 'file_storage/call_q8IhPYIbKTQcSErterjq4d5n.json', 'var_call_EPqBtSQnfGDAjiONyg2HTIYm': 'file_storage/call_EPqBtSQnfGDAjiONyg2HTIYm.json', 'var_call_TIeUihCrO14cUJE95FPxLJkg': 'file_storage/call_TIeUihCrO14cUJE95FPxLJkg.json'}

exec(code, env_args)
