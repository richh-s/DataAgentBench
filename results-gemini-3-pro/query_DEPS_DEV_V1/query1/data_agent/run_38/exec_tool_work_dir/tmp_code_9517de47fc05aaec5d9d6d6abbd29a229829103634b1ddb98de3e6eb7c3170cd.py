code = """import json
import pandas as pd
import re

# Load Project Info
with open(locals()['var_function-call-15886949842167622299'], 'r') as f:
    project_info_data = json.load(f)

# Parse Project Info
projects = []
# Regex to find project name: "The project [name] ..." or "The GitHub project [name] ..." or "The project named [name] ..."
# Regex to find stars: "X stars" or "stars count of X" or "total of X stars"
# Examples:
# "The project leaflet/leaflet on GitHub ..." -> Name: leaflet/leaflet
# "... 38715 stars ..." -> Stars: 38715
# "... stars count of 3761 ..." -> Stars: 3761
# "... total of 2,534 stars ..." -> Stars: 2534

# Combined regex strategy might be complex, so I'll do two passes or look specifically.
# Name pattern: after "The project " or "The GitHub project " or "The project is hosted on GitHub under the name "
# It seems the text structure is somewhat consistent.
# "The project X is hosted..."
# "The project X on GitHub..."
# "The GitHub project named X currently..."
# "The project named X is..."
# "The project is hosted on GitHub under the name X, and..."

for entry in project_info_data:
    text = entry.get('Project_Information', '')
    if not text:
        continue
    
    # Extract Name
    name_match = re.search(r'The (?:GitHub )?project (?:is hosted on GitHub under the name |named |on GitHub, named )?([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', text)
    if not name_match:
        # Fallback for simple "The project X"
        name_match = re.search(r'The (?:GitHub )?project ([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', text)
    
    project_name = None
    if name_match:
        project_name = name_match.group(1)
    
    # Extract Stars
    # Look for "X stars" or "stars count of X"
    stars_match = re.search(r'(\d+(?:,\d+)*) stars', text)
    if not stars_match:
        stars_match = re.search(r'stars count of (\d+(?:,\d+)*)', text)
    
    stars = 0
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    
    if project_name:
        projects.append({'ProjectName': project_name, 'Stars': stars})

df_projects = pd.DataFrame(projects)

# Load Project Package Version
with open(locals()['var_function-call-444880856909815404'], 'r') as f:
    ppv_data = json.load(f)
df_ppv = pd.DataFrame(ppv_data)

# Load Package Info
with open(locals()['var_function-call-12516034446023091941'], 'r') as f:
    pkg_data = json.load(f)
df_pkg = pd.DataFrame(pkg_data)

# 1. Identify Latest Versions in Package Info
# Convert UpstreamPublishedAt to numeric
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Date desc
df_pkg_sorted = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates on Name, keeping first (latest)
df_latest = df_pkg_sorted.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]
df_latest['is_latest'] = True

# 2. Join Project Mapping with Projects (Stars)
# df_ppv has Name, Version, ProjectName
# df_projects has ProjectName, Stars
df_mapped = pd.merge(df_ppv, df_projects, on='ProjectName', how='inner')

# 3. Filter for Latest Versions
# Join df_mapped with df_latest on Name and Version
df_final = pd.merge(df_mapped, df_latest, on=['Name', 'Version'], how='inner')

# 4. Sort by Stars
df_final = df_final.sort_values(by='Stars', ascending=False)

# 5. Top 5
top_5 = df_final[['Name', 'Version', 'Stars']].head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-17632385162144977339': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-17936339978084971575': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'UpstreamPublishedAt': '1651424462000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'UpstreamPublishedAt': '1666049703000000.0'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'UpstreamPublishedAt': '1637610934000000.0'}], 'var_function-call-3481648233324390033': ['project_info', 'project_packageversion'], 'var_function-call-4332136606606608238': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-1322133517653074183': [{'COUNT(*)': '661372'}], 'var_function-call-16342152212161679902': [{'count_star()': '597602'}], 'var_function-call-2050267083909317145': [{'count_star()': '770'}], 'var_function-call-15886949842167622299': 'file_storage/function-call-15886949842167622299.json', 'var_function-call-444880856909815404': 'file_storage/function-call-444880856909815404.json', 'var_function-call-12516034446023091941': 'file_storage/function-call-12516034446023091941.json'}

exec(code, env_args)
