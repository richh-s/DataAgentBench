code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_lPMRggVb5X7vGgavnR6xhWgb, 'r') as f:
    pkgs = json.load(f)
with open(var_call_mf0iD7IkH0Wu2yq9OuPBftZQ, 'r') as f:
    ppv = json.load(f)
with open(var_call_XEEyj6qMazao1eQ3UGsS36TG, 'r') as f:
    proj = json.load(f)

# DataFrames
df_pkgs = pd.DataFrame(pkgs)
df_ppv = pd.DataFrame(ppv)
df_proj = pd.DataFrame(proj)

# Normalize columns
for df in (df_pkgs, df_ppv):
    if 'System' in df.columns:
        df['System'] = df['System'].astype(str)
    if 'Name' in df.columns:
        df['Name'] = df['Name'].astype(str)
    if 'Version' in df.columns:
        df['Version'] = df['Version'].astype(str)

# Merge packages with project_packageversion on System, Name, Version
merged = pd.merge(df_pkgs, df_ppv, on=['System','Name','Version'], how='inner')

# Get unique ProjectName values
if 'ProjectName' in merged.columns:
    project_names = merged['ProjectName'].dropna().unique().tolist()
else:
    project_names = []

# Prepare function to extract forks from Project_Information
def extract_forks(text):
    if not isinstance(text, str):
        return None
    # look for patterns like '1234 forks', 'forks count of 1234', 'and 1234 forks'
    m = re.search(r"([\d,]+)\s*(?:forks|fork)\b", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    return None

# Build mapping from projectName to best fork count found in project_info
proj_info_texts = df_proj['Project_Information'].astype(str).tolist()

results = []
for pname in project_names:
    best = None
    # search all project_info entries that mention the repo name
    for text in proj_info_texts:
        if pname.lower() in text.lower():
            forks = extract_forks(text)
            if forks is not None:
                if best is None or forks > best:
                    best = forks
    # If best is still None, try to find numeric mention with owner or repo separately
    if best is None:
        # try splitting owner/repo
        if '/' in pname:
            owner, repo = pname.split('/',1)
            for text in proj_info_texts:
                if repo.lower() in text.lower():
                    forks = extract_forks(text)
                    if forks is not None:
                        if best is None or forks > best:
                            best = forks
    # default to 0 if not found
    forks_val = best if best is not None else 0
    results.append({'ProjectName': pname, 'Forks': forks_val})

# Sort and pick top 5
top5 = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

# Ensure JSON serializable
out = json.dumps(top5)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_lPMRggVb5X7vGgavnR6xhWgb': 'file_storage/call_lPMRggVb5X7vGgavnR6xhWgb.json', 'var_call_mf0iD7IkH0Wu2yq9OuPBftZQ': 'file_storage/call_mf0iD7IkH0Wu2yq9OuPBftZQ.json', 'var_call_XEEyj6qMazao1eQ3UGsS36TG': 'file_storage/call_XEEyj6qMazao1eQ3UGsS36TG.json'}

exec(code, env_args)
