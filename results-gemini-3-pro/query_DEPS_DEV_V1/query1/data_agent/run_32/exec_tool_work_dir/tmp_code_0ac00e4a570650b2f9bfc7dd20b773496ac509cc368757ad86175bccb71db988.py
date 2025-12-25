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
projects = []
# Common regex patterns for extracting name and stars
# Pattern 1: "The project <name> is hosted on GitHub ... <stars> stars"
# Pattern 2: "The project <name> on GitHub ... <stars> stars"
# Pattern 3: "The GitHub project <name> currently has ... <stars> stars"
# Pattern 4: "The project is hosted on GitHub under the name <name> ... <stars> stars"
# Pattern 5: "The project named <name> is hosted on GitHub ... <stars> stars"
# Pattern 6: "The project is a GitHub repository named <name> ... <stars> stars"
# Pattern 7: "The GitHub project named <name> ... <stars> stars"

# I'll use a combined approach or try multiple.
# Note: The stars count might be "0" or "10,249" (with commas).

def parse_project_info(info_str):
    # Extract Stars
    # Look for "X stars" where X is a number (possibly with commas)
    stars_match = re.search(r'(\d[\d,]*)\s+stars', info_str)
    stars = 0
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    
    # Extract Name
    # This is trickier. Let's try to find the pattern "project <name>" or "named <name>" or "name <name>"
    # Most patterns start with "The project" or "The GitHub project".
    # The name usually contains '/' for owner/repo, but not always if it's just a repo name (but usually owner/repo in these DBs).
    # Let's look for the owner/repo pattern `[\w\-\.]+ / [\w\-\.]+` roughly.
    
    # Refined regex for name:
    # "The project ([\w\-\./]+) is hosted"
    # "The project ([\w\-\./]+) on GitHub"
    # "The GitHub project ([\w\-\./]+) currently"
    # "name ([\w\-\./]+), and"
    # "named ([\w\-\./]+) is hosted"
    # "named ([\w\-\./]+) on GitHub"
    # "named ([\w\-\./]+) currently"
    
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
        r"The project\s+([\w\-\./]+)\s+currently" # Fallback
    ]
    
    for pat in patterns:
        m = re.search(pat, info_str)
        if m:
            name = m.group(1)
            # Cleanup trailing dots or commas if regex caught them (though \w\-\./ shouldn't catch comma)
            break
            
    if not name:
        # Fallback: look for any string with "/" that isn't a URL?
        # But some might be "owner/repo".
        # Let's try to find a word with a slash in the first half of the string.
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
# Remove duplicates if any (keep max stars?)
df_projects = df_projects.sort_values('Stars', ascending=False).drop_duplicates('ProjectName')

# 2. Process Packages (Find Latest)
df_packages = pd.DataFrame(package_data)
# Convert UpstreamPublishedAt to float
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
# Drop rows with no time
df_packages = df_packages.dropna(subset=['UpstreamPublishedAt'])
# Find max time per Name
idx = df_packages.groupby('Name')['UpstreamPublishedAt'].idxmax()
df_latest_packages = df_packages.loc[idx]

# 3. Process Mapping
df_mapping = pd.DataFrame(mapping_data)

# 4. Join
# Join Latest Packages with Mapping
# mapping has (Name, Version, ProjectName)
# latest has (Name, Version)
# Inner join on Name and Version
merged = pd.merge(df_latest_packages, df_mapping, on=['Name', 'Version'], how='inner')

# Join with Projects (Stars)
final_df = pd.merge(merged, df_projects, on='ProjectName', how='inner')

# 5. Top 5
top_5 = final_df.sort_values('Stars', ascending=False).head(5)

result = top_5[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2039732020817722549': ['project_info', 'project_packageversion'], 'var_function-call-2039732020817719890': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2039732020817721327': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-1135659811635837986': [{'COUNT(*)': '661372'}], 'var_function-call-1135659811635838801': [{'count_star()': '597602'}], 'var_function-call-1135659811635835520': [{'count_star()': '770'}], 'var_function-call-111227086617338357': 'file_storage/function-call-111227086617338357.json', 'var_function-call-111227086617339750': 'file_storage/function-call-111227086617339750.json', 'var_function-call-111227086617341143': 'file_storage/function-call-111227086617341143.json'}

exec(code, env_args)
