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

# Filter out weird names (likely dependency paths)
df_pkg = df_pkg[~df_pkg['Name'].str.contains('>')]

df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Date desc
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates, keeping first (latest)
latest_pkgs = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# 2. Filter project mappings
df_proj = pd.DataFrame(project_package)
# Filter df_proj as well? Not strictly necessary if join keys match, but good for safety
df_proj = df_proj[~df_proj['Name'].str.contains('>')]

# Merge
merged = pd.merge(latest_pkgs, df_proj, on=['Name', 'Version'], how='inner')

# 3. Parse project info
project_stars = {}

def parse_project_info(text):
    name = None
    stars = 0
    
    # Extract Name
    # Case 1: "The project named owner/repo..."
    # Case 2: "The project owner/repo is..."
    # Case 3: "The project owner/repo on..."
    # Case 4: "The project is hosted on GitHub under the name owner/repo"
    # Case 5: "The project is a GitHub repository named owner/repo"
    # Case 6: "The GitHub project owner/repo currently..."
    
    # Try generic pattern first: "project ... owner/repo" where owner/repo is the first path-like string found?
    # No, too risky.
    
    # Combined regexes
    # We look for the project identifier. It usually has a slash: "owner/repo".
    # But sometimes just "repo"? No, mostly owner/repo.
    
    # Pattern A: "project [named] X [on|is|currently]"
    match_name = re.search(r"project\s+(?:named\s+|is\s+a\s+GitHub\s+repository\s+named\s+)?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)", text)
    
    if not match_name:
        # Pattern B: "under the name X,"
        match_name = re.search(r"under the name\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)", text)
        
    if not match_name:
        # Pattern C: "The GitHub project X currently"
        match_name = re.search(r"The\s+GitHub\s+project\s+([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)", text)
        
    if match_name:
        name = match_name.group(1).rstrip(',.')
        
    # Extract Stars
    match_stars = re.search(r"([\d,]+)\s+stars", text)
    if not match_stars:
        match_stars = re.search(r"stars\s+count\s+of\s+([\d,]+)", text)
        
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
        project_stars[p_name] = p_stars

# 4. Join Stars
def get_stars(row):
    # Try exact match
    s = project_stars.get(row['ProjectName'], 0)
    if s == 0 and row['ProjectName'] not in project_stars:
        # Fallback: maybe ProjectName in DB is different from ProjectInfo?
        # e.g. "leaflet/leaflet" vs "Leaflet/Leaflet" (case)
        # Try lower case matching
        # But for now assuming exact match or case insensitive match if needed
        # Let's try matching lower case keys
        pass
    return s

merged['Stars'] = merged.apply(get_stars, axis=1)

# Handle duplicate packages (if any remain)
# Sort by stars desc
sorted_df = merged.sort_values(by='Stars', ascending=False)
# If multiple rows for same Name, take the one with highest stars (though usually 1)
# But we might have duplicates if multiple projects map to same package.
final_df = sorted_df.drop_duplicates(subset=['Name'])

top_5 = final_df.head(5)
result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9554848968538350883': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-5738836302267607862': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-4800441277572895241': 'file_storage/function-call-4800441277572895241.json', 'var_function-call-542677843635182640': 'file_storage/function-call-542677843635182640.json', 'var_function-call-1804405089190849290': [{'count_star()': '770'}], 'var_function-call-12086757890660498677': 'file_storage/function-call-12086757890660498677.json', 'var_function-call-5394043733317327243': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}], 'var_function-call-5885061836512152918': [{'Name': '@dummmy/pack-cli>1.0.8>@babel/plugin-syntax-optional-chaining'}, {'Name': '@dpoineau/react-scripts>1.0.0>babel-core'}, {'Name': '@dmrvos/infrajs>0.0.7>@types/jquery'}, {'Name': '@dwarvesf/react-scripts>0.7.0>babel-plugin-transform-es2015-modules-umd'}, {'Name': '@dummmy/webpack-cli>1.0.7>@babel/template'}, {'Name': '@dummmy/webpack-cli>1.0.7>@babel/template'}, {'Name': '@dpoineau/react-scripts>1.0.0>js-yaml'}, {'Name': '@dpoineau/react-scripts>1.0.0>js-yaml'}, {'Name': '@dollarshaveclub/cli>1.10.0>jsprim'}, {'Name': '@dollarshaveclub/cli>1.10.0>jsprim'}]}

exec(code, env_args)
