code = """import json
import re
import pandas as pd
import numpy as np

# Load data
with open(locals()['var_function-call-17936320984994100568'], 'r') as f:
    package_data = json.load(f)
with open(locals()['var_function-call-5171920729111271395'], 'r') as f:
    project_package_data = json.load(f)
with open(locals()['var_function-call-13695207813627073106'], 'r') as f:
    project_info_data = json.load(f)

# 1. Identify latest release per package
df_pkg = pd.DataFrame(package_data)
# Convert UpstreamPublishedAt to float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Drop rows with NaN in UpstreamPublishedAt
df_pkg = df_pkg.dropna(subset=['UpstreamPublishedAt'])
# Find max UpstreamPublishedAt per Name
# reset_index() helps avoid issues
latest_idx = df_pkg.groupby('Name')['UpstreamPublishedAt'].idxmax()
df_latest = df_pkg.loc[latest_idx, ['Name', 'Version']]

# 2. Parse Project Info for Stars
project_star_map = {}

def parse_stars(text):
    if not text: return 0
    # Specific patterns
    patterns = [
        r"currently has.*?\s([\d,]+)\s+stars",
        r"stars count of\s*([\d,]+)",
        r"total of\s*([\d,]+)\s+stars",
        r"stars count of\s*([\d,]+)", 
        r"with a total of\s*([\d,]+)\s+stars"
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return int(m.group(1).replace(',', ''))
    
    # Fallback: "X stars"
    # But be careful of "0 stars"
    m = re.search(r"([\d,]+)\s+stars", text)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    return 0

def parse_project_name(text):
    # Try "project owner/repo"
    m = re.search(r"project\s+(?:named\s+)?([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    # Try just "owner/repo" if it looks like a repo path near "project"
    # But risk of capturing other text.
    # Let's rely on the first pattern which catches "The project owner/repo ..."
    # Many descriptions start with "The project owner/repo is..."
    return None

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    p_name = parse_project_name(info)
    stars = parse_stars(info)
    
    # Sometimes project name extraction might fail or be slightly off (e.g. casing).
    # But let's assume standard casing.
    if p_name:
        project_star_map[p_name] = stars
        # Also add lowercase version just in case
        project_star_map[p_name.lower()] = stars

# 3. Join
df_pp = pd.DataFrame(project_package_data)
# Ensure columns are strings
df_pp['Name'] = df_pp['Name'].astype(str)
df_pp['Version'] = df_pp['Version'].astype(str)
df_pp['ProjectName'] = df_pp['ProjectName'].astype(str)

df_latest['Name'] = df_latest['Name'].astype(str)
df_latest['Version'] = df_latest['Version'].astype(str)

merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='inner')

# 4. Map stars
# Try exact match, then lower case match
def get_stars(p_name):
    if p_name in project_star_map:
        return project_star_map[p_name]
    if p_name.lower() in project_star_map:
        return project_star_map[p_name.lower()]
    return None

merged['Stars'] = merged['ProjectName'].apply(get_stars)
merged = merged.dropna(subset=['Stars'])
merged['Stars'] = merged['Stars'].astype(int)

# 5. Top 5
top5 = merged.sort_values(by=['Stars', 'Name'], ascending=[False, True]).head(5)

result = top5[['Name', 'Version']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15265893695332558738': ['packageinfo'], 'var_function-call-1015005864724100337': ['project_info', 'project_packageversion'], 'var_function-call-297498087076333845': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2551278673153472772': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3158966555197872046': [{'count(*)': '661372'}], 'var_function-call-17992344091215332840': [{'count_star()': '597602'}], 'var_function-call-13934852242877722428': [{'count_star()': '770'}], 'var_function-call-13695207813627073106': 'file_storage/function-call-13695207813627073106.json', 'var_function-call-5171920729111271395': 'file_storage/function-call-5171920729111271395.json', 'var_function-call-17936320984994100568': 'file_storage/function-call-17936320984994100568.json'}

exec(code, env_args)
