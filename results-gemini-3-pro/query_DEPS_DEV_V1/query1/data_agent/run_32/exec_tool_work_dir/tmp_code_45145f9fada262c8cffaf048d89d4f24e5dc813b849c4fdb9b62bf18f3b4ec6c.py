code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-111227086617338357'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-111227086617339750'], 'r') as f:
    mapping_data = json.load(f)

with open(locals()['var_function-call-111227086617341143'], 'r') as f:
    package_data = json.load(f)

# 1. Process Project Info
def parse_project_info(info_str):
    stars_match = re.search(r'(\d[\d,]*)\s+stars', info_str)
    stars = 0
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    
    name = None
    patterns = [
        r"The project\s+([\w\-\./]+)\s+is hosted",
        r"The project\s+([\w\-\./]+)\s+on GitHub",
        r"The GitHub project\s+([\w\-\./]+)\s+currently",
        r"under the name\s+([\w\-\./]+),",
        r"repository named\s+([\w\-\./]+),",
        r"project named\s+([\w\-\./]+)\s+is hosted",
        r"project named\s+([\w\-\./]+)\s+currently",
        r"project named\s+([\w\-\./]+)\s+on GitHub",
        r"The project\s+([\w\-\./]+)\s+currently"
    ]
    for pat in patterns:
        m = re.search(pat, info_str)
        if m:
            name = m.group(1)
            break
            
    if not name:
        tokens = info_str.split()
        for t in tokens[:15]:
            if '/' in t and 'http' not in t and 'github.com' not in t:
                name = t.strip(',.')
                break
    return name, stars

project_list = []
for p in project_info_data:
    info = p.get('Project_Information', '')
    name, stars = parse_project_info(info)
    if name:
        project_list.append({'ProjectName': name, 'Stars': stars})

df_projects = pd.DataFrame(project_list)
df_projects = df_projects.sort_values('Stars', ascending=False).drop_duplicates('ProjectName')

# 2. Process Packages (Find Latest)
df_packages = pd.DataFrame(package_data)
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_packages = df_packages.dropna(subset=['UpstreamPublishedAt'])
# Sort by Name and Date desc, then drop duplicates keeping first (latest)
df_latest_packages = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name')

# 3. Process Mapping
df_mapping = pd.DataFrame(mapping_data)
# Remove duplicates in mapping
df_mapping = df_mapping.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# 4. Join
merged = pd.merge(df_latest_packages, df_mapping, on=['Name', 'Version'], how='inner')
final_df = pd.merge(merged, df_projects, on='ProjectName', how='inner')

# 5. Top 5 Distinct Packages
# We want "which packages". Distinct packages.
# Sort by Stars desc
final_df = final_df.sort_values('Stars', ascending=False)
# If multiple packages map to the same project, they will have same stars.
# We list them. But we want distinct *packages*.
# drop_duplicates on Name ensures distinct packages.
final_df_unique = final_df.drop_duplicates('Name')

top_10 = final_df_unique.head(10)
result = top_10[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2039732020817722549': ['project_info', 'project_packageversion'], 'var_function-call-2039732020817719890': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2039732020817721327': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-1135659811635837986': [{'COUNT(*)': '661372'}], 'var_function-call-1135659811635838801': [{'count_star()': '597602'}], 'var_function-call-1135659811635835520': [{'count_star()': '770'}], 'var_function-call-111227086617338357': 'file_storage/function-call-111227086617338357.json', 'var_function-call-111227086617339750': 'file_storage/function-call-111227086617339750.json', 'var_function-call-111227086617341143': 'file_storage/function-call-111227086617341143.json', 'var_function-call-15207619706595375808': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Stars': 57236, 'ProjectName': 'strapi/strapi'}]}

exec(code, env_args)
