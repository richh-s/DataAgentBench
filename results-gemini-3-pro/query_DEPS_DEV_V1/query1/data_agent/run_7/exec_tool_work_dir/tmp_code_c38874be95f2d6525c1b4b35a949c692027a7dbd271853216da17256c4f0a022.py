code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-4800441277572895241'], 'r') as f:
    package_info = json.load(f)

with open(locals()['var_function-call-542677843635182640'], 'r') as f:
    project_package = json.load(f)

with open(locals()['var_function-call-12086757890660498677'], 'r') as f:
    project_info_list = json.load(f)

# 1. Get latest version for each package
df_pkg = pd.DataFrame(package_info)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Date desc
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates, keeping first (latest)
latest_pkgs = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]
latest_pkg_set = set(zip(latest_pkgs['Name'], latest_pkgs['Version']))

# 2. Filter project mappings
# Create a set of (Name, Version) keys for fast lookup
# Or just filter the dataframe if I convert project_package to DF
df_proj = pd.DataFrame(project_package)
# Filter
# We only want rows where (Name, Version) is in latest_pkg_set
# Merging is easier
merged = pd.merge(latest_pkgs, df_proj, on=['Name', 'Version'], how='inner')
# merged columns: Name, Version, ProjectName

# 3. Parse project info
project_stars = {}

def parse_project_info(text):
    # Regex for name
    # Common prefix: "The project " or "The GitHub project "
    # Case 1: "The project owner/repo is..." or "The project owner/repo on..."
    # Case 2: "The project named owner/repo..."
    # Case 3: "The project is hosted on GitHub under the name owner/repo..."
    # Case 4: "The project is a GitHub repository named owner/repo..."
    
    name = None
    stars = 0
    
    # Extract Name
    # Try specific patterns first
    match_name = re.search(r"under the name\s+([\w\-\./]+)[,]", text)
    if not match_name:
        match_name = re.search(r"repository named\s+([\w\-\./]+)[,]", text)
    if not match_name:
        match_name = re.search(r"project\s+(?:named\s+)?([\w\-\./]+)\s+(?:on|is|currently)", text)
    
    if match_name:
        name = match_name.group(1)
        # Clean trailing punctuation if any (though \w should be safe, but . or - might be at end?)
        # Actually / is included.
        # Sometimes it might match "is" if not careful? No, space after.
    
    # Extract Stars
    # "X stars" or "stars count of X"
    match_stars = re.search(r"([\d,]+)\s+stars", text)
    if not match_stars:
        match_stars = re.search(r"stars count of\s+([\d,]+)", text)
        
    if match_stars:
        stars_str = match_stars.group(1).replace(',', '')
        try:
            stars = int(stars_str)
        except:
            stars = 0
            
    return name, stars

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    p_name, p_stars = parse_project_info(text)
    if p_name:
        # Normalize name?
        project_stars[p_name] = p_stars

# 4. Join Stars
# merged has Name, Version, ProjectName
def get_stars(p_name):
    return project_stars.get(p_name, 0)

merged['Stars'] = merged['ProjectName'].apply(get_stars)

# 5. Sort and Top 5
top_5 = merged.sort_values(by='Stars', ascending=False).head(5)

result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9554848968538350883': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-5738836302267607862': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-4800441277572895241': 'file_storage/function-call-4800441277572895241.json', 'var_function-call-542677843635182640': 'file_storage/function-call-542677843635182640.json', 'var_function-call-1804405089190849290': [{'count_star()': '770'}], 'var_function-call-12086757890660498677': 'file_storage/function-call-12086757890660498677.json'}

exec(code, env_args)
