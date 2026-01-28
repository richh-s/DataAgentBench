code = """import json
import pandas as pd
import re

# Load data from storage variables (could be lists or file paths)
def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to json
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_records = load_var(var_call_zQ1ZPdG5god3XI8z3Weab8Vn)
ppv_records = load_var(var_call_WwSZOAWnUPjJhseVprFhIpU3)
projinfo_records = load_var(var_call_2apy3t0L6VTREqSKb9n23XpG)

df_pkg = pd.DataFrame(pkg_records)
df_ppv = pd.DataFrame(ppv_records)
df_proj = pd.DataFrame(projinfo_records)

# Merge packageinfo with project_packageversion on System, Name, Version
merge_cols = ['System', 'Name', 'Version']
# Ensure columns exist
for c in merge_cols:
    if c not in df_pkg.columns or c not in df_ppv.columns:
        raise ValueError(f"Missing column {c} in one of the dataframes")

merged = pd.merge(df_pkg, df_ppv, on=merge_cols, how='inner')

# Get unique ProjectNames from merged
project_names = merged['ProjectName'].dropna().unique().tolist()

# Function to extract forks from a Project_Information string
def extract_forks(text):
    if not isinstance(text, str):
        return None
    # try patterns
    patterns = [r"([0-9,]+)\s+forks", r"forked\s+([0-9,]+)\s+times", r"forks count of\s*([0-9,]+)", r"forks count of\s*([0-9,]+)", r"forks[: ]\s*([0-9,]+)"]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1).replace(',', '')
            try:
                return int(num)
            except:
                pass
    # fallback: find 'and X forks' pattern with commas
    m = re.search(r"and\s+([0-9,]+)\s+forks", text, flags=re.IGNORECASE)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    # fallback: find any number near the word 'fork'
    m = re.search(r"([0-9,]{1,10}).{0,30}fork", text, flags=re.IGNORECASE)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    m = re.search(r"fork.{0,30}([0-9,]{1,10})", text, flags=re.IGNORECASE)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    return None

# Build a mapping from ProjectName to extracted forks and project_info text
results = []
for pname in project_names:
    # find project_info entries that contain the exact project name
    mask = df_proj['Project_Information'].astype(str).str.contains(re.escape(pname), case=False, na=False)
    matched_text = None
    forks = None
    if mask.any():
        # take the first matching entry
        matched_text = df_proj.loc[mask, 'Project_Information'].iloc[0]
        forks = extract_forks(matched_text)
    else:
        # No direct match; try to extract owner/repo from project info and match by last part (repo)
        # skip for now
        matched_text = None
        forks = None
    results.append({'ProjectName': pname, 'Forks': forks, 'Project_Information': matched_text})

# Filter out entries without forks (None) and sort
results_with_forks = [r for r in results if isinstance(r['Forks'], int)]
results_with_forks.sort(key=lambda x: x['Forks'], reverse=True)

top5 = results_with_forks[:5]

# Prepare output as JSON-serializable
output = top5

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_geOr1eVB2LFBJa0cNjAfQUZ4': ['packageinfo'], 'var_call_8MPPTiRSeesndHxxbFNUaOKX': ['project_info', 'project_packageversion'], 'var_call_zQ1ZPdG5god3XI8z3Weab8Vn': 'file_storage/call_zQ1ZPdG5god3XI8z3Weab8Vn.json', 'var_call_WwSZOAWnUPjJhseVprFhIpU3': 'file_storage/call_WwSZOAWnUPjJhseVprFhIpU3.json', 'var_call_2apy3t0L6VTREqSKb9n23XpG': 'file_storage/call_2apy3t0L6VTREqSKb9n23XpG.json'}

exec(code, env_args)
