code = """import json
import re
import pandas as pd

# Load data from storage files
with open(var_call_66uLckAMqIRZipHif3zK6SKU, 'r') as f:
    pkg_latest = json.load(f)
with open(var_call_TKeeRf4uZRB6wcHVpJDO2cuZ, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_X7swye6rurMXNZTn569Tx9qP, 'r') as f:
    proj_info = json.load(f)

# DataFrames
df_pkg = pd.DataFrame(pkg_latest)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Keep only relevant columns
if 'System' in df_pkg.columns:
    df_pkg = df_pkg[['System','Name','Version']]
else:
    df_pkg = df_pkg[['Name','Version']]

# Merge latest packages with project_packageversion to get ProjectName
merged = pd.merge(df_pkg, df_proj_pkg[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# Build mapping from ProjectName to Project_Information
proj_info_map = {}
for idx, row in df_proj_info.iterrows():
    info = row.get('Project_Information')
    if not info or not isinstance(info, str):
        continue
    # try to extract owner/repo from the string using pattern 'The project owner/repo'
    m = re.search(r'The project\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', info)
    if m:
        key = m.group(1)
        # prefer first occurrence
        if key not in proj_info_map:
            proj_info_map[key] = info
    else:
        # also try pattern 'The GitHub project owner/repo'
        m2 = re.search(r'on GitHub under the name\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', info)
        if m2:
            key = m2.group(1)
            if key not in proj_info_map:
                proj_info_map[key] = info
        else:
            # try finding any owner/repo-like token
            m3 = re.search(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+) on GitHub', info)
            if m3:
                key = m3.group(1)
                if key not in proj_info_map:
                    proj_info_map[key] = info

# Function to extract stars from Project_Information text
star_re_patterns = [r'([0-9]{1,3}(?:,[0-9]{3})*)\s+stars',
                    r'stars count of\s+([0-9,]+)',
                    r'has garnered (?:a total of )?([0-9,]+) stars',
                    r'has a total of\s+([0-9,]+) stars']

def extract_stars(text):
    if not text or not isinstance(text, str):
        return None
    for pat in star_re_patterns:
        m = re.search(pat, text)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    # fallback: find any number followed by 'stars' later
    m = re.search(r'([0-9,]+)\s+stars', text)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            return None
    return None

# For each merged row, get Project_Information via proj_info_map
def find_project_info(project_name):
    if not isinstance(project_name, str):
        return None
    if project_name in proj_info_map:
        return proj_info_map[project_name]
    # try variations: some project_info may have 'owner/repo' without exact match; try to find any info containing project_name
    for key, info in proj_info_map.items():
        if project_name.lower() == key.lower():
            return info
    # as last resort, search through all project_info entries for a substring match
    for info in df_proj_info['Project_Information'].dropna().astype(str):
        if project_name in info:
            return info
    return None

# Attach project info and stars
merged['Project_Information'] = merged['ProjectName'].apply(find_project_info)
merged['Stars'] = merged['Project_Information'].apply(extract_stars)

# For packages without direct mapping, Stars may be NaN; set to 0 for ranking
merged['Stars'] = merged['Stars'].fillna(0).astype(int)

# For packages that map to multiple project entries, keep the maximum stars per package (though merged is per package already)
# Group by package Name and Version (should be unique), but ensure uniqueness
grouped = merged.groupby(['Name','Version','ProjectName'], as_index=False)['Stars'].max()

# Now sort by Stars desc and take top 5
top5 = grouped.sort_values('Stars', ascending=False).head(5)

# Prepare output
result = []
for _, r in top5.iterrows():
    result.append({
        'Name': r['Name'],
        'Version': r['Version'],
        'Stars': int(r['Stars']),
        'ProjectName': r['ProjectName'] if pd.notna(r['ProjectName']) else None
    })

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_66uLckAMqIRZipHif3zK6SKU': 'file_storage/call_66uLckAMqIRZipHif3zK6SKU.json', 'var_call_TKeeRf4uZRB6wcHVpJDO2cuZ': 'file_storage/call_TKeeRf4uZRB6wcHVpJDO2cuZ.json', 'var_call_X7swye6rurMXNZTn569Tx9qP': 'file_storage/call_X7swye6rurMXNZTn569Tx9qP.json'}

exec(code, env_args)
