code = """import pandas as pd
import json
import re

# Access file paths
path_project_info = locals()['var_function-call-16975548899778660295']
path_ppv = locals()['var_function-call-2264476726664710435']
path_pkg = locals()['var_function-call-2264476726664712078']

# Load project_info
with open(path_project_info) as f:
    project_info_list = json.load(f)

# Parse project info
project_stars = {}

def parse_stars(text):
    text_clean = text.replace(',', '')
    m = re.search(r'stars count of (\d+)', text_clean)
    if m: return int(m.group(1))
    m = re.search(r'(\d+) stars', text_clean)
    if m: return int(m.group(1))
    m = re.search(r'(\d+) star', text_clean)
    if m: return int(m.group(1))
    return 0

def parse_project_name(text):
    patterns = [
        r'project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)',
        r'named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)',
        r'name ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)',
        r'project is a GitHub repository named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)'
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            name = m.group(1)
            if name.endswith('.'): name = name[:-1]
            if name.endswith(','): name = name[:-1]
            return name
    return None

for entry in project_info_list:
    desc = entry.get('Project_Information', '')
    name = parse_project_name(desc)
    stars = parse_stars(desc)
    if name:
        project_stars[name] = stars

# Load project_packageversion
with open(path_ppv) as f:
    ppv_list = json.load(f)

# Filter ppv
valid_projects = set(project_stars.keys())
ppv_filtered = [x for x in ppv_list if x.get('ProjectName') in valid_projects]
df_ppv = pd.DataFrame(ppv_filtered)

# Load packageinfo
with open(path_pkg) as f:
    pkg_list = json.load(f)

df_pkg = pd.DataFrame(pkg_list)

# Process pkg
def is_release(info_str):
    if not info_str: return False
    try:
        d = json.loads(info_str)
        return d.get('IsRelease', False)
    except:
        return False

df_pkg['IsRelease'] = df_pkg['VersionInfo'].apply(is_release)
df_pkg = df_pkg[df_pkg['IsRelease'] == True]

df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name', 'Version']]

if not df_ppv.empty:
    merged = pd.merge(df_latest, df_ppv, on=['Name', 'Version'], how='inner')
    merged['Stars'] = merged['ProjectName'].map(project_stars)
    merged = merged.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])
    result = merged.sort_values(by='Stars', ascending=False).head(5)
    print("__RESULT__:")
    print(result[['Name', 'Version', 'Stars']].to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-14041441666248180991': ['project_info', 'project_packageversion'], 'var_function-call-14041441666248182542': ['packageinfo'], 'var_function-call-12036119204174710905': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-12036119204174711320': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-12036119204174711735': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-11657201791391702001': [{'count(*)': '661372'}], 'var_function-call-11657201791391702356': [{'count_star()': '597602'}], 'var_function-call-11657201791391702711': [{'count_star()': '770'}], 'var_function-call-16975548899778660295': 'file_storage/function-call-16975548899778660295.json', 'var_function-call-2264476726664710435': 'file_storage/function-call-2264476726664710435.json', 'var_function-call-2264476726664712078': 'file_storage/function-call-2264476726664712078.json', 'var_function-call-418421774787013996': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}]}

exec(code, env_args)
