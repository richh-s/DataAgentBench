code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_Pq6tzr2g1IHWUB7iUXwchTV6, 'r') as f:
    pkg_latest = json.load(f)
with open(var_call_qSOGE5XKZQpMlKlv6zb4mOPf, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_eXkL3pEpCCNV9MYYgz5cqTqE, 'r') as f:
    proj_info = json.load(f)

df_pkg = pd.DataFrame(pkg_latest)
df_projpkg = pd.DataFrame(proj_pkg)
df_pinfo = pd.DataFrame(proj_info)

# Merge latest package versions with project_packageversion on System, Name, Version
merged = pd.merge(df_pkg, df_projpkg, on=['System', 'Name', 'Version'], how='inner')

# Prepare project_info text for faster searching
# Ensure Project_Information is string
df_pinfo['Project_Information'] = df_pinfo['Project_Information'].astype(str)

# Function to extract star count from project information text
star_patterns = [r"([0-9][0-9,]*)\s*stars",
                 r"stars count of\s*([0-9][0-9,]*)",
                 r"a total of\s*([0-9][0-9,]*)\s*stars",
                 r"stars count is\s*([0-9][0-9,]*)"]

def extract_stars(text):
    if not text or not isinstance(text, str):
        return 0
    text_lower = text.lower()
    for pat in star_patterns:
        m = re.search(pat, text_lower)
        if m:
            try:
                return int(m.group(1).replace(',', ''))
            except:
                continue
    return 0

# Build a mapping from ProjectName to stars by searching project_info for substring matches
project_names = merged['ProjectName'].astype(str).unique()
projname_to_stars = {}

for pname in project_names:
    pname_lower = pname.lower()
    # find rows where Project_Information contains the project name
    candidates = df_pinfo[df_pinfo['Project_Information'].str.lower().str.contains(pname_lower, na=False)]
    stars_found = []
    if not candidates.empty:
        for txt in candidates['Project_Information'].tolist():
            stars_found.append(extract_stars(txt))
    else:
        # If no direct substring match, try matching just the repo part after slash
        if '/' in pname_lower:
            repo_part = pname_lower.split('/', 1)[1]
            candidates = df_pinfo[df_pinfo['Project_Information'].str.lower().str.contains(repo_part, na=False)]
            for txt in candidates['Project_Information'].tolist():
                stars_found.append(extract_stars(txt))

    projname_to_stars[pname] = max(stars_found) if stars_found else 0

# Attach stars to merged dataframe
merged['Stars'] = merged['ProjectName'].map(projname_to_stars).fillna(0).astype(int)

# For each package Name, Version pair, get the max stars (in case multiple project mappings exist)
grouped = merged.groupby(['Name', 'Version'], as_index=False)['Stars'].max()

# Sort by Stars desc and take top 5
top5 = grouped.sort_values('Stars', ascending=False).head(5)

# Prepare result list
result = []
for _, row in top5.iterrows():
    result.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'Stars': int(row['Stars'])
    })

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_Pq6tzr2g1IHWUB7iUXwchTV6': 'file_storage/call_Pq6tzr2g1IHWUB7iUXwchTV6.json', 'var_call_qSOGE5XKZQpMlKlv6zb4mOPf': 'file_storage/call_qSOGE5XKZQpMlKlv6zb4mOPf.json', 'var_call_eXkL3pEpCCNV9MYYgz5cqTqE': 'file_storage/call_eXkL3pEpCCNV9MYYgz5cqTqE.json'}

exec(code, env_args)
