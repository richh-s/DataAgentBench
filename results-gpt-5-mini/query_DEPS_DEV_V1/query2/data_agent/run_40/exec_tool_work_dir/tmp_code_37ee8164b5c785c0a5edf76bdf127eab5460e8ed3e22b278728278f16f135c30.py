code = """import json, pandas as pd, re, os

# load variables from storage
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkgs = load_var(var_call_kD4sn1pJa9QNz9V5LEOrqkAz)
pv = load_var(var_call_HRkFdhHsY0VkVHQlfVue8KLl)
pi = load_var(var_call_Ji5a2DQEMyItZdOT0nXaYHdu)

df_pkgs = pd.DataFrame(pkgs)
df_pv = pd.DataFrame(pv)
df_pi = pd.DataFrame(pi)

# Merge packages with project_packageversion to get ProjectName
if not {'Name','Version'}.issubset(df_pkgs.columns):
    raise SystemExit('package data missing expected columns')
if not {'Name','Version','ProjectName'}.issubset(df_pv.columns):
    raise SystemExit('project_packageversion data missing expected columns')

merged = pd.merge(df_pkgs.drop_duplicates(), df_pv.drop_duplicates(), on=['Name','Version'], how='left')
# keep only rows with a project mapping
merged = merged[merged['ProjectName'].notna()]

# Build set of project names to match into project_info
proj_names = set(merged['ProjectName'].unique())

# For each project_info row, try to find which project name it refers to by substring matching
def find_projectname_in_info(info_text, proj_names):
    if not isinstance(info_text, str):
        return None
    for pname in proj_names:
        if pname in info_text:
            return pname
    return None

# Apply to df_pi
df_pi = df_pi.copy()
df_pi['ProjectName_extracted'] = df_pi['Project_Information'].apply(lambda x: find_projectname_in_info(x, proj_names))
# Keep only rows where we extracted a project name
df_pi_matched = df_pi[df_pi['ProjectName_extracted'].notna()].copy()

# Merge merged with project_info on ProjectName
final = pd.merge(merged, df_pi_matched, left_on='ProjectName', right_on='ProjectName_extracted', how='left')
# Filter rows that have project info and licenses
final = final[final['Project_Information'].notna()]

# Filter projects whose Licenses include MIT
def licenses_include_mit(lic_str):
    if not isinstance(lic_str, str):
        return False
    s = lic_str.strip()
    try:
        parsed = json.loads(s)
        if isinstance(parsed, list):
            return any((isinstance(x, str) and x.upper().strip()=="MIT") for x in parsed)
    except Exception:
        pass
    # fallback: substring match
    return 'MIT' in s

final['HasMIT'] = final['Licenses'].apply(licenses_include_mit)
final = final[final['HasMIT']]

# Extract fork counts from Project_Information
fork_re = re.compile(r"(\d{1,3}(?:,\d{3})*|\d+)\s*(?:forks|forked|fork)", re.IGNORECASE)
def extract_forks(text):
    if not isinstance(text, str):
        return None
    m = fork_re.search(text)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    # alternative pattern: 'been forked X times'
    m2 = re.search(r'been forked\s*(\d{1,3}(?:,\d{3})*|\d+)', text, re.IGNORECASE)
    if m2:
        num = m2.group(1).replace(',', '')
        try:
            return int(num)
        except:
            return None
    return None

final['Forks'] = final['Project_Information'].apply(extract_forks)
final['Forks'] = final['Forks'].fillna(0).astype(int)

# For each ProjectName, get the maximum forks and representative info
grouped = final.groupby('ProjectName').agg({
    'Forks': 'max',
    'Project_Information': 'first',
    'Licenses': 'first'
}).reset_index()

# Sort and take top 5
top5 = grouped.sort_values('Forks', ascending=False).head(5)

# Prepare result list
result = []
for _, row in top5.iterrows():
    result.append({
        'ProjectName': row['ProjectName'],
        'Forks': int(row['Forks']),
        'Project_Information': row['Project_Information'],
        'Licenses': row['Licenses']
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kD4sn1pJa9QNz9V5LEOrqkAz': 'file_storage/call_kD4sn1pJa9QNz9V5LEOrqkAz.json', 'var_call_HRkFdhHsY0VkVHQlfVue8KLl': 'file_storage/call_HRkFdhHsY0VkVHQlfVue8KLl.json', 'var_call_Ji5a2DQEMyItZdOT0nXaYHdu': 'file_storage/call_Ji5a2DQEMyItZdOT0nXaYHdu.json'}

exec(code, env_args)
