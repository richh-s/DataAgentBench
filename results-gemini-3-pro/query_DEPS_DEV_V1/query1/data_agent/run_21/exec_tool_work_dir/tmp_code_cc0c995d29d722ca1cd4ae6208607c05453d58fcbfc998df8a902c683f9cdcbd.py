code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-1061209119833448743'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-1061209119833451694'], 'r') as f:
    package_version_data = json.load(f)

with open(locals()['var_function-call-1061209119833450549'], 'r') as f:
    package_info_data = json.load(f)

# 1. Process Project Info
projects = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    
    # Extract Name
    # Look for "owner/repo"
    # Patterns observed: 
    # "The project owner/repo..."
    # "The GitHub project owner/repo..."
    # "under the name owner/repo..."
    # "The project is a GitHub repository named owner/repo..."
    # "The project named owner/repo..."
    
    # Regex to capture owner/repo: words/dots/dashes followed by slash followed by words/dots/dashes
    name_match = re.search(r'(?:project|name|repository named)\s+([\w\-\.]+\/[\w\-\.]+)', info)
    
    # Extract Stars
    # Patterns:
    # "X stars"
    # "stars count of X"
    # "received X stars"
    # "garnered a total of X stars"
    # Handle commas in numbers
    
    stars_match = re.search(r'(\d[\d,]*)\s+stars', info)
    if not stars_match:
        stars_match = re.search(r'stars count of\s+(\d[\d,]*)', info)
        
    if name_match and stars_match:
        p_name = name_match.group(1)
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
            projects.append({'ProjectName': p_name, 'Stars': stars})
        except:
            continue

df_projects = pd.DataFrame(projects)

# 2. Process Package Version Mapping
df_pkg_ver = pd.DataFrame(package_version_data)
# df_pkg_ver has Name, Version, ProjectName

# Merge to link Packages to Stars
df_mapped = pd.merge(df_pkg_ver, df_projects, on='ProjectName', how='inner')

# 3. Process Package Info to find Latest Release
df_info = pd.DataFrame(package_info_data)

def parse_version_info(x):
    try:
        if isinstance(x, str):
            d = json.loads(x)
            return d.get('IsRelease', False), d.get('Ordinal', -1)
    except:
        pass
    return False, -1

# Apply parsing
# This might be slow if 600k rows, but manageable.
parsed = df_info['VersionInfo'].apply(parse_version_info)
df_info['IsRelease'] = parsed.apply(lambda x: x[0])
df_info['Ordinal'] = parsed.apply(lambda x: x[1])

# Filter for releases
df_releases = df_info[df_info['IsRelease'] == True]

# Find max ordinal per package
# Sort by Name and Ordinal desc
df_releases = df_releases.sort_values(by=['Name', 'Ordinal'], ascending=[True, False])
# Drop duplicates keeping top
df_latest = df_releases.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]
df_latest.rename(columns={'Version': 'LatestVersion'}, inplace=True)

# 4. Filter mapped packages for latest version
df_final = pd.merge(df_mapped, df_latest, on='Name', how='inner')
df_final = df_final[df_final['Version'] == df_final['LatestVersion']]

# 5. Sort and Top 5
# Handle potential duplicates if multiple projects link to same package (take max stars)
df_final = df_final.sort_values(by='Stars', ascending=False)
# Drop duplicates by Name to ensure distinct packages
df_final = df_final.drop_duplicates(subset=['Name'], keep='first')

top_5 = df_final[['Name', 'Version', 'Stars']].head(5)

result_json = top_5.to_json(orient='records')
print("__RESULT__:")
print(result_json)"""

env_args = {'var_function-call-7025636698027820361': ['project_info', 'project_packageversion'], 'var_function-call-7025636698027820920': ['packageinfo'], 'var_function-call-1516181120121544106': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-1516181120121541795': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1516181120121543580': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-6177134456124082482': [{'count(*)': '661372'}], 'var_function-call-6177134456124084175': [{'count_star()': '597602'}], 'var_function-call-6177134456124081772': [{'count_star()': '770'}], 'var_function-call-1061209119833448743': 'file_storage/function-call-1061209119833448743.json', 'var_function-call-1061209119833451694': 'file_storage/function-call-1061209119833451694.json', 'var_function-call-1061209119833450549': 'file_storage/function-call-1061209119833450549.json'}

exec(code, env_args)
