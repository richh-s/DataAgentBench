code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_XhC8HEB95z5IuuNjeoFhy00K, 'r') as f:
    pkg_data = json.load(f)
with open(var_call_X8SdG9RUMzFvg076xGYwkpy1, 'r') as f:
    proj_pkg_data = json.load(f)
with open(var_call_0jAb7jrxsVqizV8YrGsBmXjB, 'r') as f:
    proj_info_data = json.load(f)

pkg_df = pd.DataFrame(pkg_data)
proj_pkg_df = pd.DataFrame(proj_pkg_data)
proj_info_df = pd.DataFrame(proj_info_data)

# Merge package rows (which already filtered for NPM + MIT + IsRelease) with project_packageversion on System, Name, Version
merged = pd.merge(pkg_df, proj_pkg_df, on=['System', 'Name', 'Version'], how='inner')

# Consider only GitHub projects (ProjectType == 'GITHUB')
merged = merged[merged['ProjectType'] == 'GITHUB']

# Get unique ProjectName values
project_names = merged['ProjectName'].dropna().unique().tolist()

# Function to extract forks from Project_Information
def extract_forks(text):
    if not isinstance(text, str):
        return None
    # Look for patterns like '123 forks' or 'forked 123 times' but most entries use 'X forks'
    m = re.search(r"([0-9,]+)\s+forks", text)
    if m:
        return int(m.group(1).replace(',', ''))
    # try alternative: 'and X forks' or 'forks count of X'
    m = re.search(r"forks.*?([0-9,]+)", text)
    if m:
        return int(m.group(1).replace(',', ''))
    # try pattern 'forked X times' or 'forked X'
    m = re.search(r"forked\s+([0-9,]+)", text)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

# Build a mapping from repo (owner/repo) to project_info entries that mention it
results = []
for repo in project_names:
    # find rows in proj_info_df where Project_Information contains the repo string
    matches = proj_info_df[proj_info_df['Project_Information'].str.contains(repo, na=False)]
    forks_vals = []
    pis = None
    if not matches.empty:
        for _, row in matches.iterrows():
            fi = extract_forks(row.get('Project_Information', ''))
            if fi is not None:
                forks_vals.append(fi)
        # take the max forks if multiple
        forks = max(forks_vals) if forks_vals else None
        # capture the first Project_Information for context
        pis = matches.iloc[0].get('Project_Information', None)
    else:
        forks = None
    if forks is not None:
        results.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': pis})

# Sort by forks descending and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

# Prepare JSON-serializable string
output = results_sorted

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PmVwV753yy1yxWMmdukfdgdy': ['packageinfo'], 'var_call_JweEQj3u3T8LYqD5lYr8OAiD': ['project_info', 'project_packageversion'], 'var_call_XhC8HEB95z5IuuNjeoFhy00K': 'file_storage/call_XhC8HEB95z5IuuNjeoFhy00K.json', 'var_call_X8SdG9RUMzFvg076xGYwkpy1': 'file_storage/call_X8SdG9RUMzFvg076xGYwkpy1.json', 'var_call_0jAb7jrxsVqizV8YrGsBmXjB': 'file_storage/call_0jAb7jrxsVqizV8YrGsBmXjB.json'}

exec(code, env_args)
