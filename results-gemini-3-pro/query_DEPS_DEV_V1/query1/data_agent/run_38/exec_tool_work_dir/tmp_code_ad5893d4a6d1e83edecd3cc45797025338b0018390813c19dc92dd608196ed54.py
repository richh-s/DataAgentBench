code = """import json
import pandas as pd
import re

# Load Project Info
with open(locals()['var_function-call-15886949842167622299'], 'r') as f:
    project_info_data = json.load(f)

projects = []
for entry in project_info_data:
    text = entry.get('Project_Information', '')
    if not text:
        continue
    
    # Improved Name Extraction
    # Try to capture strictly the name.
    # Pattern 1: "The project X on GitHub..."
    # Pattern 2: "The project X is hosted..."
    # Pattern 3: "The GitHub project named X currently..."
    # Pattern 4: "The project named X is..."
    # Pattern 5: "The project is hosted on GitHub under the name X, and..."
    
    name = None
    # Flexible pattern
    # Look for "project [name]" where name is not "is", "named", "hosted", "on".
    # And name usually contains "/" for owner/repo.
    
    # Strategy: Find "project" then look ahead.
    # We want the string that looks like "owner/repo".
    
    match = re.search(r'project\s+(?:is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name\s+|named\s+|on\s+GitHub\s+named\s+|)([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', text, re.IGNORECASE)
    if match:
        name = match.group(1)
        # Filter out common false positives if any (e.g. "hosted/on") - unlikely with the pattern.
    
    # Extract Stars
    stars = 0
    stars_match = re.search(r'(\d+(?:,\d+)*) stars', text)
    if not stars_match:
        stars_match = re.search(r'stars count of (\d+(?:,\d+)*)', text)
    if stars_match:
        stars = int(stars_match.group(1).replace(',', ''))
    
    if name:
        projects.append({'ProjectName': name, 'Stars': stars})

df_projects = pd.DataFrame(projects)
# Drop duplicates if any (same project info might appear twice?)
df_projects = df_projects.drop_duplicates(subset=['ProjectName'])

# Load Project Package Version
with open(locals()['var_function-call-444880856909815404'], 'r') as f:
    ppv_data = json.load(f)
df_ppv = pd.DataFrame(ppv_data)

# Load Package Info
with open(locals()['var_function-call-12516034446023091941'], 'r') as f:
    pkg_data = json.load(f)
df_pkg = pd.DataFrame(pkg_data)

# Latest Version
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg_sorted = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_pkg_sorted.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

# Merge
# ppv map
df_mapped = pd.merge(df_ppv, df_projects, on='ProjectName', how='inner')
# Join with latest
df_final = pd.merge(df_mapped, df_latest, on=['Name', 'Version'], how='inner')

# Sort
df_final = df_final.sort_values(by='Stars', ascending=False)

top_20 = df_final[['Name', 'Version', 'Stars', 'ProjectName']].head(20).to_dict(orient='records')

print("DEBUG: Top 20 Candidates:")
print(json.dumps(top_20, indent=2))

print("__RESULT__:")
print(json.dumps(top_20[:5])) # Just print top 5 for the result format"""

env_args = {'var_function-call-17632385162144977339': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-17936339978084971575': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'UpstreamPublishedAt': '1651424462000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'UpstreamPublishedAt': '1666049703000000.0'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'UpstreamPublishedAt': '1637610934000000.0'}], 'var_function-call-3481648233324390033': ['project_info', 'project_packageversion'], 'var_function-call-4332136606606608238': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-1322133517653074183': [{'COUNT(*)': '661372'}], 'var_function-call-16342152212161679902': [{'count_star()': '597602'}], 'var_function-call-2050267083909317145': [{'count_star()': '770'}], 'var_function-call-15886949842167622299': 'file_storage/function-call-15886949842167622299.json', 'var_function-call-444880856909815404': 'file_storage/function-call-444880856909815404.json', 'var_function-call-12516034446023091941': 'file_storage/function-call-12516034446023091941.json', 'var_function-call-320376471934704286': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}]}

exec(code, env_args)
