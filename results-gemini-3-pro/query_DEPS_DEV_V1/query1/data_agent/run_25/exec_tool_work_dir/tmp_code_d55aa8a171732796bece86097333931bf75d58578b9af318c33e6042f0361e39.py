code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-6533266665392833605'], 'r') as f:
    latest_pkgs = json.load(f)
    
with open(locals()['var_function-call-2594427622717481590'], 'r') as f:
    pkg_mappings = json.load(f)

with open(locals()['var_function-call-11249593111119486648'], 'r') as f:
    proj_info = json.load(f)

# Convert to DataFrames
df_latest = pd.DataFrame(latest_pkgs)
df_map = pd.DataFrame(pkg_mappings)
df_info = pd.DataFrame(proj_info)

# Filter mappings to only latest packages
# Create a key for join
df_latest['key'] = df_latest['Name'] + "@@" + df_latest['Version']
df_map['key'] = df_map['Name'] + "@@" + df_map['Version']

# Keep only mappings that match latest packages
df_map_filtered = df_map[df_map['key'].isin(df_latest['key'])]

# Parse Project Info
def parse_info(text):
    # Regex for Project Name
    name_regexes = [
        r"The project ([^\s]+) is hosted on GitHub",
        r"The project ([^\s]+) on GitHub",
        r"The GitHub project ([^\s]+) currently",
        r"The project is hosted on GitHub under the name ([^\s]+),",
        r"The project named ([^\s]+) on GitHub",
        r"The GitHub project named ([^\s]+) currently",
        r"The project ([^\s]+) has an open issues",
        r"The project ([^\s]+) currently has" # fallback
    ]
    
    p_name = None
    for r in name_regexes:
        m = re.search(r, text)
        if m:
            candidate = m.group(1)
            # clean trailing comma or punctuation if any
            candidate = candidate.rstrip(",.")
            if "/" in candidate: # Valid names usually have owner/repo
                p_name = candidate
                break
    
    # Regex for Stars
    # "38,715 stars", "0 stars", "105 stars"
    stars = 0
    m_star = re.search(r"(\d+(?:,\d+)*) stars", text)
    if m_star:
        stars_str = m_star.group(1).replace(",", "")
        stars = int(stars_str)
        
    return p_name, stars

parsed_data = []
for entry in proj_info:
    text = entry.get('Project_Information', '')
    name, stars = parse_info(text)
    if name:
        parsed_data.append({'ProjectName': name, 'Stars': stars})

df_parsed_info = pd.DataFrame(parsed_data)

# Join Mappings with Info
# mappings has ProjectName, info has ProjectName and Stars
df_final = pd.merge(df_map_filtered, df_parsed_info, on='ProjectName', how='inner')

# Sort by Stars
df_final = df_final.sort_values(by='Stars', ascending=False)

# Get top 5 distinct packages? 
# The query asks "which packages are the top 5 most popular... as well as their versions"
# Since we filtered for latest versions, each package name appears once (unless multiple projects map to it, but usually 1-1 or many-1).
# If multiple projects map to the same package, we might get duplicates or different star counts. 
# We should probably take the max stars for the package if ambiguous, but typically 1 package -> 1 repo.
# However, distinct packages means distinct Name.

df_final = df_final.drop_duplicates(subset=['Name'])
top_5 = df_final.head(5)[['Name', 'Version', 'Stars']]

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-2400554470036027377': ['project_info', 'project_packageversion'], 'var_function-call-7826454399859203854': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-16313167936421178255': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-17095951221475461517': [{'COUNT(*)': '661372'}], 'var_function-call-9493649555037983030': [{'COUNT(DISTINCT Name)': '16614'}], 'var_function-call-10744671647180174986': [{'count_star()': '597602'}], 'var_function-call-14411249742618821086': [{'count_star()': '770'}], 'var_function-call-6533266665392833605': 'file_storage/function-call-6533266665392833605.json', 'var_function-call-2594427622717481590': 'file_storage/function-call-2594427622717481590.json', 'var_function-call-11249593111119486648': 'file_storage/function-call-11249593111119486648.json'}

exec(code, env_args)
