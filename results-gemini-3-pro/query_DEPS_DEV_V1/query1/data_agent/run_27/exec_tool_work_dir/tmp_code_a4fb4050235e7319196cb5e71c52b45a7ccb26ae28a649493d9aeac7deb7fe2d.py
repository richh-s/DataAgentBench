code = """import json
import pandas as pd
import re

pinfo_path = locals()['var_function-call-16798371139005880042']
ppv_path = locals()['var_function-call-4051356973218459042']
pkg_path = locals()['var_function-call-12646124071208032916']

# 1. Project Info
with open(pinfo_path, 'r') as f:
    project_info_data = json.load(f)

project_stars = {}
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    p_name = None
    m1 = re.search(r'The project (?!is hosted)([\w\-]+/[\w\-\.]+)', info)
    if m1: p_name = m1.group(1)
    else:
        m2 = re.search(r'under the name ([\w\-]+/[\w\-\.]+)', info)
        if m2: p_name = m2.group(1)
    
    if p_name:
        stars = 0
        m_stars = re.search(r'([\d,]+) stars', info)
        if m_stars: stars = int(m_stars.group(1).replace(',', ''))
        else:
            m_stars2 = re.search(r'stars count of ([\d,]+)', info)
            if m_stars2: stars = int(m_stars2.group(1).replace(',', ''))
        project_stars[p_name] = stars

# 2. Package Info
with open(pkg_path, 'r') as f:
    package_data = json.load(f)
pkg_df = pd.DataFrame(package_data)
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
latest_idx = pkg_df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest_pkg = pkg_df.loc[latest_idx, ['Name', 'Version']]

# 3. Links
with open(ppv_path, 'r') as f:
    ppv_data = json.load(f)
ppv_df = pd.DataFrame(ppv_data)

# Debug lodash
print("Lodash in pkg:", 'lodash' in latest_pkg['Name'].values)
if 'lodash' in latest_pkg['Name'].values:
    ver = latest_pkg[latest_pkg['Name'] == 'lodash']['Version'].values[0]
    print("Lodash latest ver:", ver)
    links = ppv_df[(ppv_df['Name'] == 'lodash') & (ppv_df['Version'] == ver)]
    print("Lodash links:", links.to_dict(orient='records'))

# Filter ppv
ppv_df = ppv_df[ppv_df['ProjectName'].isin(project_stars.keys())]

# Merge
merged = pd.merge(latest_pkg, ppv_df, on=['Name', 'Version'], how='inner')
merged['Stars'] = merged['ProjectName'].map(project_stars)

# Deduplicate by Name (keep highest stars if multiple projects? or just any)
# Usually 1 package -> 1 project. If multiple, take max stars?
merged = merged.sort_values(by='Stars', ascending=False)
merged_unique = merged.drop_duplicates(subset=['Name'])

top10 = merged_unique.head(10)[['Name', 'Version', 'ProjectName', 'Stars']]
print("__RESULT__:")
print(json.dumps(top10.to_dict(orient='records')))"""

env_args = {'var_function-call-15773098157219662905': ['project_info', 'project_packageversion'], 'var_function-call-8430745518218083936': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-2859142733570909284': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-10867351041767233472': [{'count(*)': '661372'}], 'var_function-call-17928122819329189235': [{'count_star()': '597602'}], 'var_function-call-10566044690792379772': [{'count_star()': '770'}], 'var_function-call-16798371139005880042': 'file_storage/function-call-16798371139005880042.json', 'var_function-call-4051356973218459042': 'file_storage/function-call-4051356973218459042.json', 'var_function-call-12646124071208032916': 'file_storage/function-call-12646124071208032916.json', 'var_function-call-13215922259992712374': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@dolsem/actioncable', 'Version': '7.0.0-alpha-simple-5s-step-backoff'}]}

exec(code, env_args)
