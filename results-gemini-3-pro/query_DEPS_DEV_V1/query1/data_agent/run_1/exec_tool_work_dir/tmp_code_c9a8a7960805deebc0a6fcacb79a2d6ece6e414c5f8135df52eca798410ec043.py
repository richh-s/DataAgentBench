code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-17936320984994100568'], 'r') as f:
    package_data = json.load(f)
with open(locals()['var_function-call-5171920729111271395'], 'r') as f:
    project_package_data = json.load(f)
with open(locals()['var_function-call-13695207813627073106'], 'r') as f:
    project_info_data = json.load(f)

# 1. Identify latest release per package
df_pkg = pd.DataFrame(package_data)
# Convert UpstreamPublishedAt to float just in case
df_pkg['UpstreamPublishedAt'] = df_pkg['UpstreamPublishedAt'].astype(float)
# Find max UpstreamPublishedAt per Name
latest_idx = df_pkg.groupby('Name')['UpstreamPublishedAt'].idxmax()
df_latest = df_pkg.loc[latest_idx, ['Name', 'Version']]

# 2. Parse Project Info for Stars
project_stars = {}

# Regex patterns
# "currently has 0 open issues, 0 stars,"
# "stars count of 3761"
# "total of 2,534 stars"
patterns = [
    r"currently has.*?\s([\d,]+)\s+stars",
    r"stars count of\s*([\d,]+)",
    r"total of\s*([\d,]+)\s+stars",
    r"garnered.*?total of\s*([\d,]+)\s+stars",
    r",\s*([\d,]+)\s+stars" # fallback, might be risky
]

def parse_stars(text):
    if not text: return 0
    # Try specific patterns first
    for pat in [r"stars count of\s*([\d,]+)", r"total of\s*([\d,]+)\s+stars", r"currently has.*?\s([\d,]+)\s+stars"]:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return int(m.group(1).replace(',', ''))
    
    # Fallback: look for "X stars"
    m = re.search(r"([\d,]+)\s+stars", text)
    if m:
        # Check if it's not part of something else?
        # Usually safe given the context sentences.
        try:
            return int(m.group(1).replace(',', ''))
        except:
            pass
    return 0

def parse_project_name(text):
    # "The project lberrocal/npm-packages-template is hosted..."
    # "The project leaflet/leaflet on GitHub..."
    # "The project named leo-ran/easy-node-server is hosted..."
    # "The GitHub project named leviticusmb/divine-synchronization currently..."
    
    # Look for owner/repo format
    m = re.search(r"project\s+(?:named\s+)?([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    
    # Fallback
    m = re.search(r"([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)", text)
    if m:
        return m.group(1)
    return None

project_star_map = {}

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    # We need to link info to ProjectName. The info text contains the name.
    p_name = parse_project_name(info)
    stars = parse_stars(info)
    if p_name:
        project_star_map[p_name] = stars

# 3. Join Latest Packages with Project Names
df_pp = pd.DataFrame(project_package_data)
# df_pp has Name, Version, ProjectName
# df_latest has Name, Version

# Merge on Name AND Version to ensure we are looking at the latest version
merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='inner')

# 4. Map to Stars
merged['Stars'] = merged['ProjectName'].map(project_star_map)

# Drop rows where Stars is NaN (meaning project not found in project_info or parsing failed)
merged = merged.dropna(subset=['Stars'])
merged['Stars'] = merged['Stars'].astype(int)

# 5. Top 5
top5 = merged.sort_values(by=['Stars', 'Name'], ascending=[False, True]).head(5)

result = top5[['Name', 'Version']].to_dict(orient='records') # Just return Name, Version as requested?
# "which packages are the top 5 most popular based on the Github star number, as well as their versions?"
# Implies return Name and Version.

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15265893695332558738': ['packageinfo'], 'var_function-call-1015005864724100337': ['project_info', 'project_packageversion'], 'var_function-call-297498087076333845': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2551278673153472772': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3158966555197872046': [{'count(*)': '661372'}], 'var_function-call-17992344091215332840': [{'count_star()': '597602'}], 'var_function-call-13934852242877722428': [{'count_star()': '770'}], 'var_function-call-13695207813627073106': 'file_storage/function-call-13695207813627073106.json', 'var_function-call-5171920729111271395': 'file_storage/function-call-5171920729111271395.json', 'var_function-call-17936320984994100568': 'file_storage/function-call-17936320984994100568.json'}

exec(code, env_args)
