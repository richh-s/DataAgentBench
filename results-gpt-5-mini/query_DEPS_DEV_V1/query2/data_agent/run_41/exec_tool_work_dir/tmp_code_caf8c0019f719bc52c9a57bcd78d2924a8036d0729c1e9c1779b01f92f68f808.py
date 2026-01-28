code = """import json, re
from pathlib import Path
import pandas as pd

# load previous tool outputs (file paths)
packages_path = Path(var_call_Iqly7QLfJkb6B2iGc5R4PejT)
proj_ver_path = Path(var_call_Mp3mFzO9xZclqsl4MQsXtZ4j)
proj_info_path = Path(var_call_soI9EiS4kpSiHsJ4GvPqV5ER)

packages = json.loads(packages_path.read_text())
proj_versions = json.loads(proj_ver_path.read_text())
proj_info = json.loads(proj_info_path.read_text())

# DataFrames
df_packages = pd.DataFrame(packages)
df_proj_versions = pd.DataFrame(proj_versions)
df_proj_info = pd.DataFrame(proj_info)

# Merge packages with project versions to get ProjectName for matching packages
merged = pd.merge(df_packages, df_proj_versions[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
# Unique project names mapped from packages
project_names = merged['ProjectName'].dropna().unique().tolist()

# Function to extract repo and forks from Project_Information
repo_pattern_list = [r'under the name\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)',
                     r'The GitHub project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)',
                     r'The project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)',
                     r'GitHub project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)',
                     r'hosted on GitHub under the name\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)']

fork_patterns = [r'(\d{1,3}(?:,\d{3})*)\s+forks',
                 r'forked\s+(\d{1,3}(?:,\d{3})*)\s+times',
                 r'forks count of\s*(\d{1,3}(?:,\d{3})*)',
                 r'forks count[:\s]+(\d{1,3}(?:,\d{3})*)']

repo_forks = {}
for rec in proj_info:
    info = rec.get('Project_Information') or ''
    repo = None
    for pat in repo_pattern_list:
        m = re.search(pat, info, re.IGNORECASE)
        if m:
            repo = m.group(1)
            break
    if not repo:
        # try find any owner/repo pattern
        m = re.search(r'([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)', info)
        if m:
            repo = m.group(1)
    # extract forks
    forks = None
    for pat in fork_patterns:
        m = re.search(pat, info)
        if m:
            forks = int(m.group(1).replace(',',''))
            break
    if forks is None:
        # try to capture pattern like 'and 5782 forks'
        m = re.search(r'and\s+(\d{1,3}(?:,\d{3})*)\s+forks', info)
        if m:
            forks = int(m.group(1).replace(',',''))
    if forks is None:
        # try pattern 'has been forked 12 times' already covered; else default 0
        forks = 0
    if repo:
        # keep max forks if multiple entries
        prev = repo_forks.get(repo)
        if prev is None or forks > prev:
            repo_forks[repo] = forks

# For any project_names that include a leading owner/repo but maybe in different case, normalize
# Compute top 5 among project_names by looking up in repo_forks
rows = []
for pn in project_names:
    forks = repo_forks.get(pn)
    if forks is None:
        # try lowercase or variations
        forks = repo_forks.get(pn.lower(), 0)
    rows.append({'ProjectName': pn, 'Forks': int(forks)})

# Sort and take top 5
rows_sorted = sorted(rows, key=lambda r: r['Forks'], reverse=True)
top5 = rows_sorted[:5]

# If less than 5, still return available
result = top5

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Iqly7QLfJkb6B2iGc5R4PejT': 'file_storage/call_Iqly7QLfJkb6B2iGc5R4PejT.json', 'var_call_3lf0gkjywWJYVprCwlC9j9Vc': 'file_storage/call_3lf0gkjywWJYVprCwlC9j9Vc.json', 'var_call_l4He0Tc1VHk8cDEEE47f8yJw': ['project_info', 'project_packageversion'], 'var_call_7KG3DCq44f5oPM8C9QGZrzKC': 'file_storage/call_7KG3DCq44f5oPM8C9QGZrzKC.json', 'var_call_Mp3mFzO9xZclqsl4MQsXtZ4j': 'file_storage/call_Mp3mFzO9xZclqsl4MQsXtZ4j.json', 'var_call_soI9EiS4kpSiHsJ4GvPqV5ER': 'file_storage/call_soI9EiS4kpSiHsJ4GvPqV5ER.json'}

exec(code, env_args)
