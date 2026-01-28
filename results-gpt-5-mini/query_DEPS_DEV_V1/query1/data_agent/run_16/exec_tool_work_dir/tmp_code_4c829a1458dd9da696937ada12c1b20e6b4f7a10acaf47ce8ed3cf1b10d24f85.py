code = """import json
import pandas as pd
import re

# Load data from the storage-provided file paths
with open(var_call_JWWAF3JD5iD7ih8ELkIORMxh, 'r') as f:
    pkg_latest = json.load(f)
with open(var_call_XpFQDRvzBheC7cVWZTmeFf2z, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_pngh9bIZoogTY7aX8W79qM9n, 'r') as f:
    proj_info = json.load(f)

# Create DataFrames
df_pkg = pd.DataFrame(pkg_latest)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Ensure relevant columns exist
for col in ['System','Name','Version']:
    if col not in df_pkg.columns:
        df_pkg[col] = None

# Merge package (latest) with project_packageversion on System, Name, Version
# project_packageversion may have multiple entries; keep first match
merged = pd.merge(df_pkg, df_proj_pkg, on=['System','Name','Version'], how='inner')

# Build a mapping from Project_Information text to that text for quick search
proj_info_texts = df_proj_info['Project_Information'].astype(str).tolist()

# Function to extract stars from project_info text
def extract_stars(text):
    if not isinstance(text, str):
        return None
    # try several regex patterns to capture numbers before 'star' or 'stars'
    patterns = [r"([\d,]+)\s+stars",
                r"stars count of\s+([\d,]+)",
                r"a total of\s+([\d,]+)\s+stars",
                r"has garnered a total of\s+([\d,]+)\s+stars",
                r"has\s+([\d,]{1,3}(?:[,\d]{3})*)\s+stars",
                r"has\s+an?\s+stars?\s+count\s+of\s+([\d,]+)"]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    # fallback: look for pattern like '<number> stars' anywhere
    m = re.search(r"([\d,]+)\s+star", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    return None

# For each merged row, find the project_info entry that contains the ProjectName and extract stars
results = []
for _, row in merged.iterrows():
    projname = row.get('ProjectName')
    if not isinstance(projname, str):
        continue
    # search for projname in project_info texts
    matched_text = None
    for txt in proj_info_texts:
        if projname in txt:
            matched_text = txt
            break
    stars = None
    if matched_text is not None:
        stars = extract_stars(matched_text)
    # If not matched_text, try to extract from any project_info that contains repo name (last part)
    if matched_text is None:
        # try matching by repo suffix
        repo_suffix = projname.split('/')[-1]
        for txt in proj_info_texts:
            if f"/{repo_suffix}" in txt or repo_suffix in txt:
                matched_text = txt
                stars = extract_stars(txt)
                if stars is not None:
                    break
    # Default stars to 0 if None
    if stars is None:
        stars = 0
    results.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'ProjectName': projname,
        'Stars': stars
    })

# Create DataFrame of results and deduplicate by package name (keep entry with highest stars if duplicates)
res_df = pd.DataFrame(results)
# In case multiple project mappings for same package, keep the one with max stars
res_df = res_df.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

# Get top 5 packages by Stars
top5 = res_df.sort_values('Stars', ascending=False).head(5)

# Prepare output list
out = []
for _, r in top5.iterrows():
    out.append({'Name': r['Name'], 'Version': r['Version'], 'ProjectName': r['ProjectName'], 'Stars': int(r['Stars'])})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_JWWAF3JD5iD7ih8ELkIORMxh': 'file_storage/call_JWWAF3JD5iD7ih8ELkIORMxh.json', 'var_call_WvNJsnDmnc5Ku6vO5XaBvQ3Y': ['project_info', 'project_packageversion'], 'var_call_XpFQDRvzBheC7cVWZTmeFf2z': 'file_storage/call_XpFQDRvzBheC7cVWZTmeFf2z.json', 'var_call_pngh9bIZoogTY7aX8W79qM9n': 'file_storage/call_pngh9bIZoogTY7aX8W79qM9n.json'}

exec(code, env_args)
