code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-6713805549134767544'], 'r') as f:
    project_info_data = json.load(f)
with open(locals()['var_function-call-6713805549134767079'], 'r') as f:
    mappings_data = json.load(f)
with open(locals()['var_function-call-6713805549134766614'], 'r') as f:
    package_data = json.load(f)

# 1. Process project_info to get (ProjectName, Stars)
projects_list = []
name_pattern = re.compile(r"(?:project|name)\s+(?:(?:is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name|on\s+GitHub,\s+named|GitHub\s+project|named)\s+)?([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)", re.IGNORECASE)
stars_pattern = re.compile(r"(\d+(?:,\d+)*)\s+stars", re.IGNORECASE)

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    if not info:
        continue
    
    stars_match = stars_pattern.search(info)
    stars = 0
    if stars_match:
        stars = int(stars_match.group(1).replace(',', ''))
    
    name_match = name_pattern.search(info)
    if name_match:
        project_name = name_match.group(1)
        if project_name.endswith('.') or project_name.endswith(','):
            project_name = project_name[:-1]
        projects_list.append({'ProjectName': project_name, 'Stars': stars})

df_projects = pd.DataFrame(projects_list)

# 2. Process packages
df_packages = pd.DataFrame(package_data)
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_latest = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name')
df_latest = df_latest[['Name', 'Version']]

# 3. Process mappings
df_mappings = pd.DataFrame(mappings_data)

# 4. Join
df_joined = pd.merge(df_latest, df_mappings, on=['Name', 'Version'], how='inner')
df_final = pd.merge(df_joined, df_projects, on='ProjectName', how='inner')

# 5. Top 5
df_final = df_final.drop_duplicates('Name')
top_5 = df_final.sort_values('Stars', ascending=False).head(5)

result = top_5[['Name', 'Version']].to_dict(orient='records')
# I'll print with Stars for internal verification, but output plain list as requested?
# "which packages ... as well as their versions"
# I will output the list of dicts.

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12194318604120634057': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-12194318604120637218': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-12194318604120636283': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-11957998869366056697': [{'count(*)': '661372'}], 'var_function-call-11957998869366055766': [{'count_star()': '597602'}], 'var_function-call-11957998869366058931': [{'count_star()': '770'}], 'var_function-call-6713805549134767544': 'file_storage/function-call-6713805549134767544.json', 'var_function-call-6713805549134767079': 'file_storage/function-call-6713805549134767079.json', 'var_function-call-6713805549134766614': 'file_storage/function-call-6713805549134766614.json'}

exec(code, env_args)
