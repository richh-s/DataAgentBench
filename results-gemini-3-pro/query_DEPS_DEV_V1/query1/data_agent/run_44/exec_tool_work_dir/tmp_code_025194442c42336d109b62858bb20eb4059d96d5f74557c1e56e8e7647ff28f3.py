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
project_stars = {}

def parse_project_info(text):
    # Extract Project Name
    name = None
    m_name = re.search(r'project\s+(?:named\s+|is\s+a\s+GitHub\s+repository\s+named\s+)?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', text, re.IGNORECASE)
    if m_name:
        name = m_name.group(1)
    else:
        m_name = re.search(r'under\s+the\s+name\s+([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', text, re.IGNORECASE)
        if m_name:
            name = m_name.group(1)
            
    if name and name.endswith(','):
        name = name[:-1]
    
    if not name:
        return None, None

    # Extract Stars
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
package_rows = []
for entry in package_info_data:
    try:
        v_info = json.loads(entry['VersionInfo'])
        is_release = v_info.get('IsRelease', False)
        if is_release:
            package_rows.append({
                'Name': entry['Name'],
                'Version': entry['Version'],
                'PublishedAt': float(entry['UpstreamPublishedAt'])
            })
    except:
        continue

df_packages = pd.DataFrame(package_rows)

if not df_packages.empty:
    df_latest = df_packages.sort_values(by=['Name', 'PublishedAt'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')
else:
    df_latest = pd.DataFrame(columns=['Name', 'Version'])

latest_versions = set(zip(df_latest['Name'], df_latest['Version']))

# 3. Process Project Mapping
results = []
seen_packages = set()

for entry in project_package_data:
    p_name = entry['Name']
    p_ver = entry['Version']
    proj_name = entry['ProjectName']
    
    if (p_name, p_ver) in latest_versions:
        stars = project_stars.get(proj_name, 0)
        # Avoid duplicate package entries if multiple project mappings (unlikely for 1 version but possible)
        if p_name not in seen_packages:
            results.append({
                'Package': p_name,
                'Version': p_ver,
                'Stars': stars,
                'Project': proj_name
            })
            seen_packages.add(p_name)

# 4. Sort and Top 20
df_results = pd.DataFrame(results)
if not df_results.empty:
    df_results = df_results.sort_values(by='Stars', ascending=False)
    top_20 = df_results.head(20)[['Package', 'Version', 'Stars', 'Project']]
    final_output = top_20.to_dict(orient='records')
else:
    final_output = []

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-2706936669194307738': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-9928628453520016703': [{'count(*)': '661372'}], 'var_function-call-8985349422324017409': [{'count_star()': '597602'}], 'var_function-call-6130787592698314376': [{'count_star()': '770'}], 'var_function-call-6170568374372301766': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-14873809826180698413': 'file_storage/function-call-14873809826180698413.json', 'var_function-call-13208149251224258601': 'file_storage/function-call-13208149251224258601.json', 'var_function-call-2349627184319086272': 'file_storage/function-call-2349627184319086272.json', 'var_function-call-1758140346329882875': [{'Package': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Package': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464}, {'Package': '@dpoineau/react-scripts>1.0.0>lodash.clonedeep', 'Version': '4.5.0', 'Stars': 57779}], 'var_function-call-8268120015157661868': [], 'var_function-call-11632949306346248062': [{'System': 'NPM'}], 'var_function-call-674800854312752890': [], 'var_function-call-14835001496578382737': [], 'var_function-call-11052674589669464674': [{'RelationType': 'SOURCE_REPO_TYPE'}, {'RelationType': 'ISSUE_TRACKER_TYPE'}]}

exec(code, env_args)
