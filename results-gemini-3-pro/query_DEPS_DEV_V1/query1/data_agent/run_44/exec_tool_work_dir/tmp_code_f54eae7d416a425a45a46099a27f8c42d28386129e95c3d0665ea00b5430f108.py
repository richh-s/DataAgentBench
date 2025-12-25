code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-14873809826180698413'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-13208149251224258601'], 'r') as f:
    project_package_data = json.load(f)

with open(locals()['var_function-call-2349627184319086272'], 'r') as f:
    package_info_data = json.load(f)

# 1. Parse Project Info
# "The project lberrocal/npm-packages-template is hosted..."
# "The project named leo-ran/easy-node-server is hosted..."
# "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
# "The GitHub project ledgerproject/keypairoom currently..."
# "... has 38715 stars..."
# "... stars count of 3761..."
# "... total of 2,534 stars..."

project_stars = {}

def parse_project_info(text):
    # Extract Project Name
    # Patterns for name:
    # 1. "project (is a GitHub repository named )?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)"
    # 2. "under the name ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)"
    
    name = None
    # Pattern 1: Standard "project owner/repo"
    m_name = re.search(r'project\s+(?:named\s+|is\s+a\s+GitHub\s+repository\s+named\s+)?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', text, re.IGNORECASE)
    if m_name:
        name = m_name.group(1)
    else:
        # Pattern 2: "under the name owner/repo"
        m_name = re.search(r'under\s+the\s+name\s+([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', text, re.IGNORECASE)
        if m_name:
            name = m_name.group(1)
            
    # Remove trailing punctuation if captured
    if name and name.endswith(','):
        name = name[:-1]
    
    if not name:
        return None, None

    # Extract Stars
    # Patterns:
    # 1. "(\d+(?:,\d+)*) stars"
    # 2. "stars count of (\d+(?:,\d+)*)"
    stars = 0
    m_stars = re.search(r'(\d+(?:,\d+)*)\s+stars', text)
    if not m_stars:
        m_stars = re.search(r'stars\s+count\s+of\s+(\d+(?:,\d+)*)', text)
    
    if m_stars:
        stars_str = m_stars.group(1).replace(',', '')
        stars = int(stars_str)
    
    return name, stars

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    p_name, p_stars = parse_project_info(info)
    if p_name is not None:
        project_stars[p_name] = p_stars

# 2. Process Package Info to find Latest Release Version
# Data: Name, Version, UpstreamPublishedAt, VersionInfo
package_rows = []
for entry in package_info_data:
    try:
        v_info = json.loads(entry['VersionInfo'])
        is_release = v_info.get('IsRelease', False)
        # We only care about releases
        if is_release:
            package_rows.append({
                'Name': entry['Name'],
                'Version': entry['Version'],
                'PublishedAt': float(entry['UpstreamPublishedAt'])
            })
    except:
        continue

df_packages = pd.DataFrame(package_rows)

# Find latest version for each package
# Sort by Name and PublishedAt desc, then drop duplicates keeping first
if not df_packages.empty:
    df_latest = df_packages.sort_values(by=['Name', 'PublishedAt'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')
else:
    df_latest = pd.DataFrame(columns=['Name', 'Version'])

# Create a set or map for fast lookup
# Key: (Name, Version) -> True
latest_versions = set(zip(df_latest['Name'], df_latest['Version']))

# 3. Process Project Mapping
# project_package_data: Name, Version, ProjectName
# We filter this list: keep only if (Name, Version) is in latest_versions
# Then map to ProjectName -> Stars

results = []

for entry in project_package_data:
    p_name = entry['Name']
    p_ver = entry['Version']
    proj_name = entry['ProjectName']
    
    if (p_name, p_ver) in latest_versions:
        # Get stars
        stars = project_stars.get(proj_name, 0)
        results.append({
            'Package': p_name,
            'Version': p_ver,
            'Stars': stars,
            'Project': proj_name
        })

# 4. Sort and Top 5
df_results = pd.DataFrame(results)
if not df_results.empty:
    df_results = df_results.sort_values(by='Stars', ascending=False)
    # Deduplicate by Package Name (in case multiple projects map to same package?? Unlikely for latest version but just in case)
    df_results = df_results.drop_duplicates(subset=['Package'])
    top_5 = df_results.head(5)[['Package', 'Version', 'Stars']]
    
    # Convert to list of dicts
    final_output = top_5.to_dict(orient='records')
else:
    final_output = []

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-2706936669194307738': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-9928628453520016703': [{'count(*)': '661372'}], 'var_function-call-8985349422324017409': [{'count_star()': '597602'}], 'var_function-call-6130787592698314376': [{'count_star()': '770'}], 'var_function-call-6170568374372301766': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-14873809826180698413': 'file_storage/function-call-14873809826180698413.json', 'var_function-call-13208149251224258601': 'file_storage/function-call-13208149251224258601.json', 'var_function-call-2349627184319086272': 'file_storage/function-call-2349627184319086272.json'}

exec(code, env_args)
