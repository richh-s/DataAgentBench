code = """import json
import re
import pandas as pd

# Load project_info
with open(locals()['var_function-call-1247615843400787734'], 'r') as f:
    project_info_data = json.load(f)

project_stars = {}
# Regex to extract ProjectName and Stars
# Example: "The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks."
# Example: "The project named leo-ran/easy-node-server is hosted on GitHub..."
# Example: "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
# I'll use a few patterns.

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    if not info:
        continue
    
    # Extract stars
    # Pattern: "(\d+(?:,\d{3})*) stars"
    stars_match = re.search(r'([\d,]+)\s+stars', info)
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    else:
        stars = 0
        
    # Extract project name
    # Pattern 1: "The project ([^ ]+) is hosted"
    # Pattern 2: "The project named ([^ ]+) is hosted"
    # Pattern 3: "The project named ([^ ]+) on GitHub"
    # Pattern 4: "The project ([^ ]+) on GitHub"
    # Pattern 5: "hosted on GitHub under the name ([^, ]+)"
    
    # Common project name pattern: "owner/repo"
    # Let's search for "owner/repo" pattern near "The project" or "project named".
    # Or just search for any string "A/B" in the text? Might be risky.
    # Let's try specific patterns.
    
    name = None
    if "hosted on GitHub under the name" in info:
        m = re.search(r'hosted on GitHub under the name\s+([\w\-\.]+/[^\s,]+)', info)
        if m: name = m.group(1)
    elif "project named" in info:
        m = re.search(r'project named\s+([\w\-\.]+/[^\s,]+)', info)
        if m: name = m.group(1)
    elif "The project" in info:
        # Try to match the word after "The project"
        # Avoid matching "is", "on", etc.
        m = re.search(r'The project\s+([\w\-\.]+/[^\s,]+)', info)
        if m: name = m.group(1)
        
    # If regex failed, maybe I can just split by space and look for "owner/repo" format?
    if not name:
        parts = info.split()
        for p in parts:
            if '/' in p and not p.startswith('http') and not p.endswith('.'):
                # Simple check for owner/repo
                if re.match(r'^[\w\-\.]+/[\w\-\.]+$', p):
                    name = p
                    break
    
    if name:
        # Clean up punctuation
        name = name.rstrip('.,')
        project_stars[name] = stars

# Load project_packageversion
with open(locals()['var_function-call-17646360106339151605'], 'r') as f:
    pp_data = json.load(f)

# Filter pp_data for projects in project_stars
# List of (Name, Version, ProjectName)
mapping = []
for row in pp_data:
    pname = row.get('ProjectName')
    if pname and pname in project_stars:
        mapping.append(row)

# Load packageinfo
with open(locals()['var_function-call-17646360106339151180'], 'r') as f:
    pkg_data = json.load(f)

# Convert pkg_data to DataFrame to find latest version
df_pkg = pd.DataFrame(pkg_data)
# Ensure UpstreamPublishedAt is float
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')

# Find latest version for each Name
# Sort by Name and Date desc, then drop duplicates keeping first
latest_versions = df_pkg.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name', keep='first')
latest_versions_map = latest_versions.set_index('Name')['Version'].to_dict()

# Filter mapping to keep only latest versions
final_list = []
for row in mapping:
    pkg_name = row['Name']
    pkg_ver = row['Version']
    project_name = row['ProjectName']
    
    # Check if this is the latest version
    if pkg_name in latest_versions_map and latest_versions_map[pkg_name] == pkg_ver:
        # Get stars
        stars = project_stars.get(project_name, 0)
        final_list.append({
            'Package': pkg_name,
            'Version': pkg_ver,
            'Project': project_name,
            'Stars': stars
        })

# Create DataFrame, sort by Stars desc
df_final = pd.DataFrame(final_list)
# Remove duplicates if any (same package mapping to same project multiple times?)
df_final = df_final.drop_duplicates(subset=['Package'])
# Sort
top_5 = df_final.sort_values('Stars', ascending=False).head(5)

print("__RESULT__:")
print(top_5[['Package', 'Version', 'Stars']].to_json(orient='records'))"""

env_args = {'var_function-call-14557066858108351976': ['packageinfo'], 'var_function-call-14557066858108354359': ['project_info', 'project_packageversion'], 'var_function-call-4780743343946175729': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-4780743343946177256': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-8791064489498277390': [{'count(*)': '661372'}], 'var_function-call-8791064489498279551': [{'count_star()': '597602'}], 'var_function-call-8791064489498277616': [{'count_star()': '770'}], 'var_function-call-1247615843400787734': 'file_storage/function-call-1247615843400787734.json', 'var_function-call-17646360106339151605': 'file_storage/function-call-17646360106339151605.json', 'var_function-call-17646360106339151180': 'file_storage/function-call-17646360106339151180.json'}

exec(code, env_args)
